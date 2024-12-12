from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

# Sample data (just for illustration purposes)
timestamps = [
    1733821200, 1733824800, 1733828400, 1733832000, 1733835600, 1733839200, 1733842800,
    1733846400, 1733850000, 1733853600, 1733857200, 1733860800, 1733864400, 1733868000,
    1733871600, 1733875200, 1733878800, 1733882400, 1733886000, 1733889600, 1733893200,
    1733896800, 1733900400, 1733904000, 1733907600, 1733911200, 1733914800, 1733918400,
    1733922000, 1733925600, 1733929200, 1733932800, 1733936400, 1733940000, 1733943600,
    1733947200, 1733950800
]
prices = [
    3.7199999999999998, 0.73, 0.0, 0.0, 0.0, 0.01, 1.96, 1.6099999999999999, 3.66,
    5.07, 4.22, 4.17, 3.92, 3.46, 3.58, 3.27, 2.95, 2.6, 3.34, 2.63, 2.14, 1.47,
    1.18, 1.1, 0.0, -0.1, -0.11, -0.30000000000000004, -0.11, -0.05, 0.01, 1.5, 3.14,
    3.37, 5.38, 5.02, 4.26, 3.6, 2.99, 2.76, 2.8, 2.5, 2.33, 3.05, 3.04, 3.25, 3.74,
    3.6
]

# Convert timestamps to days and hours and combine with prices
class PriceData:
    def __init__(self, timestamp, price):
        self.timestamp = timestamp
        self.price = price
        # Convert timestamp to a human-readable date and time format
        self.date_time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    def to_dict(self):
        return {"time": self.date_time, "price": self.price}

# Combine timestamps and prices into PriceData objects
price_data_objects = []
for ts, price in zip(timestamps, prices):
    price_data = PriceData(ts, price)
    price_data_objects.append(price_data)

@app.route('/api/prices', methods=['GET'])
def get_prices():
    # Return the prices as JSON
    return jsonify({"prices": [price_data.to_dict() for price_data in price_data_objects]})

if __name__ == '__main__':
    app.run(debug=True)
