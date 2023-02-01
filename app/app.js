import { initializeApp } from "firebase/app";
// import { getDatabase } from "firebase/database";
import { getDatabase, ref, set,onValue,child,get } from "firebase/database";
import  admin from 'firebase-admin';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

var serviceAccount = path.join(__dirname,"./trunk-raspberry-pi-tah-firebase-adminsdk-pxjji-d8f129d255.json");

// TODO: Replace the following with your app's Firebase project configuration
// See: https://firebase.google.com/docs/web/learn-more#config-object
const firebaseConfig = {
  // ...
  // The value of `databaseURL` depends on the location of the database
  databaseURL: "https://console.firebase.google.com/project/trunk-raspberry-pi-tah/firestore/data/~2Fmain~2F37SzEbImtsNhjA6I4yhi",
};

// Initialize Firebase
 const app = admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});
console.log(app)

// Initialize Realtime Database and get a reference to the service
const database = getDatabase(app);

// function writeUserData(userId, name, email, imageUrl) {
//     const db = getDatabase();
//     set(ref(db, 'users/' + userId), {
//       username: name,
//       email: email,
//       profile_picture : imageUrl
//     });
//   }
// writeUserData(2,"Harvey","123@gmail.com","http:111.imgyr")

// const dbRef=ref(getDatabase());
// const userId=2;
// get(child(dbRef, `users/${userId}`)).then((snapshot) => {
//     if (snapshot.exists()) {
//       console.log(snapshot.val());
//     } else {
//       console.log("No data available");
//     }
//   }).catch((error) => {
//     console.error(error);
//   });