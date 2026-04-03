from pathlib import Path
import boto3


BUCKET_NAME = "metroville-traffic-analytics"
S3_PREFIX = "raw/traffic"


def main() -> None:
    # Script is in repo root
    repo_root = Path(__file__).resolve().parent
    local_folder = repo_root / "data"

    if not local_folder.exists():
        raise FileNotFoundError(f"Local folder not found: {local_folder}")

    csv_files = sorted(local_folder.glob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in: {local_folder}")

    s3 = boto3.client("s3")

    for file_path in csv_files:
        s3_key = f"{S3_PREFIX}/{file_path.name}"
        print(f"Uploading {file_path.name} → s3://{BUCKET_NAME}/{s3_key}")
        s3.upload_file(str(file_path), BUCKET_NAME, s3_key)

    print("Upload complete.")


if __name__ == "__main__":
    main()
