import requests


def main():
    input_cur_code = input()

    url = f"http://www.floatrates.com/daily/{input_cur_code}.json"
    all_cur = requests.get(url, timeout=1).json()

    cache = {cache_cur["code"].lower(): cache_cur["rate"] for cache_cur
             in (cur_info for (cur_code, cur_info) in all_cur.items()
                 if cur_code.lower() in {'usd', 'eur'})}

    while True:
        output_cur_code = input()
        if output_cur_code == "":
            break
        cur_amount = input()
        if cur_amount == "":
            break
        cur_amount = float(cur_amount)
        print("Checking the cache...")
        if output_cur_code.lower() in cache.keys():
            print("Oh! It is in the cache!")
        else:
            print("Sorry, but it is not in the cache!")
            base_cur = all_cur[output_cur_code.lower()]
            cache[output_cur_code.lower()] = base_cur["rate"]
        rate = cache[output_cur_code.lower()]
        print(f"You received {cur_amount * rate:.2f} {output_cur_code}.")


if __name__ == "__main__":
    main()
