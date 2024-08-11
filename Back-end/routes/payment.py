import os
import requests
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.transaction import TransactionModel
from fraud_detection import predict_fraud

payment_bp = Blueprint('payment_bp', __name__)

# Ensure the API key is set
api_key = os.getenv('API_SETU_KEY')
if api_key is None:
    raise ValueError("API_SETU_KEY environment variable is not set")

@payment_bp.route('/api/upi_payment', methods=['POST'])
@jwt_required()
def upi_payment():
    data = request.get_json()

    # Run fraud detection on the transaction data
    is_fraud, fraud_probability = predict_fraud(data)

    if is_fraud:
        return jsonify({"error": "Fraudulent transaction detected", "fraud_probability": fraud_probability}), 403
    
    # Proceed with payment processing if not fraudulent
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    payload = {
        "amount": data['amount'],
        "vpa": data['vpa'],  # Virtual Payment Address of the recipient
        "transaction_note": "Payment for services",
        "transaction_id": data['transaction_id'],
        "merchant_code": "your_merchant_code"  # Replace with your actual merchant code
    }

    response = requests.post("https://api.api-setu.com/upi/payment", headers=headers, json=payload)

    if response.status_code == 200:
        transaction_data = {
            "amount": data['amount'],
            "vpa": data['vpa'],
            "transaction_id": data['transaction_id'],
            "status": response.json().get('status', 'pending'),
            "created_at": response.json().get('created_at'),
            "response": response.json(),
            "is_fraud": is_fraud,
            "fraud_probability": fraud_probability
        }
        transaction_id = TransactionModel(request.db).create_transaction(transaction_data)
        return jsonify({"transaction_id": str(transaction_id), "status": "Payment initiated"}), 201
    else:
        print(f"API Setu request failed with status code {response.status_code} and response {response.json()}")
        return jsonify({"error": "Payment failed", "details": response.json()}), response.status_code
