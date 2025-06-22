from flask import Flask, request, render_template, jsonify
import pandas as pd
import joblib
import json

app = Flask(__name__)

# Load model and artifacts once at startup
model = joblib.load('model/model.pkl')
scaler = joblib.load('model/scaler.pkl')
label_encoder = joblib.load('model/label_encoder.pkl')
with open('model/columns.json', 'r') as f:
    model_columns = json.load(f)


def safe_float(value, field_name):
    """
    Convert value to float safely; raise ValueError with clear message if invalid.
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid or missing value for {field_name}: '{value}'")


def preprocess_and_predict(input_data):
    """
    Preprocess input data and return model prediction label.
    """
    df = pd.DataFrame([input_data])

    # One-hot encode categorical variables
    df_encoded = pd.get_dummies(df, drop_first=True)

    # Ensure columns match training data
    df_encoded = df_encoded.reindex(columns=model_columns, fill_value=0)

    # Scale features
    df_scaled = scaler.transform(df_encoded)

    # Predict using the loaded model
    prediction = model.predict(df_scaled)

    # Decode label
    result = label_encoder.inverse_transform(prediction)[0]
    return result


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        print("Received form data:", request.form)  # Debug log

        # Extract and validate numeric inputs safely
        input_data = {
            'Time_spent_Alone': safe_float(request.form.get('Time_spent_Alone'), 'Time_spent_Alone'),
            'Stage_fear': request.form.get('Stage_fear'),
            'Social_event_attendance': request.form.get('Social_event_attendance'),
            'Going_outside': request.form.get('Going_outside'),
            'Drained_after_socializing': request.form.get('Drained_after_socializing'),
            'Friends_circle_size': safe_float(request.form.get('Friends_circle_size'), 'Friends_circle_size'),
            'Post_frequency': safe_float(request.form.get('Post_frequency'), 'Post_frequency'),
        }

        # Validate categorical fields presence
        categorical_fields = ['Stage_fear', 'Social_event_attendance', 'Going_outside', 'Drained_after_socializing']
        for field in categorical_fields:
            if not input_data[field]:
                raise ValueError(f"Invalid or missing value for {field}: ''")

        # Make prediction
        prediction = preprocess_and_predict(input_data)

        return render_template('index.html', prediction_text=f"Predicted Personality: {prediction}")

    except Exception as e:
        print("Error during prediction:", e)  # Debug log
        # Return JSON error with 400 status code
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))  # Render sets the PORT env var
    app.run(host="0.0.0.0", port=port)

