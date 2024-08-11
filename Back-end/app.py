from flask import Flask, g, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token
from firebase_config import db
from routes.payment import payment_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)

@app.before_request
def before_request():
    g.db = db

@app.teardown_request
def teardown_request(exception):
    pass

app.register_blueprint(payment_bp)

@app.route('/api/login', methods=['POST'])
@app.route('/api/login', methods=['POST'])
def login():
    token = request.headers.get('Authorization')
    if token is None:
        return jsonify({"error": "Unauthorized"}), 401
    
    try:
        decoded_token = auth.verify_id_token(token)
        user_id = decoded_token['uid']
        # Proceed with login
        return jsonify({"user_id": user_id}), 200
    except:
        return jsonify({"error": "Invalid token"}), 401


if __name__ == '__main__':
    app.run(debug=True)
