SELECT
    is_weekend,
    SUM(vehicle_count) AS total_traffic
FROM metroville_processed_traffic
GROUP BY is_weekend;
