import joblib
from flask import Flask, request, jsonify, render_template

# Load the Titanic model using joblib
model = joblib.load('titanic_model.pkl')

# Initialize Flask app
application = Flask(__name__)

# Route to render the HTML form
@application.route('/')
def index():
    return render_template('index.html')

# Route to handle prediction request
@application.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    pclass = int(request.form['pclass'])
    sex = int(request.form['sex'])
    age = float(request.form['age'])
    sibsp = int(request.form['sibsp'])
    parch = int(request.form['parch'])
    fare = float(request.form['fare'])
    embarked = int(request.form['embarked'])

    # Create feature array
    features = [[pclass, sex, age, sibsp, parch, fare, embarked]]

    # Make prediction
    prediction = model.predict(features)[0]

    # Return the result as JSON
    return jsonify({'prediction': int(prediction)})

# Run the Flask app
# if __name__ == '__main__':
#     app.run(debug=True)
if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000, debug=True)
