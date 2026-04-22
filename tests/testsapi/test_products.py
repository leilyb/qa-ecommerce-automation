import requests
import json
import pytest 
BASE_URL = "https://dummyjson.com"

@pytest.mark.smoke
@pytest.mark.api
def test_get_all_products():
    response = requests.get(f"{BASE_URL}/products")
    print(response.status_code)
    assert response.status_code == 20000

    body = response.json()
    # print(body)
    assert "products" in body
    assert len(body["products"]) > 0

@pytest.mark.api
def test_get_single_product():
    response = requests.get(f"{BASE_URL}/products/1")
    assert response.status_code == 200

    body = response.json()
    # print(json.dumps(body, indent = 4))
    print(body["title"])
    assert body["id"] == 1
    assert "title" in body

@pytest.mark.api
def test_get_invalid_product():
    response = requests.get(f"{BASE_URL}/products/999999")

    assert response.status_code in [404, 400]    