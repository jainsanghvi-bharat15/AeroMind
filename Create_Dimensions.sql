CREATE TABLE Dim_Airline
(
    Airline_Key INT PRIMARY KEY,
    Carrier_Code VARCHAR(10)
);

CREATE TABLE Dim_Airport
(
    Airport_Key INT PRIMARY KEY,
    Airport_Code VARCHAR(10),
    City_Name VARCHAR(100),
    State_Name VARCHAR(100)
);

CREATE TABLE Dim_Date
(
    Date_Key INT PRIMARY KEY,
    Date DATE,
    Year INT,
    Quarter INT,
    Month INT,
    Month_Name VARCHAR(20),
    Day INT,
    Day_Name VARCHAR(20),
    Week_Number INT,
    Is_Weekend VARCHAR(5)
);

CREATE TABLE Dim_Time
(
    Time_Key INT PRIMARY KEY,
    Hour INT,
    Part_Of_Day VARCHAR(20)
);

CREATE TABLE Dim_Delay_Type
(
    Delay_Type_Key INT PRIMARY KEY,
    Delay_Type VARCHAR(50)
);