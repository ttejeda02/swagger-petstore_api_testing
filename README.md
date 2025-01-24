# Swagger Petstore API Testing
## Features
- **Automated API testing**: allows to verify basic API operations like GET, POST, PUT and DELETE.
- **HTTP status code validation**: ensures that the API responses return the correct HTTP status codes (e.g., `200 OK`).
- **JSON response data validation**: verifies that the response data is correct at a basic level.
- **Easy to use**: configurable tests that require minimal setup in a virtual environment.
- **Error code verification**: specifically checks for error codes like `404` to ensure that deletion work as expected.
- **Individual Test Execution**: Tests can be run individually or in groups, allowing for flexible and targeted testing of specific API endpoints.

## Requirements
- Python 3
- Pip 24

## Installation
### Download the repository
```bash
git clone https://github.com/ttejeda02/swagger-petstore_api_testing.git
cd swagger-petstore_api_testing/
```
### Create the virtual environment and activate it
#### On Windows
```
python -m venv venv
```
Activate in **Command prompt**:
```cmd
venv\Scripts\activate
```
Activate in **Powershell**:
```PowerShell
.\venv\Scripts\Activate.ps1
```
#### On macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Create .env file
In the root of the project directory, create a .env file. This file will store all your environment variables in the following format:
```bash
SP_USER_ID=user_id_value
SP_USERNAME=username_value
SP_PASSWORD=password_value
ORDER_ID=order_id_value
PET_ID=pet_id_value
```

## Usage
To run all test use:
```bash
pytest swagger_petstore/
```
To run the set of test individually use:
```bash
pytest swagger_petstore/test_pet.py
```
```bash
pytest swagger_petstore/test_store.py
```
```bash
pytest swagger_petstore/test_user.py
```
#### Pytest options
Use `-v` to show detailed information for each test, including the test name and whether it passed or failed.
```bash
pytest -v swagger_petstore/test_pet.py
```
Use `-q` to show a minimal summary at the end of the test run (pass/fail counts).
```bash
pytest -q swagger_petstore/test_user.py
```
The `-r` flag displays a summary of the results with additional information about the test execution. You can specify different formats:
- short: Show a brief summary.
- f: Show only failed tests.
- p: Show only passed tests.
- x: Show expected failures.
- a: Show aborted tests.
```bash
pytest -r p swagger_petstore/test_store.py
```

## Deactivate the virtual environment
To deactivate the virtual environment, use the following command:
```bash
deactivate
```