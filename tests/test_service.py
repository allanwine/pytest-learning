import pytest
import src.service as service
import unittest.mock as mock
import requests

@mock.patch('src.service.get_user_by_id')
def test_get_user_by_id(mock_test_get_user_by_id):
    mock_test_get_user_by_id.return_value = {"name": "Mocked Alice", "age": "35"}

    assert service.get_user_by_id(2) == {"name": "Mocked Alice", "age": "35"}

def test_get_user_by_id_api():
    response = service.get_user_by_id_api(2)
    assert response == {
  "id": 2,
  "name": "Ervin Howell",
  "username": "Antonette",
  "email": "Shanna@melissa.tv",
  "address": {
    "street": "Victor Plains",
    "suite": "Suite 879",
    "city": "Wisokyburgh",
    "zipcode": "90566-7771",
    "geo": {
      "lat": "-43.9509",
      "lng": "-34.4618"
    }
  },
  "phone": "010-692-6593 x09125",
  "website": "anastasia.net",
  "company": {
    "name": "Deckow-Crist",
    "catchPhrase": "Proactive didactic contingency",
    "bs": "synergize scalable supply-chains"
  }
}

@mock.patch('requests.get')
def test_get_mocked_user_by_id(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    # We use return value here because .json is a method call, not a property
    mock_response.json.return_value = {"name": "Mocked Bob", "age": "20"}
    mock_get.return_value = mock_response

    response = service.get_user_by_id_api(1)
    assert response == {"name": "Mocked Bob", "age": "20"}

@mock.patch('requests.get')
def test_error_get_mocked_user_by_id_api(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_response.json.return_value = {"error": "Bad Request"}
    mock_get.return_value = mock_response

    with pytest.raises(requests.exceptions.HTTPError):
        service.get_user_by_id_api(1)