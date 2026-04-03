SELECT
    intersection_id,
    SUM(vehicle_count) AS peak_hour_traffic
FROM metroville_processed_traffic
WHERE hour_of_day IN (6, 7, 8, 9, 16, 17, 18, 19)
GROUP BY intersection_id
ORDER BY peak_hour_traffic DESC
LIMIT 5;
