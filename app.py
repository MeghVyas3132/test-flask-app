from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/info')
def info():
    return jsonify({
        'app_name': 'Test Flask App',
        'version': '1.0.0',
        'status': 'running',
        'endpoints': [
            {'path': '/', 'method': 'GET', 'description': 'Home page'},
            {'path': '/api/info', 'method': 'GET', 'description': 'API information'},
            {'path': '/api/data', 'method': 'GET', 'description': 'Sample data'}
        ]
    })

@app.route('/api/data')
def data():
    return jsonify({
        'items': [
            {'id': 1, 'name': 'Sample Item 1', 'value': 100},
            {'id': 2, 'name': 'Sample Item 2', 'value': 200},
            {'id': 3, 'name': 'Sample Item 3', 'value': 300}
        ]
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)