import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

""" Model 1: Disruption Risk Classification
             Target: delay > 30 minutes (binary classification).
             Algorithms: XGBoost, Random Forest.
             Deliverables: Classification report, ROC curve, feature importance chart."""
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, roc_auc_score, RocCurveDisplay
df=pd.read_csv("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/Feature & EDA/Engineered_Features.csv")

# Target variable
df["target_delay"] = (df["arr_delay"] > 30).astype(int)
X = df[["dep_delay","congestion_index","operational_stress_index","disruption_risk_score"]]
y = df["target_delay"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Random Forest
rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
print("Random Forest Report:\n", classification_report(y_test, y_pred_rf))

# ROC Curve
RocCurveDisplay.from_estimator(rf, X_test, y_test)
plt.title("Random Forest ROC Curve")
plt.show()

""" Model 2: Delay Forecasting
             Forecast: Hourly/Daily delays.
             Algorithms: Prophet, LightGBM.
             Deliverables: Forecast plots, trend/seasonality decomposition.""" 
from prophet import Prophet
# Prepare data for Prophet
df_prophet = df.groupby("fl_date")["arr_delay"].mean().reset_index()
df_prophet.rename(columns={"fl_date":"ds","arr_delay":"y"}, inplace=True)
model = Prophet()
model.fit(df_prophet)
future = model.make_future_dataframe(periods=30)  # forecast next 30 days
forecast = model.predict(future)
model.plot(forecast)
plt.title("Daily Delay Forecast (Prophet)")
plt.show()
model.plot_components(forecast)
plt.show()

""" Model 3: Airport Clustering
             Algorithms: KMeans.
             Outputs: Cluster labels → Stable / Congested / Risk Airports.
             Deliverables: Cluster visualization (scatterplot, cluster centers).""" 
from sklearn.cluster import KMeans
features = df.groupby("origin")[["airport_health_score","congestion_index","operational_stress_index"]].mean()
kmeans = KMeans(n_clusters=3, random_state=42)
features["cluster"] = kmeans.fit_predict(features)
sns.scatterplot(data=features, x="congestion_index", y="airport_health_score", hue="cluster", palette="Set2")
plt.title("Airport Clustering: Stable vs Congested vs Risk")
plt.show()

""" Model 4: Anomaly Detection
             Algorithms: Isolation Forest.
             Detect: Sudden delay spikes, operational anomalies.
             Deliverables: Anomaly flags, anomaly visualization.""" 

from sklearn.ensemble import IsolationForest
iso = IsolationForest(contamination=0.05, random_state=42)
df["anomaly_flag"] = iso.fit_predict(df[["arr_delay","dep_delay","congestion_index"]])
sns.scatterplot(data=df, x="dep_delay", y="arr_delay", hue="anomaly_flag", palette={1:"blue",-1:"red"}, alpha=0.6)
plt.title("Anomaly Detection: Delay Spikes & Operational Issues")
plt.show()

import joblib
joblib.dump(rf, "C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/ML/random_forest_model.pkl")
joblib.dump(model, "C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/ML/prophet_model.pkl")
joblib.dump(kmeans, "C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/ML/airport_clustering_model.pkl")
joblib.dump(iso, "C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/ML/isolation_forest_model.pkl")