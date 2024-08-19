from flask import Flask, render_template, request
import datetime
import requests
import creds  # Your API key should be stored here or in .env

app = Flask(__name__)


def get_previous_trading_day(current_date):
    # Check to see if date is Saturday(5), Sunday(6), or a Monday(0)
    if current_date.weekday() == 5:
        previous_day = current_date - datetime.timedelta(days=1)  # Friday
    elif current_date.weekday() == 6:
        previous_day = current_date - datetime.timedelta(days=2)  # Friday
    elif current_date.weekday() == 0:
        previous_day = current_date - datetime.timedelta(days=3)  # Friday
    else:
        previous_day = current_date - datetime.timedelta(days=1)

    return previous_day


@app.route("/", methods=["GET", "POST"])
def stock_lookup():
    data = None
    if request.method == "POST":
        ticker = request.form.get("ticker").upper()  # Making the ticker uppercase
        current_date = datetime.date.today()
        previous_day = get_previous_trading_day(current_date)
        url = f"https://api.polygon.io/v1/open-close/{ticker}/{previous_day}?adjusted=true&apiKey={creds.api_key}"
        response = requests.get(url)
        data = response.json()

    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
