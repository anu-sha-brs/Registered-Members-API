"""The tests to run for this api.
To run the tests type,
$ nosetests --verbose
"""
from nose.tools import assert_true
import requests

BASE_URL = "http://localhost:5000" 


def test_get_all_members():
    "Test getting all registered members"
    response = requests.get('%s/registered-members' % (BASE_URL))
    assert_true(response.ok)


def test_get_single_member():
    "Test getting a single member"
    response = requests.get('%s/registered-members/5' % (BASE_URL))
    assert_true(response.ok)


def test_get_single_member_404():
    "Test getting a non existent member"
    response = requests.get('%s/registered-members/22' % (BASE_URL))
    assert_true(response.status_code == 404)


def test_get_statistical_information():
    "Test getting statistical information of all registered members"
    response = requests.get('%s/statistical-information' % (BASE_URL))
    assert_true(response.ok)