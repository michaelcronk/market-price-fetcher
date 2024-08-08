import requests
import creds

spy_url = f"https://api.polygon.io/v1/open-close/SPY/2024-08-07?adjusted=true&apiKey={creds.api_key}"
response = requests.get(spy_url)
data = response.json()
print(f"Ticker: {data["symbol"]}")
print(f"Date: {data["from"]}")
print(f"Market open price: ${data["open"]}")
print(f"Market close price: ${data["close"]}")

print()

qqq_url = f"https://api.polygon.io/v1/open-close/QQQ/2024-08-07?adjusted=true&apiKey={creds.api_key}"
response = requests.get(qqq_url)
data = response.json()
print(f"Ticker: {data["symbol"]}")
print(f"Date: {data["from"]}")
print(f"Market open price: ${data["open"]}")
print(f"Market close price: ${data["close"]}")

