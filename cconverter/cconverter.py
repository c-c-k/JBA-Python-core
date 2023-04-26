EXCHANGE_RATES = {
    "RUB": 2.98,  # Russian Ruble; 1 conicoin = 2.98 RUB;
    "ARS": 0.82,  # Argentine Peso; 1 conicoin = 0.82 ARS;
    "HNL": 0.17,  # Honduran Lempira; 1 conicoin = 0.17 HNL;
    "AUD": 1.9622,  # Australian Dollar; 1 conicoin = 1.9622 AUD;
    "MAD": 0.208,  # Moroccan Dirham; 1 conicoin = 0.208 MAD.
}


def main():
    conicoins = float(input())
    for (cur_id, cur_rate) in EXCHANGE_RATES.items():
        print(f"I will get {conicoins * cur_rate:.2f} {cur_id}"
              f" from the sale of {conicoins} conicoins.")


if __name__ == "__main__":
    main()
