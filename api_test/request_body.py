from pprint import pprint

import requests

# JSON_HEADER = {"Content-Type": "application/json", "charset": "utf-8"}
HOST = "http://localhost:8000"
ROOT = HOST + "/request_body"


def create_item_full_data():
    """Create item with optional fields filled"""
    data = {
        "name": "item 1",
        "description": "description 1",
        "price": "42.23",
        "tax": "12"
    }
    r = requests.post(ROOT + "/items", json=data)
    pprint(r.json())


def create_item_partial_data():
    """Create item with optional fields omitted"""
    data = {
        "name": "item 1",
        "price": "42.23",
    }
    r = requests.post(ROOT + "/items", json=data)
    pprint(r.json())


def create_taxed_item():
    """Create an item that undergoes modification in the backend"""
    data = {
        "name": "item 1",
        "price": "42.23",
        "tax": "0.1"
    }
    r = requests.post(ROOT + "/items/taxed", json=data)
    pprint(r.json())


def body_and_path():
    """Put an item with using path and body"""
    data = {
        "name": "item 1",
        "price": "42.23",
    }
    r = requests.put(ROOT + "/items/14", json=data)
    pprint(r.json())


def body_and_path_and_query():
    """Put an item with using query and path and body"""
    data = {
        "name": "item 1",
        "price": "42.23",
    }
    params = {"q": "this item is marked"}
    r = requests.put(ROOT + "/items/14/remarks", params=params, json=data)
    print(r.url)
    pprint(r.json())


def main():
    # create_item_full_data()
    # create_item_partial_data()
    # create_taxed_item()
    # body_and_path()
    body_and_path_and_query()


if __name__ == "__main__":
    main()
