def main():
    print("Please, enter the number of conicoins you have:")
    conicoins = int(input())
    print("Please, enter the exchange rate:")
    exchange_rate = float(input())
    print(f"The total amount of dollars: {conicoins * exchange_rate}")

if __name__ == "__main__":
    main()
