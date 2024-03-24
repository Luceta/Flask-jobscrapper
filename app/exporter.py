import csv
import os


def save_to_file(file_name, jobs):
    home_dir = os.path.expanduser("~")
    downloads_dir = os.path.join(home_dir, "Downloads")
    file_path = os.path.join(downloads_dir, f"{file_name}.csv")
    with open(f"{file_path}.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["title", "company", "location", "URL"])  # 헤더를 씁니다.
        for job in jobs:
            writer.writerow(
                [
                    job.get("title"),
                    job.get("company"),
                    job.get("location"),
                    job.get("job_link"),
                ]
            )
