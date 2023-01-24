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
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
