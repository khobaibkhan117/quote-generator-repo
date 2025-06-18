from flask import Flask, jsonify
import random

app = Flask(__name__)

# List of quotes
quotes = [
    {"quote": "The only limit is your mind.", "author": "Unknown"},
    {"quote": "Work hard in silence, let success make the noise.", "author": "Frank Ocean"},
    {"quote": "Code. Deploy. Sleep. Repeat.", "author": "Khobaib"},
]

# Route to get a random quote
@app.route("/quote")
def get_quote():
    return jsonify(random.choice(quotes))

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
