import datetime
import requests
import creds

current_date = datetime.date.today()
previous_day = current_date - datetime.timedelta(days = 1)
ticker = input("What ticker would you like to look up?\n").upper()

spy_url = f"https://api.polygon.io/v1/open-close/{ticker}/{previous_day}?adjusted=true&apiKey={creds.api_key}"
response = requests.get(spy_url)
data = response.json()
print(f"Ticker: {data["symbol"]}")
print(f"Date: {data["from"]}")
print(f"Market open price: ${data["open"]}")
print(f"Market close price: ${data["close"]}")

