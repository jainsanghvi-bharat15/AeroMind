-- Peak Flight Hours
SELECT T.Hour, COUNT(*) AS total_flights FROM Fact_Flight_Operations_500K F
JOIN Dim_Time T ON F.Time_Key = T.Time_Key
GROUP BY T.Hour ORDER BY total_flights DESC;

-- Peak Delay Hours
SELECT T.Hour, ROUND(AVG(F.Departure_Delay), 2) AS avg_delay FROM Fact_Flight_Operations_500K F
JOIN Dim_Time T ON F.Time_Key = T.Time_Key
GROUP BY T.Hour ORDER BY avg_delay DESC;

-- Monthly Delay Trend
SELECT D.Month_Name, ROUND(AVG(F.Departure_Delay), 2) AS avg_delay
FROM Fact_Flight_Operations_500K F JOIN Dim_Date D ON F.Date_Key = D.Date_Key
GROUP BY D.Month_Name ORDER BY MIN(D.Month);