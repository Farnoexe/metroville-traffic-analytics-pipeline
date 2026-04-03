from pathlib import Path
from datetime import datetime, timedelta
import csv
import random


CITY = "Metroville"
INTERSECTIONS = [f"INT_{i:03d}" for i in range(1, 11)]
DIRECTIONS = ["N", "S", "E", "W"]

START_DATE = datetime(2026, 3, 1)
NUM_DAYS = 31


def base_traffic_for_hour(hour: int) -> int:
    if 0 <= hour <= 5:
        return 8
    if 6 <= hour <= 9:
        return 40
    if 10 <= hour <= 15:
        return 22
    if 16 <= hour <= 19:
        return 48
    if 20 <= hour <= 23:
        return 18
    return 15


def day_multiplier(date_value: datetime) -> float:
    if date_value.weekday() in (5, 6):
        return 0.7
    return 1.0


def generate_daily_file(output_dir: Path, current_date: datetime) -> None:
    file_name = f"traffic_{current_date.strftime('%Y_%m_%d')}.csv"
    output_file = output_dir / file_name

    with output_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["intersection_id", "timestamp", "direction", "vehicle_count", "city"])

        for intersection in INTERSECTIONS:
            intersection_bias = random.randint(-5, 5)

            for hour in range(24):
                timestamp = current_date.replace(hour=hour, minute=0, second=0)
                base_count = round(base_traffic_for_hour(hour) * day_multiplier(current_date))

                for direction in DIRECTIONS:
                    direction_bias = {
                        "N": 2,
                        "S": 0,
                        "E": 3,
                        "W": 1,
                    }[direction]

                    noise = random.randint(-4, 8)
                    vehicle_count = max(0, base_count + intersection_bias + direction_bias + noise)

                    writer.writerow([
                        intersection,
                        timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                        direction,
                        vehicle_count,
                        CITY,
                    ])


def main() -> None:
    random.seed(42)

    # Script is in repo root
    repo_root = Path(__file__).resolve().parent
    output_dir = repo_root / "data"
    output_dir.mkdir(parents=True, exist_ok=True)

    for day_offset in range(NUM_DAYS):
        current_date = START_DATE + timedelta(days=day_offset)
        generate_daily_file(output_dir, current_date)

    print(f"Done. Generated {NUM_DAYS} daily CSV files in: {output_dir}")


if __name__ == "__main__":
    main()
