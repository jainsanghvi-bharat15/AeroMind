import pandas as pd
import numpy as np

# Loading dataset, low_memory=False prevents mixed datatype warnings when reading a very large CSV. 
df = pd.read_csv("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/flight_data_2024.csv", low_memory=False)

# Create a working copy keep raw data untouched and perform all transformations on a separate dataframe. 
df_clean = df.copy()

""" Convert flight date to datetime format.
    This enables time-based analysis such as:
        - Monthly trends
        - Weekly trends
        - Time intelligence in Power BI"""
df_clean["fl_date"] = pd.to_datetime(df_clean["fl_date"], errors="coerce")

#Remove duplicate records.
df_clean.drop_duplicates(inplace=True)

""" Remove records where critical identifiers are missing.
    A flight without carrier, origin or destination cannot be used for analytics."""
df_clean = df_clean.dropna(
    subset=[
        "op_unique_carrier",
        "origin",
        "dest" ])

""" Create date-based features.
    These will be useful for:
        - Forecasting
        - Power BI filtering
        - Seasonality analysis """
df_clean["year"] = df_clean["fl_date"].dt.year
df_clean["month"] = df_clean["fl_date"].dt.month
df_clean["day"] = df_clean["fl_date"].dt.day

""" Create cancellation flag.
    For dashboards and ML models."""
df_clean["is_cancelled"] = np.where(df_clean["cancelled"] == 1,"Yes","No")

""" Create diversion flag.
    Useful for disruption monitoring."""
df_clean["is_diverted"] = np.where(df_clean["diverted"] == 1,"Yes","No")

""" Missing values in cancellation_code are expected because most flights are not cancelled.
    Replace missing values with 'Not Cancelled' for reporting purposes."""
df_clean["cancellation_code"] = (df_clean["cancellation_code"].fillna("Not Cancelled"))

""" Delay columns contain missing values mainly because flights were cancelled.
    Not filling with averages because that would distort operational metrics.
    Instead replace missing values with 0 for reporting datasets. """
delay_columns = [
    "carrier_delay",
    "weather_delay",
    "nas_delay",
    "security_delay",
    "late_aircraft_delay"]
for col in delay_columns:
    df_clean[col] = df_clean[col].fillna(0)

""" Create departure status.
    Business-friendly classification for airport operations teams. """
df_clean["departure_status"] = np.select(
    [
        df_clean["dep_delay"] <= 0,
        df_clean["dep_delay"] <= 15,
        df_clean["dep_delay"] <= 60,
        df_clean["dep_delay"] > 60
    ],
    [
        "On Time / Early",
        "Minor Delay",
        "Moderate Delay",
        "Severe Delay"
    ],
    default="Unknown")

""" Create arrival status.
    Used for airport health dashboards. """
df_clean["arrival_status"] = np.select(
    [
        df_clean["arr_delay"] <= 0,
        df_clean["arr_delay"] <= 15,
        df_clean["arr_delay"] <= 60,
        df_clean["arr_delay"] > 60
    ],
    [
        "On Time / Early",
        "Minor Delay",
        "Moderate Delay",
        "Severe Delay"
    ],
    default="Unknown")

""" Create route feature.
    Many airport analytics are performed at route level rather than airport level."""
df_clean["route"] = (df_clean["origin"]+ " → " + df_clean["dest"])

"""Extract scheduled departure hour.
    Important for:
        - Congestion analysis
        - Peak-hour analysis
        - Forecasting"""
df_clean["scheduled_hour"] = (df_clean["crs_dep_time"] // 100)

""" Identify flights affected by any delay(For classification models). """
df_clean["delayed_flight"] = np.where(df_clean["dep_delay"] > 15, 1, 0)

""" Create total attributed delay.
    Represents total operational delay explained by known delay categories."""

df_clean["total_delay_causes"] = (
    df_clean["carrier_delay"]
    + df_clean["weather_delay"]
    + df_clean["nas_delay"]
    + df_clean["security_delay"]
    + df_clean["late_aircraft_delay"])

""" Detecting extreme outliers.
    In aviation, extreme delays are often the most valuable disruption events.
    Instead creating a flag. """

df_clean["extreme_delay_flag"] = np.where(df_clean["dep_delay"] > 180,1,0)

""" Create airport traffic indicator(Useful later when calculating airport congestion metrics)."""
airport_traffic = (
    df_clean.groupby("origin")
    .size()
    .reset_index(name="airport_flights"))

df_clean = df_clean.merge(airport_traffic, on="origin", how="left")

""" Final validation checks. """
print("Rows:", len(df_clean))
print("Columns:", len(df_clean.columns))
print("\nRemaining Missing Values:")
print(df_clean.isnull().sum().sort_values(ascending=False).head(15))

""" Saving cleaned dataset.
    This dataset will be used for:
        - SQL
        - Power BI
        - Machine Learning
        - AI Insights"""
df_clean.to_csv("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/flight_data_2024_cleaned.csv",index=False)
print("\nCleaned dataset exported successfully.")