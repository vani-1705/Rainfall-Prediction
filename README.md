# 🌧️ Rainfall Prediction

A Machine Learning-based weather forecasting web application that predicts whether it will rain tomorrow, based on historical weather conditions.

🔗 **GitHub Repo:** https://github.com/vani-1705/Rainfall-Prediction
🚀 **Live App:** https://rainfall-prediction-beryl.vercel.app/

---

## 📖 Overview

The system analyzes meteorological parameters such as temperature, humidity, rainfall, wind speed, wind direction, pressure, cloud cover, and sunshine to generate rainfall predictions. Multiple classification algorithms were trained and compared, and the best-performing model (Random Forest) is served through a Flask web application with a simple, user-friendly interface.

---

## ✅ Project Requirements vs What Was Used

| Requirement (given in project) | Used in this project |
|---|---|
| Python | ✅ Python 3 |
| Pandas | ✅ Used for data loading, cleaning, preprocessing |
| NumPy | ✅ Used for numerical operations |
| Matplotlib | ✅ Used for distribution plots, ROC curve |
| Seaborn | ✅ Used for heatmap, count plots |
| Scikit-Learn | ✅ Used for preprocessing, models, evaluation metrics |
| Flask | ✅ Used for backend web application |
| HTML | ✅ Used for `index.html`, `chance.html`, `noChance.html` |
| CSS | ✅ Used for styling (`style.css`) |
| Logistic Regression | ✅ Trained and compared |
| Decision Tree | ✅ Trained and compared |
| Random Forest | ✅ Trained and compared — **final model used in production** |
| KNN | ✅ Trained and compared |
| SVM | ✅ Trained and compared |
| XGBoost | ✅ Trained and compared |
| Anaconda / Jupyter Notebook | ✅ Used for development (`Rainfall_Prediction.ipynb`) |
| JavaScript *(not originally required)* | ➕ Added extra, for basic form validation (`script.js`) |
| Deployment *(not originally required)* | ➕ Added extra — deployed live on **Vercel** for demo purposes |

> Everything listed as a requirement in the project brief has been used. JavaScript and live deployment were added on top, as enhancements.

---

## 🧠 Machine Learning Models Compared

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier ⭐ *(final model)*
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Gradient Boosting (GBM)
- XGBoost

## 📊 Model Performance

| Metric | Score |
|---|---|
| Train Accuracy | ~99% |
| Test Accuracy | ~85% |
| ROC-AUC | ~0.88 |

---

## 🗂️ Project Structure

```
rainfall_prediction/
│
├── app.py                     ⚙️ Flask backend
├── requirements.txt           📦 Python dependencies
├── vercel.json                 🔧 Vercel function config
├── Rainfall_Prediction.ipynb   📓 ML notebook (data → model → save)
├── rainfall.pkl                🧠 Trained Random Forest model
├── scale.pkl                    ⚖️ StandardScaler used during training
│
├── templates/
│   ├── index.html              📝 Input form page
│   ├── chance.html             🌧️ "Rain expected" result page
│   └── noChance.html           ☀️ "No rain" result page
│
└── public/
    ├── style.css                🎨 Styling
    ├── script.js                  ✔️ Form validation
    └── background.jpg           🖼️ Background image
```

---

## 📁 Dataset

- **Source:** Kaggle — Rain in Australia (`weatherAUS.csv`)
- **Rows:** 142,193
- **Target column:** `RainTomorrow` (Yes/No)

> Note: `weatherAUS.csv` is only needed while training the model in the notebook. It is **not** required for running or deploying the app, since the trained model (`rainfall.pkl`) is already included.

---

## ⚙️ How It Works

1. 🧍 User enters weather parameters (location, temperature, humidity, wind, pressure, etc.) in the web form.
2. 🔄 Flask backend receives the input and scales it using the same `StandardScaler` used during training.
3. 🤖 The trained Random Forest model predicts whether it will rain tomorrow.
4. 📄 The result page (chance / no chance of rain) is displayed to the user.

---

## 💻 Running Locally

```bash
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000/` in your browser.

## 🏋️ Training the Model Yourself

1. Place `weatherAUS.csv` in the same folder as `Rainfall_Prediction.ipynb`.
2. Run all cells in the notebook.
3. This regenerates `rainfall.pkl`, `scale.pkl`, `encoder.pkl`, and `imputer.pkl`.

## ☁️ Deployment (Vercel)

1. Push this project to a GitHub repository.
2. Go to [vercel.com/new](https://vercel.com/new) and import the repository.
3. Vercel auto-detects the Flask app (via `app.py` and `requirements.txt`).
4. Click **Deploy**.

Live demo: **https://rainfall-prediction-beryl.vercel.app/**

---
