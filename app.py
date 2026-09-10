import numpy as np
import joblib
import os
import sys
from flask import Flask, request, render_template
from joblib import parallel_backend

app = Flask(__name__)

try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    BASE_DIR = os.getcwd()

MODEL_PATH = os.path.join(BASE_DIR, 'artifacts/hybrid_model.pkl')

try:
    # We use 'None' (Python), NOT 'null' (JavaScript)
    full_pipeline = joblib.load(MODEL_PATH)
    print(f" Model loaded from: {MODEL_PATH}")
except Exception as e:
    # If load fails, we set it to None so the app doesn't crash immediately
    print(f"Error loading model: {e}")
    full_pipeline = None

SEGMENT_MAP = {
    0: " Highly Active Customer",
    1: " Inactive Customer",
    2: " Loyal Buyer",
    3: " New Potential Customer"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'GET':
        return render_template('index.html')
        
    if full_pipeline is None:
        return render_template('index.html', prediction_text="Error: AI Brain not loaded.")

    try:
        features = [
            float(request.form['Age']),
            float(request.form['Annual_Income']),
            float(request.form['Spending_Score'])
        ]
        
        input_vector = np.array([features])
        
        with parallel_backend('threading', n_jobs=1):
            prediction_array = full_pipeline.predict(input_vector)
            prediction_id = int(prediction_array[0])
            
        segment_name = SEGMENT_MAP.get(prediction_id, "Unknown Segment")
        
        return render_template('index.html', 
                             prediction_text=segment_name,
                             input_data=features)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
