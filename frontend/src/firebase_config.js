import firebase from "firebase";
export const firebaseConfig = {
  apiKey: "AIzaSyCyqvP2IcDKKBmNL6vwLxWiEg8wh5wdL6U",
  authDomain: "jie-0333.firebaseapp.com",
  databaseURL: "https://jie-0333-default-rtdb.firebaseio.com",
  projectId: "jie-0333",
  storageBucket: "jie-0333.appspot.com",
  messagingSenderId: "912091952109",
  appId: "1:912091952109:web:acae801f363b16726fede4",
  measurementId: "G-9G2TJZFESY",
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();

export default firebase;
