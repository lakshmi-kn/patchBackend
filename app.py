
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO
import logging
from config import FLASK_HOST, FLASK_PORT, FLASK_DEBUG

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Global variable to store latest health data
latest_health_data = None

@app.route('/')
def index():
    logger.info("Serving index page")
    return render_template('index.html')

@app.route('/api/vitals', methods=['GET', 'POST'])
def vitals():
    global latest_health_data

    if request.method == 'POST':
        latest_health_data = request.get_json()
        logger.info(f"Received new health data: {latest_health_data}")
        socketio.emit('health_data', latest_health_data)
        return jsonify({"status": "success"}), 200

    elif request.method == 'GET':
        logger.info("API request for latest vitals")
        if latest_health_data:
            return jsonify(latest_health_data)
        else:
            logger.warning("No health data available")
            return jsonify({"error": "No data available"}), 404

@app.route('/api/vitals/history')
def get_vitals_history():
    return jsonify({"message": "Historical data endpoint - to be implemented"})

@socketio.on('connect')
def handle_connect():
    logger.info("Client connected")
    if latest_health_data:
        socketio.emit('health_data', latest_health_data)

@socketio.on('disconnect')
def handle_disconnect():
    logger.info("Client disconnected")

if __name__ == '__main__':
    print(f"\nStarting server at http://{FLASK_HOST}:{FLASK_PORT}")
    print("Press Ctrl+C to stop\n")

    socketio.run(
        app,
        host=FLASK_HOST,
        port=FLASK_PORT,
        debug=FLASK_DEBUG,
        use_reloader=False
    )
