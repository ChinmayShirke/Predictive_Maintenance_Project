from flask import Flask, render_template, jsonify
import pandas as pd
import pickle
import time
import threading
import psycopg2
import os
from dotenv import load_dotenv


# --------------------------- LOAD ENV ---------------------------
load_dotenv()

# --------------------------- FLASK APP ---------------------------
app = Flask(__name__)

# --------------------------- LOAD TRAINED MODEL ---------------------------
MODEL_PATH = "RandomForest (1).pkl"
with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

# --------------------------- POSTGRES CONFIG ---------------------------
db_config = {
    "host": os.getenv("DB_HOST"),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS"),
    "port": os.getenv("DB_PORT")
}

TABLE_NAME = "sensor_data"

FEATURES = ["run_id", "cycle", "status", "temperature", "vibration", "pressure", "current", "datetime"]

REFRESH_RATE = 10  # seconds
latest_result = {"data": {}, "rul": None, "alert": ""}

# --------------------------- FUNCTION TO FETCH LATEST ROW ---------------------------
def fetch_latest_from_db():
    try:
        conn = psycopg2.connect(**db_config)
        query = f"""
            SELECT {", ".join(FEATURES)}
            FROM {TABLE_NAME}
            ORDER BY datetime DESC
            LIMIT 1;
        """
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        print("DB ERROR:", e)
        return None

# --------------------------- BACKGROUND THREAD ---------------------------
def auto_update():
    global latest_result
    while True:
        try:
            df = fetch_latest_from_db()
            if df is None or df.empty:
                latest_result = {"data": {}, "rul": None, "alert": "❌ No data in database"}
            else:
                latest_row = df.iloc[-1:][FEATURES]
                predicted_rul = model.predict(latest_row.drop(columns=["datetime"]))[0]

                if predicted_rul < 10:
                    alert = "danger"
                elif predicted_rul < 25:
                    alert = "warning"
                else:
                    alert = "success"

                latest_result = {
                    "data": latest_row.to_dict(orient="records")[0],
                    "rul": round(float(predicted_rul), 2),
                    "alert": alert
                }
        except Exception as e:
            latest_result = {"data": {}, "rul": None, "alert": f"Error: {str(e)}"}
        time.sleep(REFRESH_RATE)

# Start the updater thread
threading.Thread(target=auto_update, daemon=True).start()

# --------------------------- ROUTES ---------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/latest")
def latest():
    return jsonify(latest_result)

# --------------------------- RUN SERVER ---------------------------
if __name__ == "__main__":
    print("🚀 Flask Server Running on http://127.0.0.1:5000")
    app.run(debug=True)
