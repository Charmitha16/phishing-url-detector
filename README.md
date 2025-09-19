
# AI-Powered Phishing URL Detector 🎣

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Framework](https://img.shields.io/badge/Flask-2.0-lightgrey)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.x-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A web application that uses a machine learning model to detect phishing URLs in real-time. This project demonstrates a complete machine learning workflow, from data preparation and feature engineering to model training and deployment as a web service.

---

## 🚀 Key Features

* **Real-time Prediction:** Instantly classifies a URL as either 'Legitimate' or 'Phishing'.
* **Machine Learning Model:** Utilizes a trained `RandomForestClassifier` for high accuracy.
* **Feature Engineering:** Extracts key features from URLs, including URL length, subdomain count, dot count, and the presence of sensitive keywords.
* **Simple Web Interface:** An easy-to-use interface built with Flask and HTML for user interaction.
* **Trained on Diverse Data:** The model was trained on the Tranco Top 1 Million list for legitimate URLs and a verified online collection for phishing URLs.

---

## 🛠️ Technologies Used

* **Backend:** Python, Flask
* **Machine Learning:** Scikit-learn, Pandas
* **Model Persistence:** Joblib
* **Frontend:** HTML

---

## 📁 Project Structure

phishing-url-detector/
│
├── app.py                      # Main Flask application script
├── phishing_url_detector.joblib  # The trained machine learning model
├── prepare_data.py             # Script for data cleaning and preparation
├── train_model.py              # Script for training the model
├── requirements.txt            # List of Python dependencies
│
└── templates/
└── index.html              # The HTML file for the web interface


---

## ⚙️ Setup and Installation

To run this project on your local machine, follow these steps:

**1. Clone the Repository**
(Replace `YOUR_USERNAME/YOUR_REPOSITORY` with your actual GitHub details)
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git)
cd YOUR_REPOSITORY
2. Install Dependencies
It's recommended to create a virtual environment. Then, install the required libraries from the requirements.txt file.

Bash

pip install -r requirements.txt
(If you don't have a requirements.txt file, create one with the content below or install libraries manually: pip install flask pandas scikit-learn joblib)

requirements.txt content:

pandas
scikit-learn
joblib
flask
3. Run the Application
Execute the main Flask script to start the web server.

Bash

python app.py
4. Access the Website
Open your web browser and navigate to the following address:
http://127.0.0.1:5000

📈 Model Details
Model: RandomForestClassifier

Features Used:

URL Length

Dot Count

Sensitive Word Count

Subdomain Count

Performance: (Replace these with the scores from your training script's output)

Accuracy: XX.XX%

Precision: 0.XX

📜 License
This project is licensed under the MIT License.










