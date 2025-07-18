# FILE: app.py
# LOCATION: Place this in the root directory of your Codespace.

from flask import Flask, render_template, jsonify, send_from_directory

# Let's make sure Flask is installed. 
# In your terminal, run: pip install Flask
# If it's already installed, it'll just say so.

app = Flask(__name__)

# This route serves your main HTML file from the 'templates' folder.
@app.route('/')
def index():
    # This tells Flask to look inside the 'templates' folder for 'index.html'
    return render_template('index.html')

# This route serves the service worker file from the root directory.
@app.route('/sw.js')
def service_worker():
    return send_from_directory('.', 'sw.js')

# This route generates and serves the manifest.json file dynamically.
@app.route('/manifest.json')
def manifest():
    return jsonify({
        "name": "OmniMind Personal AI",
        "short_name": "OmniMind",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#0a0a1a",
        "theme_color": "#101024",
        "description": "Your personal AI homie from Chicago.",
        "icons": [
            {
                "src": "https://placehold.co/192x192/00bfff/0a0a1a?text=O",
                "sizes": "192x192",
                "type": "image/png"
            },
            {
                "src": "https://placehold.co/512x512/00bfff/0a0a1a?text=O",
                "sizes": "512x512",
                "type": "image/png"
            }
        ]
    })

# This starts the server.
if __name__ == '__main__':
    # This makes the server accessible from outside the Codespace.
    app.run(host='0.0.0.0', port=5000, debug=True)

