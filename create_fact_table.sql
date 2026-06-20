CREATE TABLE Fact_Flight_Operations
(
    Flight_Key BIGINT PRIMARY KEY,
    Date_Key INT,
    Airline_Key INT,
    Origin_Airport_Key INT,
    Destination_Airport_Key INT,
    Time_Key INT,
    Departure_Delay FLOAT,
    Arrival_Delay FLOAT,
    Cancelled INT,
    Diverted INT,
    Distance FLOAT,
    Air_Time FLOAT,
    Actual_Elapsed_Time FLOAT,

    FOREIGN KEY(Date_Key) REFERENCES Dim_Date(Date_Key),
    FOREIGN KEY(Airline_Key) REFERENCES Dim_Airline(Airline_Key),
    FOREIGN KEY(Origin_Airport_Key) REFERENCES Dim_Airport(Airport_Key),
    FOREIGN KEY(Destination_Airport_Key) REFERENCES Dim_Airport(Airport_Key),
    FOREIGN KEY(Time_Key) REFERENCES Dim_Time(Time_Key)
);