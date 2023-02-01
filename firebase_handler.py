import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time 
from datetime import datetime 

class FirebaseHandler:
    def __init__(self):
        cred = credentials.Certificate("./trunk-raspberry-pi-tah-firebase-adminsdk-pxjji-d8f129d255.json")
        firebase_admin.initialize_app(cred)
        self.firestore = firestore.client()
        self.collection = self.firestore.collection('main')

    def save(self, temperature, humidity):
        try:
            doc = self.collection.document()
            data = {
                'temperature' : temperature,
                'humidity' : humidity,
                'timestamp' : time.time()
            }
            # timestamp to string method
            doc.set(data)
            print("save successed.")
            return data
        except:
            print("save failed.")
            return False
    
    def get_date_time(timestamp):
        dateTime = datetime.fromtimestamp(timestamp)
        strDateTime = dateTime.strftime("%Y-%m-%d, %H:%M:%S")
        return strDateTime
