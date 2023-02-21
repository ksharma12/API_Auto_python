import time
from json import dumps
from uuid import uuid4

import jsonschema
import json
import requests
from assertpy.assertpy import assert_that
from pprint import pprint

base_url = "http://0.0.0.0:5000//api/people"


def pritty_print(msg, indent=2):
    print()
    pprint(msg, indent=indent)


def get_all_users():
    response = requests.get(base_url)
    people_json = response.json()
    return people_json, response


def create_new_unique_user():
    unique_last_name = f'User {str(uuid4())}'
    # it does serialization and convert python dict to json
    payload = dumps({
        'fname': 'New',
        'lname': unique_last_name
    })
    payload1 = {
        'fname': 'New',
        'lname': unique_last_name
    }
    header = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.post(base_url, data=payload, headers=header)
    assert_that(response.status_code).is_equal_to(204)
    return unique_last_name


def test_read_all_has_Kent():
    people_json, response = get_all_users()
    people_text = response.text
    pritty_print(people_json)
    assert_that(response.status_code).is_equal_to(200)
    first_names = [people["fname"] for people in people_json]
    assert first_names.__contains__("Kent")


def test_new_person_can_be_added():
    unique_last_name = create_new_unique_user()
    people_json = requests.get(base_url).json()
    # way 1 to check
    new_users = [person["lname"] for person in people_json if person["lname"] == unique_last_name]
    assert_that(new_users).is_not_empty()
    # way 2 to check
    is_new_user_created = filter(lambda person: person["lname"] == unique_last_name, people_json)
    assert_that(is_new_user_created).is_true()


# def test_person_can_be_deleted():
#     unique_last_name = create_new_unique_user()
#     all_users, _ = get_all_users()
#     new_user_created = [person for person in all_users if person["lname"] == unique_last_name][0]
#     person_to_be_deleted = new_user_created["person_id"]
#
#     url = f'{base_url}/{person_to_be_deleted}'
#     response = requests.delete(url)
#     assert_that(response.status_code).is_equal_to(200)
#     assert_that(response.status_code).is_equal_to(requests.codes.ok)

def test_requires_create_users():
    url = "https://reqres.in/api/users"
    payload = {
        "name": "Kim_kardashian",
        "job": "Model"
    }
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post(url=url, data=payload)
    pritty_print(response.status_code)
    pritty_print(response.json())

    # Create a validator for the JSON schema
    validator = jsonschema.Draft7Validator(response.json())

    # Get the schema of the JSON object
    schema = validator.schema

    # Print the schema
    print(json.dumps(schema, indent=2))

    # Validate the data against the schema
    try:
        jsonschema.validate(response.json(), schema)
        print("Data is valid!")
    except jsonschema.exceptions.ValidationError as e:
        print("Data is invalid:")
        print(e.message)


