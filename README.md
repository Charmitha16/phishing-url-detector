Project Report: AI-Powered Phishing URL Detector
1. Abstract
This document outlines the development of a machine learning-based Phishing URL Detector. The project aims to address the persistent cybersecurity threat of phishing by creating an intelligent system capable of classifying URLs as either 'Legitimate' or 'Phishing'. The system uses a RandomForestClassifier trained on features extracted from a large dataset of URLs. The final output is a functional web application where a user can input a URL and receive a real-time prediction of its authenticity.

2. Methodology
The project was executed in a series of sequential steps, from data collection and preparation to model training and deployment.

2.1. Data Collection
Two distinct datasets were used to create a comprehensive training corpus:

Legitimate URLs: Sourced from the Tranco Top 1 Million list, providing a large and diverse set of safe domains.

Phishing URLs: Sourced from a verified online collection containing examples of real-world phishing links.

2.2. Data Preprocessing
The raw data was cleaned and standardized to ensure model accuracy. The most critical preprocessing step was URL Normalization. A custom function was created to ensure every URL in the dataset (both legitimate and phishing) was formatted with a protocol (https://). This step was vital for maintaining consistency during feature extraction and preventing the model from learning incorrect patterns based on URL format.

2.3. Feature Engineering
Four key features were engineered from each URL string to provide the model with quantitative data for classification:

URL Length: The total number of characters in the URL string.

Dot Count: The number of periods (.) in the URL.

Sensitive Word Count: A binary feature that checks for the presence of keywords often associated with phishing (e.g., login, secure, account, verify).

Subdomain Count: The number of parts in the URL's hostname (e.g., www.google.com has 3).

2.4. Model Training and Evaluation
Model Choice: A RandomForestClassifier was selected due to its high performance and robustness in classification tasks.

Handling Imbalance: To address the imbalance between the number of legitimate and phishing URLs, two techniques were used:

Stratified Splitting: When splitting the data into training and testing sets, stratify=y was used to ensure both sets had the same proportion of phishing and legitimate examples.

Class Weighting: During training, the class_weight='balanced' parameter was set, which automatically gives more importance to the minority class (phishing URLs), preventing the model from being biased towards the majority class.

Evaluation: The model's performance was measured using standard classification metrics, including Accuracy, Precision, and Recall.

3. Tools and Technologies
Language: Python 3

Libraries:

Pandas: For data manipulation and processing.

Scikit-learn: For feature engineering, model training, and evaluation.

Joblib: For saving and loading the trained model.

Flask: For creating the final web application.

Frontend: HTML

4. Results
The trained model successfully learned the patterns differentiating phishing links from legitimate ones. The final output is a functional web application that loads the saved model (phishing_url_detector.joblib) and provides real-time predictions with a confidence score. The system correctly identifies common phishing techniques like typosquatting and keyword stuffing.

5. Conclusion and Future Work
This project successfully demonstrates the effectiveness of using a RandomForestClassifier for phishing detection. By carefully preprocessing the data and engineering relevant features, a reliable and accurate model was created.

Future improvements could include:

Expanding the Feature Set: Incorporating more advanced features, such as domain age (from a WHOIS lookup) or SSL certificate status.

Regular Retraining: Creating a pipeline to automatically retrain the model with new phishing URLs to keep it effective against emerging threats.

Using More Advanced Models: Experimenting with gradient boosting models (like XGBoost) or neural networks for potentially higher accuracy.







