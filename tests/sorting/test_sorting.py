from src.pre_built.sorting import sort_by
import pytest


@pytest.fixture
def test_sort_by_criteria():
    jobs = [
        {"min_salary": 1300, "max_salary": 2300, "date_posted": "2023-01-02"},
        {"min_salary": 1500, "max_salary": 2500, "date_posted": "2022-10-18"},
        {"min_salary": 1800, "max_salary": 2800, "date_posted": "2023-01-01"},
    ]

    expect = [
        [jobs[0], jobs[1], jobs[2]],
        [jobs[2], jobs[1], jobs[0]],
        [jobs[0], jobs[2], jobs[1]],
    ]

    sort_by(jobs, "min_salary")
    assert jobs == expect[0]

    sort_by(jobs, "max_salary")
    assert jobs == expect[1]

    sort_by(jobs, "date_posted")
    assert jobs == expect[2]
