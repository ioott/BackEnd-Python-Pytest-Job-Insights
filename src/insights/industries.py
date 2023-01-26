from typing import List, Dict
import csv


def get_unique_industries(path: str) -> List[str]:
    industry = []
    with open(path, "r") as file:
        all_jobs = csv.DictReader(file)
        for job in all_jobs:
            if job["industry"] not in industry and job["industry"] != "":
                industry.append(job["industry"])
        return industry


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [job for job in jobs if industry == job["industry"]]
