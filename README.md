# Swagger Petstore API Testing
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

### Deactivate the virtual environment
To deactivate the virtual environment, use the following command:
```bash
deactivate
```