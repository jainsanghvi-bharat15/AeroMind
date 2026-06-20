-- Airline Delay Ranking
SELECT D.Carrier_Code, ROUND(AVG(F.Departure_Delay), 2) AS avg_delay FROM Fact_Flight_Operations_500K F
JOIN Dim_Airline D ON F.Airline_Key = D.Airline_Key
GROUP BY D.Carrier_Code ORDER BY avg_delay DESC;

-- Airline Cancellation Ranking
SELECT D.Carrier_Code, SUM(F.Cancelled) AS cancellations FROM Fact_Flight_Operations_500K F
JOIN Dim_Airline D ON F.Airline_Key = D.Airline_Key
GROUP BY D.Carrier_Code ORDER BY cancellations DESC;

-- Airline Diversion Ranking
SELECT D.Carrier_Code, SUM(F.Diverted) AS diversions FROM Fact_Flight_Operations_500K F
JOIN Dim_Airline D ON F.Airline_Key = D.Airline_Key
GROUP BY D.Carrier_Code ORDER BY diversions DESC;