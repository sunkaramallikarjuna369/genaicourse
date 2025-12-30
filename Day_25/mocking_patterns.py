"""Day 25: Mocking and Unit.mock"""
from unittest.mock import Mock, MagicMock, patch, call
import requests

class DataService:
    def fetch_user(self, user_id):
        response = requests.get(f"https://api.example.com/users/{user_id}")
        return response.json()

def test_mock_basic():
    service = DataService()
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'id': 1, 'name': 'John'}
        result = service.fetch_user(1)
        assert result['name'] == 'John'
        mock_get.assert_called_once()

def test_mock_side_effect():
    mock = Mock(side_effect=[1, 2, 3])
    assert mock() == 1
    assert mock() == 2

def test_magic_mock():
    m = MagicMock()
    m.method.return_value = 'result'
    assert m.method() == 'result'

def test_assert_called_with():
    m = Mock()
    m.greet('hello')
    m.assert_called_with('hello')
    m.assert_called_once_with('hello')
