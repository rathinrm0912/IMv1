import firebase_admin
from firebase_admin import credentials, firestore
import os
import json

# Initialize Firebase Admin
try:
    # Check if app is already initialized to avoid errors on reload
    firebase_app = firebase_admin.get_app()
except ValueError:
    # Get the JSON string from your Environment Variable
    service_account_info = os.environ.get('FIREBASE_SERVICE_ACCOUNT')
    
    if service_account_info:
        # Convert the string back into a JSON dictionary
        cert_dict = json.loads(service_account_info)
        cred = credentials.Certificate(cert_dict)
        firebase_admin.initialize_app(cred)
    else:
        print("ERROR: FIREBASE_SERVICE_ACCOUNT not found in environment variables.")

db = firestore.client()

# Collection names (used by your server.py)
USERS_COLLECTION = "users"
DOCUMENTS_COLLECTION = "documents"
COMMENTS_COLLECTION = "comments"
NOTIFICATIONS_COLLECTION = "notifications"