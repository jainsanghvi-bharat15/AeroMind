-- Total Flights
SELECT COUNT(*) AS total_flights FROM Fact_Flight_Operations_500K;

-- Average Departure Delay
SELECT ROUND(AVG(Departure_Delay),2) AS avg_departure_delay FROM Fact_Flight_Operations_500K;

-- Delay Rate
SELECT ROUND( 100.0 * SUM(CASE
								WHEN Departure_Delay > 15
								THEN 1
								ELSE 0
								END)/COUNT(*),2 ) AS delay_rate from Fact_Flight_Operations_500K;
-- Cancellation Rate
SELECT ROUND( 100.0 * SUM(Cancelled)/COUNT(*), 2) AS cancellation_rate FROM Fact_Flight_Operations_500K;