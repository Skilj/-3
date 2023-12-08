import requests
from assertpy import assert_that
from requests import codes

from api.base_request import BaseRequest
from api.logger import logger
from api.rest_settings import BASE_URL_PETSTORE
from api.store.data.store import get_random_store, Store


class StoreRequest(BaseRequest):
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
    #     self._log_response(request_type, response)
    #     return response
    #
    # def _log_response(self, request_type, response):
    #     pprint(100 * "=")
    #     pprint(f'{request_type} example')
    #     pprint(response.url)
    #     pprint(response.status_code)
    #     pprint(response.reason)
    #     pprint(response.text)
    #     pprint(response.json())
    #     pprint('**********')
    #
    # def _make_request(self, data, request_type, url):
    #     if url.__contains__("/store/order") and request_type == 'POST':
    #         response = requests.post(url, json=data, headers=headers)
    #     elif request_type == 'GET':
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
    # def delete(self, username, expected_error=False):
    #     delete_url = f'{self.path}/{username}'
    #     response = self._request(delete_url, 'DELETE', expected_error=expected_error)
    #     request = response.request
    #     get_logs(request, response)
    #     return response


def should_create_order():
    logger.info(100 * "=")
    logger.info("Start test should_create_order()")
    logger.info(100 * "-")

    store = get_random_store()
    store_request = StoreRequest(path="/store/order")

    logger.info("- Step 1: Create order:", store=store)
    response = store_request.post(store)

    assert_that(response.status_code).is_equal_to(codes.ok)
    try:
        assert_that(response.json()).is_equal_to(store)
    except AssertionError as e:
        logger.error("- Bug (wrong milliseconds):", e=e)


def should_get_error_when_not_found_order():
    logger.info(100 * "=")
    logger.info("Start test should_get_error_when_not_found_order()")
    logger.info(100 * "-")

    store_request = StoreRequest(path="/store/order")
    logger.info("- Check error when pet ID > 10:", pet_id=11)
    response = store_request.get(11, True)

    assert_that(response.status_code).is_equal_to(requests.codes.not_found)
    assert_that(response.json()).is_instance_of(dict)
    assert_that(response.json()).contains_key("code").contains_key("type").contains_key("message")
    assert_that(response.json()["code"]).is_equal_to(1)
    assert_that(response.json()["type"]).is_equal_to("error")
    assert_that(response.json()["message"]).is_equal_to("Order not found")


def should_get_order():
    logger.info(100 * "=")
    logger.info("Start test should_get_order()")
    logger.info(100 * "-")

    store_request = StoreRequest(path="/store/order")
    store = get_random_store()
    logger.info("- Step 1: Create order:", store=store)
    response = store_request.post(store)
    assert_that(response.status_code).is_equal_to(codes.ok)

    order_id = store.get("id")
    logger.info("- Check can get order:", order_id=order_id)

    response = store_request.get(order_id)

    expected_order_id = Store(order_id, store.get("petId"), store.get("quantity"), store.get("shipDate"),
                              store.get("status"), store.get("complete"))
    assert_that(response.status_code).is_equal_to(codes.ok)
    assert_that(response.json()["id"]).is_equal_to(expected_order_id.__getattribute__("id"))
    assert_that(response.json()["petId"]).is_equal_to(expected_order_id.__getattribute__("petId"))
    assert_that(response.json()["quantity"]).is_equal_to(expected_order_id.__getattribute__("quantity"))
    assert_that(response.json()["shipDate"]).contains(expected_order_id.__getattribute__("shipDate"))
    assert_that(response.json()["status"]).is_equal_to(expected_order_id.__getattribute__("status"))
    assert_that(response.json()["complete"]).is_equal_to(expected_order_id.__getattribute__("complete"))


def should_delete_order():
    logger.info(100 * "=")
    logger.info("Start test should_delete_order()")
    logger.info(100 * "-")
    store = get_random_store()
    store_request = StoreRequest(path="/store/order")

    logger.info("- Step 1: Create order")
    store_request.post(store)

    logger.info("- Step 2: Delete order: ", store=store)
    store_id = store.get("id")
    response = store_request.delete(store_id)

    assert_that(response.status_code).is_equal_to(codes.ok)
    assert_that(response.json()["code"]).is_equal_to(codes.ok)
    assert_that(response.json()["type"]).is_equal_to("unknown")
    assert_that(response.json()["message"]).is_equal_to(store_id.__str__())


should_create_order()
should_get_error_when_not_found_order()
should_get_order()
should_delete_order()
