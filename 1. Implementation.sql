CREATE DATABASE aeromind;
USE aeromind;
SELECT COUNT(*) FROM Dim_Airline;
SELECT COUNT(*) FROM Dim_Airport;
SELECT COUNT(*) FROM Dim_Date;
SELECT COUNT(*) FROM Dim_Time;
SELECT COUNT(*) FROM Fact_Flight_Operations_500k;

ALTER TABLE Dim_Airline ADD PRIMARY KEY (airline_key);
ALTER TABLE Dim_Airport ADD PRIMARY KEY (Airport_Key);
ALTER TABLE Dim_Date ADD PRIMARY KEY (Date_Key);
ALTER TABLE Dim_Time ADD PRIMARY KEY (Time_Key);
ALTER TABLE Dim_Delay_Type ADD PRIMARY KEY (Delay_Type_Key);
ALTER TABLE Fact_Flight_Operations_500K ADD PRIMARY KEY (Flight_Key);