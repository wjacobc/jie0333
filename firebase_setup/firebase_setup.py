import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

# Take your credentialing file and put it in the creds folder named "credentials.json"
# This means it won't be uploaded to the repo but will be found by the program
cred = credentials.Certificate("creds/credentials.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': "https://jie-0333-default-rtdb.firebaseio.com/"
})

ref = db.reference('')
items = ref.child("news_items")

with open("news_items.json", "r") as json_file:
    json_data = json.load(json_file)
    items.set(json_data)

