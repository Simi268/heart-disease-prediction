from flask import Flask, request, render_template
import pandas as pd
import joblib
import sqlite3

# =========================
# Load trained pipeline
# =========================
model = joblib.load("model_pipeline.pkl")

# =========================
# Setup Flask
# =========================
application = Flask(__name__)

# =========================
# Setup Database (SQLite)
# =========================
conn = sqlite3.connect("heart_predictions.db", check_same_thread=False)
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age INTEGER,
    sex TEXT,
    chest_pain TEXT,
    resting_ecg TEXT,
    exercise_angina TEXT,
    st_slope TEXT,
    other_features TEXT,
    prediction INTEGER
)
""")
conn.commit()

# =========================
# Home Page
# =========================
@application.route('/')
def home():
    return render_template("index.html")

# =========================
# Predict Endpoint
# =========================
@application.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form.to_dict()

        # Convert to DataFrame (1 row)
        df = pd.DataFrame([data])

        # Run prediction (pipeline handles preprocessing)
        pred = model.predict(df)[0]

        # Save to DB
        cursor.execute("""
            INSERT INTO predictions (age, sex, chest_pain, resting_ecg, exercise_angina, st_slope, other_features, prediction)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data.get("Age"),
            data.get("Sex"),
            data.get("ChestPainType"),
            data.get("RestingECG"),
            data.get("ExerciseAngina"),
            data.get("ST_Slope"),
            str({k:v for k,v in data.items() if k not in ["Age","Sex","ChestPainType","RestingECG","ExerciseAngina","ST_Slope"]}),
            int(pred)
        ))
        conn.commit()

        # Show result page
        return render_template("result.html", prediction=int(pred))

    except Exception as e:
        return render_template("result.html", prediction=f"Error: {str(e)}")
    # =========================
# History Page
# =========================
@application.route('/history')
def history():
    cursor.execute("SELECT * FROM predictions ORDER BY id DESC")
    rows = cursor.fetchall()
    return render_template("history.html", predictions=rows)


# =========================
# Run Flask
# =========================
if __name__ == "__main__":
    application.run(debug=True)
