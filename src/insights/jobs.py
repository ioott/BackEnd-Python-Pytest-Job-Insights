from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    jobs = []
    with open(path, "r") as file:
        all_jobs = csv.DictReader(file)
        for job in all_jobs:
            jobs.append(dict(job))
        return jobs


def get_unique_job_types(path: str) -> List[str]:
    jobs = []
    with open(path, "r") as file:
        all_jobs = csv.DictReader(file)
        for job in all_jobs:
            if job["job_type"] not in jobs:
                jobs.append(job["job_type"])
        return jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [job for job in jobs if job_type == job["job_type"]]
