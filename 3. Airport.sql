-- Top 10 Delayed Airports
SELECT A.Airport_Code, ROUND(AVG(F.Departure_Delay), 2) AS avg_delay FROM Fact_Flight_Operations_500K F
JOIN Dim_Airport A ON F.Origin_Airport_Key = A.Airport_Key
GROUP BY A.Airport_Code ORDER BY avg_delay DESC LIMIT 10;

-- Top 10 Airports by Flight Volume
SELECT A.Airport_Code, COUNT(*) AS total_flights FROM Fact_Flight_Operations_500K F
JOIN Dim_Airport A ON F.Origin_Airport_Key = A.Airport_Key
GROUP BY A.Airport_Code ORDER BY total_flights DESC LIMIT 10;

-- Airport Cancellation Ranking
SELECT A.Airport_Code, SUM(F.Cancelled) AS cancellations FROM Fact_Flight_Operations_500K F
JOIN Dim_Airport A ON F.Origin_Airport_Key = A.Airport_Key
GROUP BY A.Airport_Code ORDER BY cancellations DESC;