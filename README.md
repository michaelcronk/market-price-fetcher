# Market Price Fetcher

## Overview

**Market Price Fetcher** is a web application built with Flask that allows users to retrieve and view real-time stock market data. The application fetches the latest opening and closing prices for a given stock ticker symbol using the Polygon.io API. The results are presented in a clean, responsive interface, making it easy for users to access and understand the retrieved JSON data.

_Click here to see a [DEMO](https://youtu.be/dAB0uNtWByU)_

## Features

- **Data Retrieval**: The app fetches data for market open and close prices for a specified stock ticker. (It currently only gets previous day price data due to the free product tier)
- **User-Friendly Interface**: The UI is designed with simplicity in mind, allowing users to quickly input a stock ticker and retrieve relevant data.
- **Responsive Design**: The application is mobile-friendly and works seamlessly across various devices and screen sizes.
- **Bootstrap Styling**: The interface is styled using Bootstrap for a modern and professional look.
- **Custom CSS**: Some additional styling is applied via a custom CSS file to enhance the visual appeal and usability of the application.

## Installation

<sup>Follow the steps below to set up and run the project locally<sup>

### Prerequisites

- **Python 3.7+**: Ensure you have Python installed on your system.
- **Flask**: The web framework used for the application.
- **Polygon.io API Key**: You'll need an API key from [Polygon.io](https://polygon.io/) to fetch stock data.

### Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/market-price-fetcher.git
   cd market-price-fetcher
   ```

2. **(OPTIONAL) Create a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Configure API Key:**

- Create a file named creds.py in the root directory of the project (or use .env for environment variables)
- Add your Polygon.io API key to this file:
  ```python
  api_key = 'your_polygon_api_key'
  ```

4. **Run the Application:**

   ```bash
   python retrieve_data.py
   ```

- Once the Flask app is running, you can access the application by navigating to http://localhost:5000 in your web browser.

## Usage

- **Input a Stock Ticker:** On the homepage, enter a valid stock ticker symbol (e.g., AAPL for Apple).
- **View Results:** The application will display the latest available opening and closing prices for the given stock ticker.

### Project Structure

```plaintext
Market Price Fetcher/
│
├── retrieve_data.py # Main application file
├── creds.py # File containing API key (not included in the repo)
├── templates/
│ └── index.html # Main HTML template
└── static/
  └── css/
    └── styles.css # Custom CSS file
```

### Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.
