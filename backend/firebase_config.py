import firebase_admin
from firebase_admin import credentials, firestore
import os
import json

# Initialize Firebase Admin SDK
try:
    # This prevents errors if the app is initialized multiple times during development
    firebase_app = firebase_admin.get_app()
except ValueError:
    # Pull the JSON string from your environment variable
    service_account_info = os.environ.get('FIREBASE_SERVICE_ACCOUNT')
    
    if service_account_info:
        # Parse the JSON string into a dictionary that Python understands
        cert_dict = json.loads(service_account_info)
        cred = credentials.Certificate(cert_dict)
        firebase_admin.initialize_app(cred)
    else:
        print("CRITICAL ERROR: FIREBASE_SERVICE_ACCOUNT not found in environment variables.")

# Create the Firestore client
db = firestore.client()

# Collection names (must match your Firestore database)
USERS_COLLECTION = "users"
DOCUMENTS_COLLECTION = "documents"
COMMENTS_COLLECTION = "comments"
NOTIFICATIONS_COLLECTION = "notifications"