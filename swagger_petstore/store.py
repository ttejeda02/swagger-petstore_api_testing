"""This module was created to test petstore-swagger store API"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

HEADERS = {"accept": "application/json", "Content-Type": "application/json"}
URN = "https://petstore.swagger.io/v2/store"
ORDER_ID = os.environ["ORDER_ID"]
PET_ID = os.environ["PET_ID"]


def test_get_inventory():
    """Testing api to get the inventory by status"""

    response = requests.get(
        URN + "/inventory",
        headers=HEADERS,
        timeout=5
    )
    assert response.status_code == 200, "Error: " + str(response.status_code)


def test_post_order():
    """Testing api to order for a pet"""

    payload = {
        "id": ORDER_ID,
        "petId": PET_ID,
        "quantity": 1,
        "shipDate": "2023-10-31T03:40:39.506Z",
        "status": "placed",
        "complete": True,
    }

    response = requests.post(
        URN + "/order",
        headers=HEADERS,
        json=payload,
        timeout=5
    )
    assert response.status_code == 200, "Error: " + str(response.status_code)


def test_get_order():
    """Testing api to get the purchase data by id"""

    response = requests.get(
        URN + f"/order/{ORDER_ID}",
        headers=HEADERS,
        timeout=5
    )
    assert response.status_code == 200, "Error: " + str(response.status_code)


def test_api_delete_order():
    """Testing api to delete the purchase by id"""

    response = requests.delete(
        URN + f"/order/{ORDER_ID}",
        headers=HEADERS,
        timeout=5
    )
    assert response.status_code == 200, "Error: " + str(response.status_code)


def test_delete_order_confirmation():
    """Testing api to get the purchase by id if 404 is OK"""

    response = requests.get(
        URN + f"/order/{ORDER_ID}",
        headers=HEADERS,
        timeout=5
    )
    assert response.status_code == 404, "Error: " + str(response.status_code)
