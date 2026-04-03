-- Check for nulls
SELECT COUNT(*) AS null_vehicle_count
FROM metroville_processed_traffic
WHERE vehicle_count IS NULL;

-- Check for negative values
SELECT COUNT(*) AS negative_vehicle_count
FROM metroville_processed_traffic
WHERE vehicle_count < 0;

-- Check total row count
SELECT COUNT(*) AS total_rows
FROM metroville_processed_traffic;

-- Check for unexpected directions
SELECT DISTINCT direction
FROM metroville_processed_traffic;
