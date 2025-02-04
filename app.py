from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import os
import random
import string

app = Flask(__name__)
model = load_model('weights.h5')

# Ensure the 'uploads' folder exists
if not os.path.exists('static/uploads'):
    os.makedirs('static/uploads')

# Allowed file extensions
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

# Check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(image):
    # Resize the image to fit the model input and normalize
    img = image.resize((128, 128))
    img = np.array(img)
    img = img / 255.0
    return img

@app.route('/classify', methods=['POST'])
def classify_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'})

    # Get form data
    name = request.form.get('name')
    contact = request.form.get('contact')

    # Get uploaded image
    image = request.files['image']

    # Ensure the uploaded file has an allowed extension
    if not allowed_file(image.filename):
        return jsonify({'error': 'Invalid file type. Only jpg, jpeg, and png are allowed.'})

    # Create a random filename for the uploaded image
    image_filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12)) + '.' + image.filename.rsplit('.', 1)[1].lower()
    image_path = os.path.join('static/uploads', image_filename)

    # Save the image to the uploads folder
    image.save(image_path)

    # Preprocess the image for prediction
    img = preprocess_image(Image.open(image_path))
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img)

    # Extract confidence value (assuming it's a binary classification)
    confidence = prediction[0][0]  # Get the probability value

    # Make the prediction and analyze it
    if confidence > 0.58:
        pred = "Malignant"
        confidence_percentage = confidence * 100
        analysis = "The lesion appears to be malignant. Immediate consultation with a healthcare provider is recommended."
    else:
        pred = "Benign"
        confidence_percentage = (1 - confidence) * 100
        analysis = "The lesion appears to be benign, but monitoring for any changes is advised."

    # Render the result page with the prediction, confidence, analysis, and patient info
    return render_template('index.html', name=name, contact=contact, pred=pred, confidence=confidence_percentage, analysis=analysis, image_filename=image_filename)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
