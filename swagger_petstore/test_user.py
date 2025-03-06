"""This module was created to test petstore-swagger user API"""

import os
import requests
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_fixed

load_dotenv()

HEADERS = {"accept": "application/json", "Content-Type": "application/json"}
BASE_URL = "https://petstore.swagger.io/v2/user"
SP_USER_ID = os.environ["SP_USER_ID"]
SP_USERNAME = os.environ["SP_USERNAME"]
SP_PASSWORD = os.environ["SP_PASSWORD"]


@retry(stop=stop_after_attempt(5), wait=wait_fixed(3))
def test_post_new_user():
    """Testing api to create a new user"""

    payload = {
        "id": SP_USER_ID,
        "username": SP_USERNAME,
        "firstName": "Noah",
        "lastName": "Secret",
        "email": "user@example.dom",
        "password": SP_PASSWORD,
        "phone": "+11234567890",
        "userStatus": 1,
    }

    response = requests.post(
        url=BASE_URL,
        headers=HEADERS,
        json=payload,
        timeout=5
    )
    assert response.status_code == 200, "Error: " + str(response.status_code)
    assert response.json()["message"] == SP_USER_ID


@retry(stop=stop_after_attempt(5), wait=wait_fixed(3))
def test_get_user():
    """Testing api to get the user info by username"""

    response = requests.get(
        BASE_URL + f"/{SP_USERNAME}",
        headers=HEADERS,
        timeout=5
    )
    response_data = response.json()
    assert response.status_code == 200, "Error: " + str(response.status_code)
    assert response_data["id"] == int(SP_USER_ID)
    assert response_data["username"] == SP_USERNAME
    assert response_data["password"] == SP_PASSWORD


@retry(stop=stop_after_attempt(5), wait=wait_fixed(3))
def test_put_user():
    """Testing api to update user info"""

    payload = {
        "id": SP_USER_ID,
        "username": f"{SP_USERNAME}02",
        "firstName": "Eonoz",
        "lastName": "Rit",
        "email": "another@mail.com",
        "password": SP_PASSWORD[::-1],
        "phone": "+11234567890",
        "userStatus": 2,
    }

    response = requests.put(
        BASE_URL + f"/{SP_USERNAME}",
        headers=HEADERS,
        json=payload,
        timeout=5
    )
    assert response.status_code == 200, "Error: " + str(response.status_code)


@retry(stop=stop_after_attempt(5), wait=wait_fixed(3))
def test_get_user_confirmation():
    """Testing api to get the user info by username"""

    response = requests.get(
        BASE_URL + f"/{SP_USERNAME}02",
        headers=HEADERS,
        timeout=5
    )
    response_data = response.json()
    assert response.status_code == 200, "Error: " + str(response.status_code)
    assert response_data["id"] == int(SP_USER_ID)
    assert response_data["username"] == f"{SP_USERNAME}02"
    assert response_data["password"] == SP_PASSWORD[::-1]


@retry(stop=stop_after_attempt(5), wait=wait_fixed(3))
def test_get_login():
    """Testing api to login into the system (always return 200)"""

    response = requests.get(
        BASE_URL + f"/login?username={SP_USERNAME}02&password={SP_PASSWORD[::-1]}",
        headers=HEADERS,
        timeout=5,
    )
    assert response.status_code == 200, "Error: " + str(response.status_code)


@retry(stop=stop_after_attempt(5), wait=wait_fixed(3))
def test_get_logout():
    """Testing api to logout to the system (always return 200)"""

    response = requests.get(
        BASE_URL + "/logout",
        headers=HEADERS,
        timeout=5
    )
    assert response.status_code == 200, "Error: " + str(response.status_code)


@retry(stop=stop_after_attempt(5), wait=wait_fixed(3))
def test_delete_user():
    """Testing api to delete a user by username"""

    response = requests.delete(
        BASE_URL + f"/{SP_USERNAME}02",
        headers=HEADERS,
        timeout=5
    )
    assert response.status_code == 200, "Error: " + str(response.status_code)
    assert response.json()["message"] == f"{SP_USERNAME}02"


@retry(stop=stop_after_attempt(5), wait=wait_fixed(3))
def test_delete_user_confirmation():
    """Testing api to get the user by username if 404 is OK"""

    response = requests.get(
        BASE_URL + f"/{SP_USERNAME}02",
        headers=HEADERS,
        timeout=5
    )
    assert response.status_code == 404, "Error: " + str(response.status_code)
