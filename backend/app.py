from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to DevOps Dashboard!"})

@app.route('/metrics')
def metrics():
    return jsonify({
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent
    })

@app.route('/data')
def data():
    # Sample application data
    return jsonify({
        "users": 120,
        "active_sessions": 23
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
