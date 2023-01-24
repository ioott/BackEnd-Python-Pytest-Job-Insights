from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    jobs = []
    with open(path, "r") as file:
        DictReader_obj = csv.DictReader(file)
        for item in DictReader_obj:
            jobs.append(dict(item))
        return jobs


def get_unique_job_types(path: str) -> List[str]:
    jobs = []
    with open(path, "r") as file:
        DictReader_obj = csv.DictReader(file)
        for item in DictReader_obj:
            if item["job_type"] not in jobs:
                jobs.append(item["job_type"])
        return jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [
        item
        for item in jobs
        if job_type == item["job_type"]
    ]
    # filtered_jobs = []
    # for item in jobs:
    #     if job_type == item["job_type"]:
    #         filtered_jobs.append(item)
    # return filtered_jobs
