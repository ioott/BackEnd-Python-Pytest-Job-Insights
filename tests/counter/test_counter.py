from src.pre_built.counter import count_ocurrences

TOTAL_PYTHON = 1639
TOTAL_JAVASCRIPT = 122


def test_counter():
    result_python = count_ocurrences("data/jobs.csv", "python")
    assert result_python == TOTAL_PYTHON

    result_Python = count_ocurrences("data/jobs.csv", "Python")
    assert result_Python == TOTAL_PYTHON

    result_javascript = count_ocurrences("data/jobs.csv", "javascript")
    assert result_javascript == TOTAL_JAVASCRIPT

    result_Javascript = count_ocurrences("data/jobs.csv", "javascript")
    assert result_Javascript == TOTAL_JAVASCRIPT
