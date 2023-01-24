from typing import List, Dict
import csv


def get_unique_industries(path: str) -> List[str]:
    industry = []
    with open(path, "r") as file:
        DictReader_obj = csv.DictReader(file)
        for item in DictReader_obj:
            if item["industry"] not in industry and item["industry"] != "":
                industry.append(dict(item)["industry"])
        return industry


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
