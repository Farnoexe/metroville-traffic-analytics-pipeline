CREATE TABLE metroville_processed_traffic
WITH (
    format = 'PARQUET',
    external_location = 's3://metroville-traffic-analytics/processed/traffic/'
) AS
SELECT
    intersection_id,
    CAST(date_parse(timestamp, '%Y-%m-%d %H:%i:%s') AS timestamp) AS event_timestamp,
    direction,
    vehicle_count,
    city,
    hour(CAST(date_parse(timestamp, '%Y-%m-%d %H:%i:%s') AS timestamp)) AS hour_of_day,
    date_format(CAST(date_parse(timestamp, '%Y-%m-%d %H:%i:%s') AS timestamp), '%W') AS day_name,
    CASE
        WHEN day_of_week(CAST(date_parse(timestamp, '%Y-%m-%d %H:%i:%s') AS timestamp)) IN (6, 7) THEN true
        ELSE false
    END AS is_weekend
FROM metroville_raw_traffic;
