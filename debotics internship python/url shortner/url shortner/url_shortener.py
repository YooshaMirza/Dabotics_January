import os
import random
import string
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Dictionary to store short codes and their corresponding URLs
url_database = {}

def generate_short_code():
    """Generate a random short code."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['url']

    if not original_url.startswith(('http://', 'https://')):
        original_url = 'http://' + original_url

    if original_url in url_database.values():
        short_code = next(key for key, value in url_database.items() if value == original_url)
    else:
        short_code = generate_short_code()
        url_database[short_code] = original_url

    short_url = request.host_url + short_code
    return render_template('shorten.html', original_url=original_url, short_url=short_url)

@app.route('/<short_code>')
def redirect_to_original(short_code):
    original_url = url_database.get(short_code)
    if original_url:
        return redirect(original_url)
    else:
        return render_template('not_found.html')

if __name__ == '__main__':
    # For production use, consider using a more secure secret key and turning off debug mode
    app.secret_key = 'supersecretkey'
    app.run(debug=True)
