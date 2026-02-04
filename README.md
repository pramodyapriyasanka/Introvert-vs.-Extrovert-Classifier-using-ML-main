
# 🧠 Introvert vs. Extrovert Classifier

An AI-powered web application that predicts a person's personality type (Introvert or Extrovert) based on their social habits and behavioral patterns. This project uses **Machine Learning** for classification and **Flask** for the web interface.

## 🚀 Features
* **Accurate Prediction:** Uses a trained Random Forest/Logistic Regression model (based on your implementation).
* **Web Interface:** Simple and user-friendly UI built with HTML/CSS.
* **Scalable:** Prepared for deployment on platforms like Render or Heroku.
* **Real-time Processing:** Get instant results based on user input.

## 🛠️ Tech Stack
* **Language:** Python
* **Framework:** Flask
* **Libraries:** Pandas, Scikit-learn, Joblib
* **Frontend:** HTML5, CSS3

## 📁 Project Structure
```text
├── model/
│   ├── model.pkl            # Trained ML model
│   ├── scaler.pkl           # Feature scaler
│   ├── label_encoder.pkl    # Encoder for output labels
│   └── columns.json         # Reference for feature columns
├── templates/
│   └── index.html           # Web interface
├── app.py                   # Main Flask application
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation

```

## ⚙️ Installation & Setup

1. **Clone the repository:**
```bash
git clone [https://github.com/pramodyapriyasanka/Introvert-vs.-Extrovert-Classifier-using-ML-main.git](https://github.com/pramodyapriyasanka/Introvert-vs.-Extrovert-Classifier-using-ML-main.git)
cd Introvert-vs.-Extrovert-Classifier-using-ML-main

```


2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```


4. **Run the application:**
```bash
python app.py

```


Open `http://127.0.0.1:10000` in your browser.

## 📊 Data Features Used

The model predicts based on:

* Time spent alone
* Stage fear levels
* Social event attendance frequency
* Socializing battery (Drained after socializing)
* Friends circle size
* Social media post frequency

## 📸 App Screenshots

<img width="1899" height="989" alt="Dashboard" src="https://github.com/user-attachments/assets/c9b4f5ed-8edd-4627-9ae7-7188fe01fa60" />


## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

---

Developed by [Pramodya Priyasanka](https://[www.google.com/search?q=https://github.com/pramodyapriyasanka](https://github.com/pramodyapriyasanka))


