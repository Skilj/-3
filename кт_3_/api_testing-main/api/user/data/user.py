import json
import random
from csv import DictReader
from dataclasses import dataclass

import structlog

logger = structlog.get_logger()


@dataclass()
class User:
    username: str
    email: str
    password: str

    def to_dict(self):
        return {'username': self.username, 'email': self.email, 'password': self.password}


def __get_users_list_from_csv(path):
    users_list = []

    with open(path, newline='') as f:
        users_data = DictReader(f)

        for user_data in users_data:
            user = User(username=user_data['login'], email=user_data['email'], password=user_data['password'])
            users_list.append(user)

    return users_list


def get_random_user_json(path):
    random_index = random.randint(0, len(__get_users_list_from_csv(path)) - 1)
    random_user_dict = __get_users_list_from_csv(path)[random_index].to_dict()
    user = json.dumps(random_user_dict, ensure_ascii=False)

    logger.info("Create random user from csv file:", user=user)

    return user
