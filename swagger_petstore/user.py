"""This module was created to test petstore-swagger user API"""

import json
import os
import requests

HEADERS = {"accept": "application/json", "Content-Type": "application/json"}
URN = "https://petstore.swagger.io/v2"
SP_USER_ID = os.environ["SP_USER_ID"]
SP_USERNAME = os.environ["SP_USERNAME"]
SP_PASSWORD = os.environ["SP_PASSWORD"]


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
        URN + "/user", headers=HEADERS, data=json.dumps(payload), timeout=15
    )
    assert response.status_code == 200, "Error: " + str(response.status_code)


def test_get_user():
    """Testing api to get the user info by username"""

    response = requests.get(URN + f"/user/{SP_USERNAME}", headers=HEADERS, timeout=15)
    assert response.status_code == 200, "Error: " + str(response.status_code)


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
        URN + f"/user/{SP_USERNAME}",
        headers=HEADERS,
        data=json.dumps(payload),
        timeout=15,
    )
    assert response.status_code == 200, "Error: " + str(response.status_code)


def test_get_login():
    """Testing api to login into the system (always return 200)"""

    response = requests.get(
        URN + f"/user/login?username={SP_USERNAME}02&password={SP_PASSWORD[::-1]}",
        headers=HEADERS,
        timeout=15,
    )
    assert response.status_code == 200, "Error: " + str(response.status_code)


def test_get_logout():
    """Testing api to logout to the system (always return 200)"""

    response = requests.get(URN + "/user/logout", headers=HEADERS, timeout=15)
    assert response.status_code == 200, "Error: " + str(response.status_code)


def test_delete_user():
    """Testing api to delete a user by username"""

    response = requests.delete(
        URN + f"/user/{SP_USERNAME}02", headers=HEADERS, timeout=15
    )
    assert response.status_code == 200, "Error: " + str(response.status_code)


def test_delete_user_confirmation():
    """Testing api to get the user by username if 404 is OK"""

    response = requests.get(URN + f"/user/{SP_USERNAME}02", headers=HEADERS, timeout=15)
    assert response.status_code == 404, "Error: " + str(response.status_code)
