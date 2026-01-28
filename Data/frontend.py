from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Backend API URL
API_URL = "http://localhost:8080"

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    try:
        files = {'file': (file.filename, file.read(), file.content_type)}
        response = requests.post(f"{API_URL}/upload", files=files)
        
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': response.text}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/query', methods=['POST'])
def query():
    """Handle query requests"""
    data = request.get_json()
    
    if not data or 'query' not in data:
        return jsonify({'error': 'No query provided'}), 400
    
    try:
        payload = {
            'query': data['query'],
            'model': data.get('model', 'llama3.2')
        }
        response = requests.post(
            f"{API_URL}/query",
            json=payload,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': response.text}), response.status_code
    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Cannot connect to backend server'}), 503
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    """Check backend health"""
    try:
        response = requests.get(f"{API_URL}/docs", timeout=2)
        if response.status_code == 200:
            return jsonify({'status': 'online'})
        else:
            return jsonify({'status': 'error'}), 500
    except:
        return jsonify({'status': 'offline'}), 503

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
