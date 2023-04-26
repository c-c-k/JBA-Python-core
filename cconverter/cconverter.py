import requests


def main():
    cur_code = input()
    url = f"http://www.floatrates.com/daily/{cur_code}.json"
    exchange_rates = requests.get(url).json()
    print(exchange_rates['usd'])
    print(exchange_rates['eur'])


if __name__ == "__main__":
    main()
