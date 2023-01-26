from typing import Union, List, Dict
import csv


def get_max_salary(path: str) -> int:
    salary = 0
    with open(path, "r") as file:
        all_jobs = csv.DictReader(file)
        for job in all_jobs:
            if job["max_salary"].isnumeric():
                if int(job["max_salary"]) > salary:
                    salary = int(job["max_salary"])
        return salary


def get_min_salary(path: str) -> int:
    salary = get_max_salary(path)
    with open(path, "r") as file:
        all_jobs = csv.DictReader(file)
        for job in all_jobs:
            if job["min_salary"].isnumeric():
                if int(job["min_salary"]) < salary:
                    salary = int(job["min_salary"])
        return salary


def verify_min_salary(job: Dict) -> int:
    if type(job["min_salary"]) == int:
        min_salary = job["min_salary"]
        return min_salary
    elif type(job["min_salary"]) == str and job["min_salary"].isnumeric():
        min_salary = int(job["min_salary"])
        return min_salary
    else:
        raise ValueError("formato inválido")


def verify_max_salary(job: Dict) -> int:
    if type(job["max_salary"]) == int:
        max_salary = job["max_salary"]
        return max_salary

    elif type(job["max_salary"]) == str and job["max_salary"].isnumeric():
        max_salary = int(job["max_salary"])
        return max_salary
    else:
        raise ValueError("formato inválido")


def verify_actual_salary(salary: Union[int, str]) -> int:
    if type(salary) == int:
        actual_salary = salary
        return actual_salary
    elif type(salary) == str and salary.isnumeric():
        actual_salary = int(salary)
        return actual_salary
    else:
        raise ValueError("formato inválido")


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("faltam informações")

    try:
        min_salary = verify_min_salary(job)
        max_salary = verify_max_salary(job)
        actual_salary = verify_actual_salary(salary)

    except ValueError:
        raise ValueError("formato inválido")

    if min_salary > max_salary:
        raise ValueError("informações incorretas")

    return min_salary <= actual_salary and max_salary >= actual_salary


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:

    filtered_salaries = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_salaries.append(job)

        except ValueError:
            pass

    return filtered_salaries
