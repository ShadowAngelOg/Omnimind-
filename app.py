# FILE: app.py
# This is the simplest possible server. Its only job is to serve one file.

from flask import Flask, render_template

# Make sure Flask is installed: pip install Flask
app = Flask(__name__)

@app.route('/')
def index():
    # This looks in the 'templates' folder for 'index.html' and shows it.
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

