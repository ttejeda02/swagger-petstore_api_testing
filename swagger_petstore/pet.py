"""This module was created to test petstore-swagger pet API"""

import json
import os
import requests

HEADERS = {"accept": "application/json", "Content-Type": "application/json"}
URN = "https:/store.swagger.io/v2/pet"
PET_ID = os.environ["PET_ID"]


def test_post_new_pet():
    """Testing api to create a new pet in petstore swagger"""

    payload = {
        "id": PET_ID,
        "category": {"id": 1, "name": "siamese cat"},
        "name": "Koala",
        "photoUrls": ["string"],
        "tags": [{"id": 1, "name": "noisy"}],
        "status": "available",
    }

    response = requests.post(
        URN, headers=HEADERS, data=json.dumps(payload), timeout=15
    )
    # print(response.json())  # Print the response in json format
    assert response.status_code == 200, "Error: " + str(response.status_code)


def test_put_existing_pet():
    """Testing api to update a pet"""

    payload = {
        "id": PET_ID,
        "category": {"id": 1, "name": "tuxedo cat"},
        "name": "Mascarita",
        "photoUrls": ["string"],
        "tags": [{"id": 2, "name": "mute"}],
        "status": "pending",
    }

    response = requests.put(
        URN, headers=HEADERS, data=json.dumps(payload), timeout=15
    )
    # print(response.json())  # Print the response in json format
    assert response.status_code == 200, "Error: " + str(response.status_code)


def test_post_existing_pet():
    """Testing api to update the pet name and status"""

    payload = "name=Guantes&status=sold"
    local_header = HEADERS
    local_header["Content-Type"] = "application/x-www-form-urlencoded"

    response = requests.post(
        URN + f"/{PET_ID}", headers=local_header, data=payload, timeout=15
    )
    # print(response.json())  # Print the response in json format
    assert response.status_code == 200, "Error: " + str(response.status_code)


def test_get_pets_status():
    """Testing api to get every pet based on status"""

    response = requests.get(
        URN + "/findByStatus?status=sold", headers=HEADERS, timeout=15
    )
    assert response.status_code == 200, "Error: " + str(response.status_code)


def test_get_pets_tags():
    """Testing api to get every pet based on tag name"""

    response = requests.get(
        URN + "/findByTags?tags=noisy", headers=HEADERS, timeout=15
    )
    assert response.status_code == 200, "Error: " + str(response.status_code)


def test_get_pet():
    """Testing api to get a pet by id"""

    response = requests.get(URN + f"/{PET_ID}", headers=HEADERS, timeout=15)
    # print(response.json())  # Print the response in json format
    assert response.status_code == 200, "Error: " + str(response.status_code)


def test_delete_pet():
    """Testing api to delete a pet by id"""

    response = requests.delete(URN + f"/{PET_ID}", headers=HEADERS, timeout=15)
    assert response.status_code == 200, "Error: " + str(response.status_code)


def test_delete_pet_confirmation():
    """Testing api to get a pet by id if 404 is OK"""

    response = requests.get(URN + f"/{PET_ID}", headers=HEADERS, timeout=15)
    # print(response.json())  # Print the response in json format
    assert response.status_code == 404, "Error: " + str(response.status_code)
