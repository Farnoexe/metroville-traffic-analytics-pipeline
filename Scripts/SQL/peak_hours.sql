SELECT
    hour_of_day,
    SUM(vehicle_count) AS total_traffic
FROM metroville_processed_traffic
GROUP BY hour_of_day
ORDER BY total_traffic DESC
LIMIT 5;
