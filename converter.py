import requests
import json

currency_code = input()
url = "http://www.floatrates.com/daily/{0}.json".format(currency_code.lower())
r = requests.get(url)
json_file = r.json()
cache = ["eur", "usd"]
exchange_code = input()
while exchange_code != "":
    start = int(input())
    if exchange_code in cache:
        total = round((json_file[exchange_code]["rate"] * start), 2)
        print("Checking the cache...")
        print("Oh! It is in the cache!")
        print("You have received", total, exchange_code)
    else:
        print("Checking the cache...")
        print("Sorry, but it is not in the cache!")
        total = round((json_file[exchange_code]["rate"] * start), 2)
        cache.append(exchange_code)
        print("You have received", total, exchange_code)
    exchange_code = input()
