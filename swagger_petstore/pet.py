"""This module was created to test petstore-swagger pet API"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

HEADERS = {"accept": "application/json", "Content-Type": "application/json"}
URN = "https://petstore.swagger.io/v2/pet"
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
        url=URN,
        headers=HEADERS,
        json=payload,
        timeout=15
    )
    response_data = response.json()
    # print(response.json())  # Print the response in json format
    assert response.status_code == 200, "Error: " + str(response.status_code)
    assert response_data["name"] == "Koala"
    assert response_data["category"]["name"] == "siamese cat"


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
        url=URN,
        headers=HEADERS,
        json=payload,
        timeout=15
    )
    response_data = response.json()
    # print(response.json())  # Print the response in json format
    assert response.status_code == 200, "Error: " + str(response.status_code)
    assert response_data["name"] == "Mascarita"
    assert response_data["category"]["name"] == "tuxedo cat"


def test_post_existing_pet():
    """Testing api to update the pet name and status"""

    payload = "name=Guantes&status=sold"
    local_header = HEADERS
    local_header["Content-Type"] = "application/x-www-form-urlencoded"

    response = requests.post(
        url=URN + f"/{PET_ID}",
        headers=local_header,
        data=payload,
        timeout=15
    )
    # print(response.json())  # Print the response in json format
    assert response.status_code == 200, "Error: " + str(response.status_code)


def test_get_pets_status():
    """Testing api to get every pet based on status"""

    response = requests.get(
        url=URN + "/findByStatus?status=sold",
        headers=HEADERS,
        timeout=15
    )
    pet_data = next(pet for pet in response.json() if pet["id"] == int(PET_ID))
    # print(pet_data)
    assert response.status_code == 200, "Error: " + str(response.status_code)
    assert pet_data["name"] == "Guantes"
    assert pet_data["status"] == "sold"


def test_get_pets_tags():
    """Testing api to get every pet based on tag name (DEPRECATED)"""

    response = requests.get(
        url=URN + "/findByTags?tags=noisy",
        headers=HEADERS,
        timeout=15
    )
    # print(response.json())
    assert response.status_code == 200, "Error: " + str(response.status_code)


def test_get_pet():
    """Testing api to get a pet by id"""

    response = requests.get(
        url=URN + f"/{PET_ID}",
        headers=HEADERS,
        timeout=15
    )
    response_data = response.json()
    # print(response.json())  # Print the response in json format
    assert response.status_code == 200, "Error: " + str(response.status_code)
    assert response_data["category"]["name"] == "tuxedo cat"
    assert response_data["name"] == "Guantes"
    assert response_data["tags"]["name"] == "mute"


def test_delete_pet():
    """Testing api to delete a pet by id"""

    response = requests.delete(
        url=URN + f"/{PET_ID}",
        headers=HEADERS,
        timeout=15
    )
    # print(response.json())
    assert response.status_code == 200, "Error: " + str(response.status_code)
    assert response.json()["message"] == PET_ID


def test_delete_pet_confirmation():
    """Testing api to get a pet by id if 404 is OK"""

    response = requests.get(
        url=URN + f"/{PET_ID}",
        headers=HEADERS,
        timeout=15
    )
    # print(response.json())  # Print the response in json format
    assert response.status_code == 404, "Error: " + str(response.status_code)
