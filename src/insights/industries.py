from typing import List, Dict
import csv


def get_unique_industries(path: str) -> List[str]:
    industry = []
    with open(path, "r") as file:
        DictReader_obj = csv.DictReader(file)
        for item in DictReader_obj:
            if item["industry"] not in industry and item["industry"] != "":
                industry.append(item["industry"])
        return industry


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [item for item in jobs if industry == item["industry"]]
