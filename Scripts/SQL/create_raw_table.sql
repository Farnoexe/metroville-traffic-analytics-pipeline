CREATE EXTERNAL TABLE metroville_raw_traffic (
    intersection_id STRING,
    timestamp STRING,
    direction STRING,
    vehicle_count INT,
    city STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    "separatorChar" = ",",
    "quoteChar" = "\""
)
LOCATION 's3://metroville-traffic-analytics/raw/traffic/'
TBLPROPERTIES ("skip.header.line.count"="1");
