import firebase_admin
from firebase_admin import credentials, firestore

# Use a raw string literal to avoid escape sequence issues
cred = credentials.Certificate(r'D:\fir\payment-app-76b49-firebase-adminsdk-6ix0m-0029f64c73.json')

firebase_admin.initialize_app(cred)

db = firestore.client()
