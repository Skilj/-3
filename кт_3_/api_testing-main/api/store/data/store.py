import json
import random
from dataclasses import dataclass, asdict
from datetime import datetime

from api.logger import logger


@dataclass()
class Store:
    id: int
    petId: int
    quantity: int
    shipDate: str
    status: str
    complete: bool

    def to_dict(self):
        return asdict(self)


def __generate_random_data():
    # Generate random data
    random_id = random.randint(1, 100)
    random_pet_id = random.randint(1, 6)
    random_quantity = random.randint(1, 10)
    random_ship_date = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
    random_status = 'placed'
    random_complete = random.choice([True, False])

    # Create and return a dictionary
    random_store_dict = {
        'id': random_id,
        'petId': random_pet_id,
        'quantity': random_quantity,
        'shipDate': random_ship_date,
        'status': random_status,
        'complete': random_complete
    }

    return random_store_dict


def get_random_store():
    # Create and return a Store instance
    random_store = __generate_random_data()

    json.dumps(random_store, ensure_ascii=False)

    logger.info("Create random store:", random_store=random_store)

    return random_store
