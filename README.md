# Diagnosis-of-Skin-Lesions-Using-AI
**Overview :**<br>
This project is an AI-powered web application designed to assist in skin lesion detection. Users can upload skin images, which are then analyzed using a deep learning model to predict whether the lesion is benign or malignant. The system aims to provide users with an initial diagnosis, with the suggestion to consult a healthcare professional for further analysis if necessary.<br><br>
**Features :**
<br>Upload skin lesion images via a user-friendly web interface.</br>
AI-driven classification of lesions as benign or malignant.<br>
Analysis of predictions, with recommendations to seek professional consultation if needed.<br><br>
**Technologies Used :**<br>
Python<br>
Flask<br>
TensorFlow/Keras<br>
NumPy & Pandas<br>
OpenCV<br>
HTML, CSS, JavaScript<br><br>
**Installation & Setup** **:**<br>
**Clone this repository** : git clone https://github.com/deeksha0808/Diagnosis-of-Skin-Lesions-Using-AI.git<br>
**Navigate to the project directory** : cd Diagnosis-of-Skin-Lesions-Using-AI<br>
**Install dependencies** :  pip install -r requirements.txt<br>
**Run the Flask app** : python app.py<br>
**Open the browser and go to** : http://127.0.0.1:5000<br><br>
**Project Structure** **:**<br>
/skin-lesion-detection<br>
│── /main.css (Contains CSS, images)<br>
│── /index.html (HTML templates for the frontend)<br>
│── /model (Contains trained model)<br>
│── app.py (Main backend logic using Flask)<br>
│── requirements.txt (Dependencies for the project)<br>
│── README.md (This file)<br>
│── /output image(1.1,1.2) (Screenshots of the project’s output)<br>
│── /launch.json (Configuration file for debugging in VS Code)<br><br>
**How It Works :**<br>
User uploads an image of a skin lesion.<br>
The system processes the image and feeds it into a trained AI model.<br>
The model classifies the lesion as benign or malignant.<br>
The result is displayed, along with a recommendation for further action.<br><br>
**Data Privacy Notice : <br><br>
This project utilizes real patient images for training the AI model. Due to privacy and ethical considerations, the dataset is not included in the GitHub repository. If you wish to use or contribute to the dataset, please ensure compliance with privacy regulations and obtain the necessary permissions. For demonstration purposes, a sample dataset with anonymized images may be used.**<br><br>
**Future Enhancements :**<br>
Improve model accuracy with additional training data.<br>
Deploy on cloud platforms (e.g., AWS, Google Cloud).<br>
Add a real-time API for dermatologist consultations.<br>


