SELECT
    hour_of_day,
    AVG(vehicle_count) AS avg_traffic
FROM metroville_processed_traffic
GROUP BY hour_of_day
ORDER BY avg_traffic DESC;
