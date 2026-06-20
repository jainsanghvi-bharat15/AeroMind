from flask import Flask, request, render_template
import joblib
import numpy as np
import plotly.graph_objects as go

app = Flask(__name__)

# --- Load models ---
rf = joblib.load("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/ML/random_forest_model.pkl")
prophet_model = joblib.load("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/ML/prophet_model.pkl")
kmeans = joblib.load("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/ML/airport_clustering_model.pkl")
iso = joblib.load("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/ML/isolation_forest_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

# --- Model 1: Classification ---
@app.route("/predict_delay", methods=["POST"])
def predict_delay():
    dep_delay = float(request.form["dep_delay"])
    congestion = float(request.form["congestion_index"])
    stress = float(request.form["operational_stress_index"])
    risk = float(request.form["disruption_risk_score"])
    X = np.array([[dep_delay, congestion, stress, risk]])
    prediction = rf.predict(X)[0]
    result = "High Disruption Risk" if prediction == 1 else "Low Disruption Risk"
    return render_template("index.html", result=result)

# --- Model 2: Forecasting ---
@app.route("/forecast")
def forecast():
    forecast_fig = go.Figure()
    forecast_fig.add_trace(go.Scatter(y=[10, 15, 8, 12, 20], mode="lines+markers", name="Forecast"))
    forecast_fig.update_layout(title="Sample Delay Forecast", template="plotly_dark")
    forecast_html = forecast_fig.to_html(full_html=False)
    return render_template("index.html", forecast=forecast_html)

# --- Model 3: Clustering ---
@app.route("/cluster", methods=["POST"])
def cluster():
    airport_health = float(request.form.get("airport_health_score", 50))
    congestion = float(request.form.get("congestion_index", 10))
    stress = float(request.form.get("operational_stress_index", 20))
    X = np.array([[airport_health, congestion, stress]])
    cluster_label = kmeans.predict(X)[0]
    labels = {0: "Stable", 1: "Congested", 2: "Risk"}
    cluster_result = f"Airport Cluster: {labels.get(cluster_label, 'Unknown')}"
    return render_template("index.html", cluster_result=cluster_result)

# --- Model 4: Anomaly Detection ---
@app.route("/detect_anomaly", methods=["POST"])
def detect_anomaly():
    dep_delay = float(request.form["dep_delay"])
    arr_delay = float(request.form["arr_delay"])
    congestion = float(request.form["congestion_index"])
    X = np.array([[arr_delay, dep_delay, congestion]])
    anomaly = iso.predict(X)[0]
    anomaly_result = "Normal" if anomaly == 1 else "Anomaly Detected"
    return render_template("index.html", anomaly_result=anomaly_result)

if __name__ == "__main__":
    app.run(debug=True)