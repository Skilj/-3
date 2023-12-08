import json

import jsonschema
import requests
from assertpy import assert_that
from requests import codes

from api.base_request import BaseRequest
from api.logger import logger
from api.rest_settings import BASE_URL_PETSTORE
from data.user import get_random_user_json, User


class UserRequest(BaseRequest):
    def __init__(self, path):
        self.path = f'{BASE_URL_PETSTORE}{path}'

    # def _request(self, url, request_type, data=None, expected_error=False):
    #     stop_flag = False
    #     while not stop_flag:
    #         response = self._make_request(data, request_type, url)
    #
    #         if not expected_error and response.status_code == codes.ok:
    #             stop_flag = True
    #
    #         elif expected_error:
    #             stop_flag = True
    #
    #     return response
    #
    # def _make_request(self, data, request_type, url):
    #     if request_type == 'GET':
    #         response = requests.get(url)
    #     elif request_type == 'POST':
    #         response = requests.post(url, data=data, headers=headers)
    #     elif request_type == 'PUT':
    #         response = requests.put(url, data=data, headers=headers)
    #     else:
    #         response = requests.delete(url, headers=headers)
    #     return response
    #
    # def get(self, path_variable, expected_error=False):
    #     get_url = f'{self.path}/{path_variable}'
    #     response = self._request(get_url, 'GET', expected_error=expected_error)
    #     request = response.request
    #     get_logs(request, response)
    #     return response
    #
    # def post(self, data):
    #     post_url = f'{self.path}'
    #     response = self._request(post_url, 'POST', data=data)
    #     request = response.request
    #     get_logs(request, response, data)
    #     return response
    #
    # def put(self, path_variable, data, expected_error=False):
    #     put_url = f'{self.path}/{path_variable}'
    #     response = self._request(put_url, 'PUT', data=data, expected_error=expected_error)
    #     request = response.request
    #     get_logs(request, response, data)
    #     return response
    #
    # def delete(self, path_varibale, expected_error=False):
    #     delete_url = f'{self.path}/{path_varibale}'
    #     response = self._request(delete_url, 'DELETE', expected_error=expected_error)
    #     request = response.request
    #     get_logs(request, response)
    #     return response


def should_create_user():
    logger.info(100*"=")
    logger.info("Start test should_create_user()")
    logger.info(100*"-")

    user = get_random_user_json("../files/users.csv")
    user_request = UserRequest(path="/user")
    logger.info("- Step 1: Create user:", user=user)
    response = user_request.post(user)


    assert_that(response.status_code).is_equal_to(codes.ok)
    assert_that(response.json()["code"]).is_equal_to(codes.ok)
    assert_that(response.json()["type"]).is_equal_to("unknown")
    assert_that(response.json()["message"]).is_not_empty()

    expected_user = User(
        json.loads(user).get("username"),
        json.loads(user).get("email"),
        json.loads(user).get("password"),
    )

    logger.info("- Step 2: Check that can get created user: ", username=json.loads(user).get("username"))
    response_created_user = user_request.get(json.loads(user).get("username"))

    expected_schema = {
        "properties": {
            "id": {"type": "number"},
            "username": {"type": "string"},
            "email": {"type": "string"},
            "password": {"type": "string"},
            "userStatus": {"type": "number"}
        }
    }

    jsonschema.validate(json.dumps(response_created_user.json()), expected_schema)
    assert_that(response_created_user.json()["username"]).is_equal_to(expected_user.username)
    assert_that(response_created_user.json()["email"]).is_equal_to(expected_user.email)
    assert_that(response_created_user.json()["password"]).is_equal_to(expected_user.password)


def should_get_error_when_not_found_user():
    logger.info(100*"=")
    logger.info("Start test should_get_error_when_not_found_user()")
    logger.info(100*"-")

    user_request = UserRequest(path="/user")
    logger.info("- Check that cannot get non exist user:", username="Jason")
    response = user_request.get("Jason", True)

    assert_that(response.status_code).is_equal_to(requests.codes.not_found)
    assert_that(response.json()).is_instance_of(dict)
    assert_that(response.json()).contains_key("code").contains_key("type").contains_key("message")
    assert_that(response.json()["code"]).is_equal_to(1)
    assert_that(response.json()["type"]).is_equal_to("error")
    assert_that(response.json()["message"]).is_equal_to("User not found")


def should_delete_user():
    logger.info(100*"=")
    logger.info("Start test should_delete_user()")
    logger.info(100*"-")
    user = get_random_user_json("../files/users.csv")
    username = json.loads(user).get("username")

    user_request = UserRequest(path="/user")
    logger.info("- Step 1: Create user:", user=user)
    user_request.post(user)
    logger.info("- Step 2: Delete user: ", username=username)
    response = user_request.delete(username)

    assert_that(response.status_code).is_equal_to(codes.ok)
    assert_that(response.json()["code"]).is_equal_to(codes.ok)
    assert_that(response.json()["type"]).is_equal_to("unknown")
    assert_that(response.json()["message"]).is_equal_to(username)

    # Bug
    logger.info("- Step 3: Check that user not found: ", username=username)
    response = user_request.delete(username)
    try:
        assert_that(response.status_code).is_equal_to(codes.not_found)
    except AssertionError as e:
        logger.error("- Bug: ", e=e)


def should_update_user():
    logger.info(100*"=")
    logger.info("Start test should_update_user()")
    logger.info(100*"-")
    user = get_random_user_json("../files/users.csv")
    new_user = json.dumps(User("Ilon", "blockhain@cc.com", "password").to_dict())

    user_request = UserRequest(path="/user")
    logger.info("- Step 1: Create user")
    user_request.post(user)
    logger.info("- Step 2: Update user: ", new_user=new_user)
    username = json.loads(user).get("username")
    response = user_request.put(username, new_user)

    assert_that(response.status_code).is_equal_to(codes.ok)
    assert_that(response.json()["code"]).is_equal_to(codes.ok)
    assert_that(response.json()["type"]).is_equal_to("unknown")
    assert_that(response.json()["message"]).is_not_empty()

    expected_user = json.loads(new_user)
    logger.info("- Step 3: Check that user updated: ", expected_user=expected_user)
    new_user_response = user_request.get(json.loads(new_user)["username"])
    assert_that(new_user_response.json()["username"]).is_equal_to(expected_user["username"])
    assert_that(new_user_response.json()["email"]).is_equal_to(expected_user["email"])
    assert_that(new_user_response.json()["password"]).is_equal_to(expected_user["password"])


should_create_user()
should_get_error_when_not_found_user()
should_delete_user()
should_update_user()
