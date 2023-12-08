import pytest
import requests
import random


# Example with single parameter
@pytest.mark.parametrize('param', [1, 2, 3, 4])
def test_list(param):
    assert param % 2 == 0


@pytest.mark.parametrize('param', '1234')
def test_string(param):
    assert param % 2 == 0
    # assert int(param) % 2 == 0


BANKS = {
    'bank_code1': 'Bank1',
    'bank_code2': 'Bank2',
}


@pytest.mark.parametrize('bank_code', BANKS.keys())
def test_dict_key(bank_code):
    assert BANKS[bank_code] == 'Bank1'


@pytest.mark.parametrize('bank_name', BANKS.values())
def test_dict_value(bank_name):
    assert BANKS['bank_code1'] == bank_name


@pytest.mark.parametrize('bank_smth', BANKS)  # what is bank_smth?
def test_dict(bank_smth):
    assert bank_smth == '?'


# Example with several parameters
@pytest.mark.parametrize("param1, param2", [
    (1, 2),
    (3, 4),
    (5, 6),
    (7, 8)
])
def test_params(param1, param2):
    assert (param1 + param2) % 3 == 0


# Example with nested parametrization
@pytest.mark.parametrize("param2", [1, 2, 3, 4, 5])
@pytest.mark.parametrize("param1", [6, 7, 8, 9, 0])
def test_params_nested(param1, param2):
    assert (param1 + param2) % 2 == 0


# Example with params ids
# Param filtering users posts by id
# https://jsonplaceholder.typicode.com/posts?userId=1
@pytest.fixture
def base_url():
    return 'https://jsonplaceholder.typicode.com'

@pytest.mark.parametrize(
    'userId', [-1, 0, 'a', 11, 9],
    ids=["negative", "zero", "letter", "out_of_range", "valid_value"]
)
def test_with_ids(base_url, userId):
    assert requests.get(base_url + "/posts", params={'userId': userId}).json() == []


@pytest.mark.parametrize("test_input, expected", [
    pytest.param("3+5", 8, id="example_name"),
    ("2+4", 6),
    pytest.param("6*9", 42, marks=pytest.mark.skip(reason="JIRA-12312"))
])
def test_param_skip(test_input, expected):
    if expected == 8:
        pytest.skip('BUG-345')
    assert eval(test_input) == expected


@pytest.fixture(params=[1, 2, 3])
def fixture_param(request):
    return request.param


@pytest.mark.parametrize('param', [10, 20, 30])
def test_parametrized_fixture(fixture_param, param):
    assert fixture_param + param == 11


@pytest.mark.parametrize('param', [
    random.randint(0, 100)
])
def test_random(param):
    assert param % 2 == 0
