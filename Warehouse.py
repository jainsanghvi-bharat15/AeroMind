import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/flight_data_2024_cleaned.csv")
# DIM_AIRLINE
dim_airline = (
    df[["op_unique_carrier"]]
    .drop_duplicates()
    .sort_values("op_unique_carrier")
    .reset_index(drop=True))

dim_airline.insert(0, "airline_key", range(1, len(dim_airline) + 1))
dim_airline.rename(columns={"op_unique_carrier": "Carrier_Code"},inplace=True)
dim_airline.to_csv("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/Warehouse_Tables/Dim_Airline.csv",index=False)
print(f"Dim_Airline Created : {len(dim_airline)} rows")

# ----------------------------------------------------------------------------------------------------------------------------------------------

""" DIM_AIRPORT
    Combining Origin and Destination Airports into one master airport table."""
origin_airports = df[
    [
        "origin",
        "origin_city_name",
        "origin_state_nm"
    ]
].rename(
    columns={
        "origin": "Airport_Code",
        "origin_city_name": "City_Name",
        "origin_state_nm": "State_Name"
    })

dest_airports = df[
    [
        "dest",
        "dest_city_name",
        "dest_state_nm"
    ]
].rename(
    columns={
        "dest": "Airport_Code",
        "dest_city_name": "City_Name",
        "dest_state_nm": "State_Name"
    }
)

dim_airport = pd.concat([origin_airports, dest_airports], ignore_index=True)
dim_airport = (
    dim_airport
    .drop_duplicates()
    .sort_values("Airport_Code")
    .reset_index(drop=True))

dim_airport.insert(0, "Airport_Key", range(1, len(dim_airport) + 1))
dim_airport.to_csv("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/Warehouse_Tables/Dim_Airport.csv",index=False)
print(f"Dim_Airport Created : {len(dim_airport)} rows")

# ----------------------------------------------------------------------------------------------------------------------------------------------
""" DIM_DATE
    One row per date. """
dim_date = pd.DataFrame()
dim_date["Date"] = pd.to_datetime(df["fl_date"]).drop_duplicates()
dim_date = (dim_date.sort_values("Date").reset_index(drop=True))

dim_date["Date_Key"] = (
    dim_date["Date"]
    .dt.strftime("%Y%m%d")
    .astype(int))

dim_date["Year"] = dim_date["Date"].dt.year
dim_date["Quarter"] = dim_date["Date"].dt.quarter
dim_date["Month"] = dim_date["Date"].dt.month

dim_date["Month_Name"] = (dim_date["Date"].dt.month_name())
dim_date["Day"] = dim_date["Date"].dt.day
dim_date["Day_Name"] = (dim_date["Date"].dt.day_name())
dim_date["Week_Number"] = (dim_date["Date"].dt.isocalendar().week)

dim_date["is_weekend"] = np.where(
    dim_date["Date"].dt.weekday >= 5,
    "Yes",
    "No")

dim_date = dim_date[
    [
        "Date_Key",
        "Date",
        "Year",
        "Quarter",
        "Month",
        "Month_Name",
        "Day",
        "Day_Name",
        "Week_Number",
        "is_weekend"
    ]]

dim_date.to_csv("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/Warehouse_Tables/Dim_Date.csv",index=False)
print(f"Dim_Date Created : {len(dim_date)} rows")

# ----------------------------------------------------------------------------------------------------------------------------------------------

""" DIM_TIME
    Hour-level dimension."""
dim_time = pd.DataFrame({"Hour": range(24)})
dim_time.insert(0, "Time_Key", range(1, 25))
dim_time["part_of_day"] = np.select(
    [
        dim_time["Hour"].between(5, 11),
        dim_time["Hour"].between(12, 16),
        dim_time["Hour"].between(17, 20),
        dim_time["Hour"].between(21, 23)
    ],
    [
        "Morning",
        "Afternoon",
        "Evening",
        "Night"
    ],
    default="Late Night")
dim_time.to_csv("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/Warehouse_Tables/Dim_Time.csv",index=False)
print(f"Dim_Time Created : {len(dim_time)} rows")

# ----------------------------------------------------------------------------------------------------------------------------------------------

""" DIM_DELAY_TYPEL
    FAA standard delay categories."""
dim_delay_type = pd.DataFrame(
    {
        "Delay_Type_Key": [1, 2, 3, 4, 5],

        "Delay_Type": [
            "Carrier Delay",
            "Weather Delay",
            "NAS Delay",
            "Security Delay",
            "Late Aircraft Delay"]
    })

dim_delay_type.to_csv("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/Warehouse_Tables/Dim_Delay_Type.csv", index=False)
print(f"Dim_Delay_Type Created : {len(dim_delay_type)} rows")