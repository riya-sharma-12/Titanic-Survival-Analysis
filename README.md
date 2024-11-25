This repository contains a Logistic Regression model built to predict the survival of passengers aboard the Titanic using features such as age, gender, passenger class, and more. The model is trained on the Titanic dataset available on Kaggle.

Key Features:
Data Preprocessing: Cleaned and transformed raw data into a format suitable for Logistic Regression.
Model Training: Built and trained a Logistic Regression model for binary classification.
Feature Engineering: Extracted and optimized key features like family size, embarkation location, etc.
Model Evaluation: Evaluated using metrics like accuracy, precision, recall, and F1-score.
Deployment:
The Logistic Regression model is deployed on an AWS EC2 instance (t2.micro) using Flask as the web framework.
Users can make predictions via a simple web API or user interface.
Technologies Used:
Python
Scikit-learn (Logistic Regression)
Pandas, NumPy
Flask (for deployment)
AWS EC2 (t2.micro instance)
How to Use:
Clone this repository.
Install the required dependencies with pip install -r requirements.txt.
Start the Flask app to deploy the model locally or on your EC2 instance.
Use the provided API to input data and get predictions.
Explore, fork, and contribute to the project! 🎉
