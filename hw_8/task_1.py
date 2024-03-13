import argparse
import requests
from datetime import datetime, timedelta
import json

def load_symbols():
    with open("symbols.json", "r") as f:
        return json.load(f)["symbols"]

def get_exchange_rate(from_currency, to_currency, amount, date):
    url = "https://api.exchangerate.host/convert"
    params = {
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "date": date
    }
    response = requests.get(url, params=params)
    data = response.json()
    if 'result' not in data:
        raise ValueError("Failed to get exchange rate")
    rate = data['info']['rate']
    result = data['result']
    return date, rate, result

def main():
    symbols = load_symbols()

    parser = argparse.ArgumentParser(description="Online currency converter")
    parser.add_argument("currency_from", type=str, help="Currency to convert from")
    parser.add_argument("currency_to", type=str, help="Currency to convert to")
    parser.add_argument("amount", type=float, help="Amount to convert")
    parser.add_argument("--start_date", type=str, default=datetime.now().strftime("%Y-%m-%d"), help="Start date")
    parser.add_argument("--save_to_file", action="store_true", help="Save results to file")
    args = parser.parse_args()

    if args.currency_from not in symbols or args.currency_to not in symbols:
        print("Invalid currency symbol.")
        return

    results = [['date', 'from', 'to', 'amount', 'rate', 'result']]
    start_date = datetime.strptime(args.start_date, "%Y-%m-%d")
    current_date = datetime.now()
    if start_date > current_date:
        start_date = current_date

    while start_date <= current_date:
        date_str = start_date.strftime("%Y-%m-%d")
        date, rate, result = get_exchange_rate(args.currency_from, args.currency_to, args.amount, date_str)
        results.append([date, args.currency_from, args.currency_to, args.amount, rate, result])
        start_date = start_date + timedelta(days=1)

    if args.save_to_file:
        filename = f"{datetime.now().strftime('%Y-%m-%d')}_exchange_rate_results.txt"
        with open(filename, 'w') as file:
            for row in results:
                file.write('\t'.join(map(str, row)) + '\n')
        print(f"Results saved to {filename}")
    else:
        for row in results:
            print('\t'.join(map(str, row)))

if __name__ == "__main__":
    main()
