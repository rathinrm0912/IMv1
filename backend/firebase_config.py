import firebase_admin
from firebase_admin import credentials, firestore
import os
import json

# Initialize Firebase Admin
# You will need to add a 'FIREBASE_SERVICE_ACCOUNT' environment variable in Netlify/Vercel
service_account_info = os.environ.get('FIREBASE_SERVICE_ACCOUNT')

if service_account_info:
    # Parse the JSON string from environment variable
    cert_dict = json.loads(service_account_info)
    cred = credentials.Certificate(cert_dict)
    firebase_admin.initialize_app(cred)
else:
    # Fallback for local development if you have the file locally
    # cred = credentials.Certificate("path/to/serviceAccountKey.json")
    # firebase_admin.initialize_app(cred)
    print("Warning: FIREBASE_SERVICE_ACCOUNT not found in environment")

db = firestore.client()

# Collection names used in server.py
USERS_COLLECTION = "users"
DOCUMENTS_COLLECTION = "documents"
COMMENTS_COLLECTION = "comments"
NOTIFICATIONS_COLLECTION = "notifications"