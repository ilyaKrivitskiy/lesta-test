from flask import Flask, jsonify
import redis
import os

from pyexpat import expat_CAPI

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, db=0, decode_responses=True)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "ok"})

@app.route('/count', methods=['GET'])
def count():
    try:
        visits = redis_client.incr("visit_count")
        return jsonify({"visit_count": visits})
    except redis.exceptions.ConnectionError:
        return jsonify({'error': 'Redis is not available'}), 500

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
