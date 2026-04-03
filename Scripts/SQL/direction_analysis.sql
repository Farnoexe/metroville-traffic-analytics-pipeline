SELECT
    direction,
    SUM(vehicle_count) AS total_traffic
FROM metroville_processed_traffic
GROUP BY direction
ORDER BY total_traffic DESC;
