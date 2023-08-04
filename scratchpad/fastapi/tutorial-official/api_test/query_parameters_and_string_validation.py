from pprint import pprint

import requests

# JSON_HEADER = {"Content-Type": "application/json", "charset": "utf-8"}
HOST = "http://localhost:8000"
ROOT = HOST + "/query_parameters_and_string_validation"


def print_func_name(func):

    def wrapper(*args, **kwargs):
        print("-----" + func.__name__ + "-----")
        func(*args, **kwargs)

    return wrapper


@print_func_name
def read_items_without_q():
    payload = {}
    r = requests.get(ROOT + "/items", params=payload)
    pprint(r.json())


@print_func_name
def read_items_with_q():
    payload = {"q": "Baz"}
    r = requests.get(ROOT + "/items", params=payload)
    pprint(r.json())


@print_func_name
def read_items2_valid_length():
    payload = {"q": "Baz"}
    r = requests.get(ROOT + "/items2", params=payload)
    pprint(r.json())


@print_func_name
def read_items2_invalid_length():
    payload = {"q": "Baz" * 20}
    r = requests.get(ROOT + "/items2", params=payload)
    pprint(r.json())


@print_func_name
def read_items3_valid_length():
    payload = {"q": "Baz"}
    r = requests.get(ROOT + "/items2", params=payload)
    pprint(r.json())


@print_func_name
def read_items3_invalid_length():
    payload = {"q": "Baz" * 20}
    r = requests.get(ROOT + "/items2", params=payload)
    pprint(r.json())


@print_func_name
def read_items4_invalid():
    payload = {"q": "Baz"}
    r = requests.get(ROOT + "/items4", params=payload)
    pprint(r.json())


@print_func_name
def read_items5_non_none_default():
    payload = {}
    r = requests.get(ROOT + "/items5", params=payload)
    pprint(r.json())


@print_func_name
def read_items6_required_by_no_val():
    payload = {}
    r = requests.get(ROOT + "/items6", params=payload)
    pprint(r.json())


@print_func_name
def read_items7_required_by_ellipsis():
    payload = {}
    r = requests.get(ROOT + "/items7", params=payload)
    pprint(r.json())


@print_func_name
def read_items8_required_but_can_be_none():
    payload = {"q": ""}
    r = requests.get(ROOT + "/items8", params=payload)
    pprint(r.json())


@print_func_name
def read_items9_required_by_pydantic_required():
    payload = {}
    r = requests.get(ROOT + "/items9", params=payload)
    pprint(r.json())


@print_func_name
def read_items10_list_query():
    payload = {"q": ["fish", "baz"]}
    r = requests.get(ROOT + "/items10", params=payload)
    pprint(r.json())


@print_func_name
def read_items11_list_becomes_body_if_no_query():
    payload = {"q": ["fish", "baz"]}
    print("-- as query --")
    r = requests.get(ROOT + "/items11", params=payload)
    pprint(r.json())
    print("-- as body --")
    r = requests.get(ROOT + "/items11", json=payload)
    pprint(r.json())


def main():
    read_items_without_q()
    read_items_with_q()
    read_items2_valid_length()
    read_items2_invalid_length()
    read_items3_valid_length()
    read_items3_invalid_length()
    read_items4_invalid()
    read_items5_non_none_default()
    read_items6_required_by_no_val()
    read_items7_required_by_ellipsis()
    read_items8_required_but_can_be_none()
    read_items9_required_by_pydantic_required()
    read_items10_list_query()
    read_items11_list_becomes_body_if_no_query()


if __name__ == "__main__":
    main()
