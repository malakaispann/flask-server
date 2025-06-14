import requests
import json
import os

URI = os.getenv("URI")

def test_get():
    for endpoint in ['', '/get_json']:
        response = requests.get(f"{URI}{endpoint}")
        assert response.ok
        
        json = response.json()
        assert json["data"] == "Hello World"


def test_post():
    
    to_send = {
        "foo": "bar",
    }
    
    response = requests.post(f"{URI}/post_json", json=to_send)
    assert response.ok
    
    json = response.json()
    assert json["data"] == "Hello World"
    assert json["input"] == to_send
