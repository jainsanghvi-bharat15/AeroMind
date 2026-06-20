import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# LOAD DATASET
df = pd.read_csv("C:/Users/HP/3D Objects/Desktop/DA_using_Python/DA Projects/Project 3 (Airport)/flight_data_2024.csv")
df.head()

""" Dataset Overview
    Answers:
        How large is the dataset?
        Is it enterprise-scale?
        What are the data types?"""
print("Number of Rows :", df.shape[0])
print("Number of Columns :", df.shape[1])
df.info()   # COLUMN INFORMATION

# MEMORY USAGE
memory_usage = df.memory_usage(deep=True).sum() / 1024**2
print(("\nMemory Usage: ",memory_usage," MB"))

"""Data Quality Assessment
    Answers:
        Which columns have missing values?
        Is data cleaning required?"""
# MISSING VALUES
missing_values = pd.DataFrame({'Missing Count': df.isnull().sum(), 'Missing %': round((df.isnull().sum()/len(df))*100,2)})
missing_values = missing_values.sort_values(by='Missing %', ascending=False)
print(missing_values)

# DUPLICATE RECORDS
print("\nDuplicate Records :", df.duplicated().sum())

"""Statistical Summary
    Answers:
        Average delay
        Maximum delay
        Distance ranges
        Flight duration ranges"""


print(df.describe().T)  # NUMERICAL SUMMARY
print("Total Flights: ", len(df))   # TOTAL FLIGHTS

"""TOTAL AIRLINES
    Business Question: How many airlines are represented?"""
print("Total Airlines :", df["op_unique_carrier"].nunique())
print("\nAirlines:", sorted(df["op_unique_carrier"].unique()))

"""Number of Airports
    Business Question : How large is the airport network?"""
origin_airports = df["origin"].nunique()
dest_airports = df["dest"].nunique()
all_airports = pd.concat([df["origin"], df["dest"]]).nunique()  # UNIQUE AIRPORTS
print("Origin Airports :", origin_airports)
print("Destination Airports :", dest_airports)
print("Unique Airports :", all_airports)

"""Flight Route Analysis
    Business Question: Which routes carry the most traffic?"""
# CREATE ROUTE
df["route"] = df["origin"] + " → " + df["dest"]

# UNIQUE ROUTES
print("Unique Routes :", df["route"].nunique())

# TOP ROUTES
top_routes = df["route"].value_counts().head(10)
print("Top routes are: \n", top_routes)

"""Cancellation Analysis"""
print("Cancelled Flights :", df["cancelled"].sum()) # TOTAL CANCELLED FLIGHTS
print("Cancellation Rate : ", df["cancelled"].sum() / len(df) * 100)    # CANCELLATION RATE

"""Diversion Analysis""" 
print("Diverted Flights: ", df["diverted"].sum())

"""Delay Distribution"""
print("\nDEPARTURE DELAY: \n",df["dep_delay"].describe())
print("\nARRIVAL DELAY: \n", df["arr_delay"].describe())

""" Visualize Delay Distribution
    Business Question: Are delays normally distributed?"""
# DEPARTURE DELAY DISTRIBUTION
plt.figure(figsize=(10,5))
sns.histplot(df["dep_delay"], bins=50)
plt.title("Departure Delay Distribution")
plt.show()

"""Top Delay Causes
    Business Question: What causes most delays?
    This insight is extremely important later."""
# TOTAL DELAYS BY CATEGORY
delay_causes = pd.DataFrame({
    "Carrier Delay": [df["carrier_delay"].sum()],
    "Weather Delay": [df["weather_delay"].sum()],
    "NAS Delay": [df["nas_delay"].sum()],
    "Security Delay": [df["security_delay"].sum()],
    "Late Aircraft Delay": [df["late_aircraft_delay"].sum()]})
delay_causes = delay_causes.T
delay_causes.columns = ["Minutes"]
delay_causes = delay_causes.sort_values(by="Minutes", ascending=False)
print("\nCause of delay is: \n", delay_causes)

"""Top Airports by Delay
    Business Question
    Which airports are operationally unstable?"""
# AVERAGE DELAY BY ORIGIN AIRPORT
airport_delay = df.groupby("origin")["dep_delay"].mean().sort_values(ascending=False).head(10)
print("\nAirport Delay is: ", airport_delay)


"""Top Airlines by Delay"""
# AIRLINE DELAY ANALYSIS
airline_delay = df.groupby("op_unique_carrier")["dep_delay"].mean().sort_values(ascending=False)
print("\nAirline delay is: ", airline_delay)

"""16. Peak Congestion Hours
    Business Question: When does congestion occur?"""
# EXTRACT HOUR
df["scheduled_hour"] = (df["crs_dep_time"] // 100)

# FLIGHTS PER HOUR
hourly_traffic = df.groupby("scheduled_hour").size()
print(hourly_traffic)