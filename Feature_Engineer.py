import pandas as pd
df = pd.read_csv("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/flight_data_2024_cleaned.csv")

# --- CLEANING BOOLEAN COLUMNS ---
# Ensure binary flags are numeric (0/1)
for col in ["is_cancelled", "is_diverted", "extreme_delay_flag"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")  # Convert to numbers
    df[col] = df[col].fillna(0).astype(int)            # Replace NaN with 0, cast to int

# --- FEATURE ENGINEERING ---
def compute_airport_health(df):
    airport_stats = df.groupby("origin").agg({
        "dep_delay": "mean",
        "arr_delay": "mean",
        "is_cancelled": "mean",
        "is_diverted": "mean"
    }).reset_index()

    # Normalize values
    for col in ["dep_delay", "arr_delay", "is_cancelled", "is_diverted"]:
        airport_stats[col] = (airport_stats[col] - airport_stats[col].min()) / (airport_stats[col].max() - airport_stats[col].min())
    airport_stats["airport_health_score"] = 100 * (1 - airport_stats[["dep_delay","arr_delay","is_cancelled","is_diverted"]].mean(axis=1))
    return airport_stats[["origin","airport_health_score"]]

# Disruption Risk Score
df["disruption_risk_score"] = (
    100 * (
        0.4*df["is_cancelled"] +
        0.3*df["is_diverted"] +
        0.3*df["extreme_delay_flag"]))

# Congestion Index
df["congestion_index"] = df["airport_flights"] / (1 + df["dep_delay"].clip(lower=0))

# Operational Stress Index
df["operational_stress_index"] = (
    0.5*df["dep_delay"].clip(lower=0) +
    0.3*df["congestion_index"] +
    0.2*df["is_cancelled"])

# Delay Propagation Index
df["delay_propagation_index"] = df["arr_delay"].clip(lower=0) / (1 + df["dep_delay"].clip(lower=0))

# On-time flag
df["on_time_flag"] = (df["arr_delay"] <= 15).astype(int)

# Route reliability
route_stats = df.groupby("route")["on_time_flag"].mean().reset_index()
route_stats.rename(columns={"on_time_flag":"route_reliability_score"}, inplace=True)

# Merge airport health
airport_health = compute_airport_health(df)
df = df.merge(airport_health, on="origin", how="left")

df.to_csv("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/Engineered_Features.csv", index=False)
print("File saved successfully.")