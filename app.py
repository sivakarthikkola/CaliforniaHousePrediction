from flask import Flask, request, render_template
import joblib
import numpy as np

# Initialize the Flask application
app = Flask(__name__)

# Load the pre-trained model and scaler
model = joblib.load('models/model.pkl')
scaler = joblib.load('models/scaler.pkl')  # Load your scaler

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form
        longitude = float(request.form['longitude'])
        latitude = float(request.form['latitude'])
        housing_median_age = float(request.form['housing_median_age'])
        total_rooms = float(request.form['total_rooms'])
        total_bedrooms = float(request.form['total_bedrooms'])
        population = float(request.form['population'])
        households = float(request.form['households'])
        median_income = float(request.form['median_income'])
        ocean_proximity = request.form['ocean_proximity']

        # Prepare the input data for prediction
        input_data = np.array([[longitude, latitude, housing_median_age,
                                total_rooms, total_bedrooms,
                                population, households,
                                median_income, ocean_proximity]])

        # Scale the input data using the loaded scaler
        scaled_input_data = scaler.transform(input_data)

        # Make prediction using the scaled data
        prediction = model.predict(scaled_input_data)

        # Render the result page with the prediction
        return render_template('result.html', prediction=prediction[0])
    
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)