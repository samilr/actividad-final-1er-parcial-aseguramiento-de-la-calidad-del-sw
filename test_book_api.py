import pytest
import requests

BASE_URL = "https://simple-books-api.glitch.me" 
TOKEN = "545a475f6d122994e427f45a1138b76160e95c2b7fa99338b0526a4f53a83d14"  

headers = {
   'Content-Type': 'application/json',
   'Authorization': f'Bearer {TOKEN}'
}

def test_status_code():
    response = requests.get(f"{BASE_URL}/status")
    assert response.status_code == 200
    assert response.json()['status'] == 'OK'

def test_get_non_fiction_books():
    response = requests.get(f"{BASE_URL}/books", params={"type": "non-fiction"})
    assert response.status_code == 200
    books = response.json()
    non_fiction_books = [book for book in books if book['available'] == True]
    assert len(non_fiction_books) > 0, "No available non-fiction books found"

def test_get_single_book():
    book_id = 1  
    response = requests.get(f"{BASE_URL}/books/{book_id}")
    assert response.status_code == 200
    book = response.json()
    assert book['id'] == book_id

def test_order_book():
    order_data = {
        "bookId": 1, 
        "customerName": "Samir"
    }
    response = requests.post(f"{BASE_URL}/orders", json=order_data, headers=headers)
    assert response.status_code == 201

def test_get_all_orders():
    headers = {'Authorization': f'Bearer {TOKEN}'}
    response = requests.get(f"{BASE_URL}/orders", headers=headers)
    assert response.status_code == 200
    orders = response.json()
    assert len(orders) > 0, "No orders found"

def test_create_order():
    data = {
        "bookId": 1,
        "customerName": "Alfreda"
    }

    response = requests.post(f"{BASE_URL}/orders", headers=headers, json=data)
    assert response.status_code == 201
    order = response.json()
    assert order['created'] is True
    assert 'orderId' in order