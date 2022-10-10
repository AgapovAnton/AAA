from what_is_year_now import what_is_year_now
from unittest.mock import patch


def test_what_is_year_now():
    with patch("what_is_year_now.what_is_year_now") as mocked_year_cases:
        mocked_year_cases.return_value.json = lambda: (2022)
        assert what_is_year_now() == 2022
