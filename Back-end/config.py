import os
from cryptography.fernet import Fernet

class Config:
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')
    ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY', Fernet.generate_key().decode())  # Generate if not set
    FRAUD_MODEL_PATH = os.getenv('FRAUD_MODEL_PATH', 'fraud_detection_model.pkl')
