SELECT
    intersection_id,
    SUM(vehicle_count) AS total_traffic
FROM metroville_processed_traffic
GROUP BY intersection_id
ORDER BY total_traffic DESC
LIMIT 5;
