// Import Firebase SDKs
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getFirestore } from "firebase/firestore";
import { getAuth } from "firebase/auth";

// Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyAUIbaz0U4nYl5b6mRrB3Iitd3MhfunEfA",
  authDomain: "im-b169f.firebaseapp.com",
  projectId: "im-b169f",
  storageBucket: "im-b169f.firebasestorage.app",
  messagingSenderId: "674696535188",
  appId: "1:674696535188:web:135799dea0cd25f5bee881",
  measurementId: "G-EHNHB5ZW5V"
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);
export const analytics = getAnalytics(app);
export const db = getFirestore(app);
export const auth = getAuth(app);

// Collections (same naming as Python)
export const USERS_COLLECTION = "users";
export const DOCUMENTS_COLLECTION = "documents";
export const COMMENTS_COLLECTION = "comments";
export const NOTIFICATIONS_COLLECTION = "notifications";
