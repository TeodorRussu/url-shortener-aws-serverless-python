import pytest

from functions.create import validate_url


# def test_valid_url():
#     valid_url = 'https://www.example.com/path/to/file?query=string'
#     assert validate_url(valid_url) == True
#
#
# @pytest.mark.parametrize(
#     "invalid_url",
#     [
#         "htp://www.google.com",
#         "https://www.google com",
#         "https:/www.google.com",
#         "https://www.google..com",
#         "https://www.google.c",
#         "https.acmilan.com"
#     ]
# )
# def test_invalid_url(invalid_url):
#     assert not validate_url(invalid_url)
