from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    jobs = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    assert 'title' in jobs[0]
    assert 'salary' in jobs[0]
    assert 'type' in jobs[0]
