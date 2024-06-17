import requests

database = {
    1: {"name": "Alice", "age": 25},
    2: {"name": "Bob", "age": 30},
    3: {"name": "Charlie", "age": 35},
    4: {"name": "David", "age": 40},
    5: {"name": "Eve", "age": 45},
}

def get_user_by_id(user_id):
    return database.get(user_id)

def get_user_by_id_api(id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}")
    if response.status_code == 200:
        return response.json()

    raise requests.exceptions.HTTPError