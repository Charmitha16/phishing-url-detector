from flask import Flask, request, render_template
import joblib
import numpy as np
from feature_extractor import extract_features  # Import your function

# Initialize the Flask application
app = Flask(__name__)

# Load your trained model
# Make sure 'phishing_url_detector.joblib' is in the same folder
model = joblib.load('phishing_url_detector.joblib')

# Define the main route for the home page
@app.route('/')
def home():
    # Render the index.html template from the 'templates' folder
    return render_template('index.html')

# Define the route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the URL from the form submission
    url = request.form['url']
    
    # Extract features from the URL using your function
    features = extract_features(url)
    
    # Reshape features for the model prediction
    final_features = np.array(features).reshape(1, -1)
    
    # Make a prediction
    prediction = model.predict(final_features)
    
    # Determine the output text based on the prediction
    if prediction[0] == 1:
        output = "This URL is likely a Phishing attempt!"
    else:
        output = "This URL seems Legitimate."
        
    # Render the index.html template again, but this time with the prediction result
    return render_template('index.html', prediction_text=output)

# Run the app when the script is executed
if __name__ == '__main__':
    app.run(debug=True)