import pandas as pd

# Load Files
df = pd.read_csv("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/flight_data_2024_cleaned.csv")
dim_airline = pd.read_csv("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/Warehouse_Tables/Dim_Airline.csv")
dim_airport = pd.read_csv("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/Warehouse_Tables/Dim_Airport.csv")
dim_date = pd.read_csv("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/Warehouse_Tables/Dim_Date.csv")
dim_time = pd.read_csv("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/Warehouse_Tables/Dim_Time.csv")

# DATE DIMENSION JOIN
df["fl_date"] = pd.to_datetime(df["fl_date"])
dim_date["Date"] = pd.to_datetime(dim_date["Date"])

df = df.merge(
    dim_date[["Date_Key", "Date"]],
    left_on="fl_date",
    right_on="Date",
    how="left")

# TIME DIMENSION JOIN
df["scheduled_hour"] = df["crs_dep_time"] // 100
time_lookup = dim_time.rename(columns={"Hour": "scheduled_hour"})
df = df.merge(
    time_lookup,
    on="scheduled_hour",
    how="left")

# AIRLINE DIMENSION JOIN
df = df.merge(
    dim_airline,
    left_on="op_unique_carrier",
    right_on="Carrier_Code",
    how="left")

# ORIGIN AIRPORT JOIN
origin_lookup = dim_airport[["Airport_Key", "Airport_Code"]].rename(columns={"Airport_Key": "Origin_Airport_Key"})
df = df.merge(
    origin_lookup,
    left_on="origin",
    right_on="Airport_Code",
    how="left")
df.drop(columns=["Airport_Code"], inplace=True)

# DESTINATION AIRPORT JOIN
destination_lookup = dim_airport[["Airport_Key", "Airport_Code"]].rename(columns={"Airport_Key": "Destination_Airport_Key"})
df = df.merge(
    destination_lookup,
    left_on="dest",
    right_on="Airport_Code",
    how="left")
df.drop(columns=["Airport_Code"], inplace=True)

# FACT TABLE
fact_flight_operations = pd.DataFrame()
fact_flight_operations["Flight_Key"] = range(1, len(df) + 1)
fact_flight_operations["Date_Key"] = df["Date_Key"]
fact_flight_operations["Airline_Key"] = df["airline_key"]
fact_flight_operations["Origin_Airport_Key"] = (df["Origin_Airport_Key"])
fact_flight_operations["Destination_Airport_Key"] = (df["Destination_Airport_Key"])
fact_flight_operations["Time_Key"] = (df["Time_Key"])
fact_flight_operations["Departure_Delay"] = (df["dep_delay"])
fact_flight_operations["Arrival_Delay"] = (df["arr_delay"])
fact_flight_operations["Cancelled"] = (df["cancelled"])
fact_flight_operations["Diverted"] = (df["diverted"])
fact_flight_operations["Distance"] = (df["distance"])
fact_flight_operations["Air_Time"] = (df["air_time"])
fact_flight_operations["Actual_Elapsed_Time"] = (df["actual_elapsed_time"])

# SAVE FACT TABLE
fact_flight_operations.to_csv("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/Warehouse_Tables/Fact_Flight_Operations.csv",index=False)
print("Fact Table Shape:", fact_flight_operations.shape)
print("Fact Table Created Successfully")
df = pd.read_csv("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/Warehouse_Tables/Fact_Flight_Operations.csv")
sample = df.sample(n=500000,random_state=42)
sample.to_csv("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/Warehouse_Tables/Fact_Flight_Operations_500K.csv",index=False)
print(sample.shape)