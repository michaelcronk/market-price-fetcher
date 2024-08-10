from flask import Flask, render_template, request
import datetime
import requests
import creds  # Your API key should be stored here

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def stock_lookup():
    data = None
    if request.method == "POST":
        ticker = request.form.get("ticker").upper()
        current_date = datetime.date.today()
        previous_day = current_date - datetime.timedelta(days=1)
        spy_url = f"https://api.polygon.io/v1/open-close/{ticker}/{previous_day}?adjusted=true&apiKey={creds.api_key}"
        response = requests.get(spy_url)
        data = response.json()

    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
