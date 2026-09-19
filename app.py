from flask import Flask, render_template, request
import pandas as pd
import pickle

# static_folder=None because Vercel serves everything in public/** directly
# from its CDN - Flask's own static file handling is not used on Vercel.
app = Flask(__name__, static_folder=None)

# ---- Load the saved model and scaler ----
model = pickle.load(open('rainfall.pkl', 'rb'))
sc = pickle.load(open('scale.pkl', 'rb'))

FEATURE_COLUMNS = [
    'Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine',
    'WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm',
    'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm',
    'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm',
    'Temp9am', 'Temp3pm', 'RainToday'
]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    form_values = [float(request.form.get(col)) for col in FEATURE_COLUMNS]
    input_df = pd.DataFrame([form_values], columns=FEATURE_COLUMNS)

    input_scaled = sc.transform(input_df)
    input_scaled = pd.DataFrame(input_scaled, columns=FEATURE_COLUMNS)

    prediction = model.predict(input_scaled)[0]

    if prediction == 0:
        return render_template('noChance.html')
    else:
        return render_template('chance.html')


# Vercel's Python runtime looks for a Flask instance named `app` -
# no app.run() needed; Vercel handles the WSGI server itself.
if __name__ == '__main__':
    app.run(debug=True)
