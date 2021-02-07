import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

def upload_to_db(items):
    with open("news_items.json", "r") as json_file:
        json_data = json.load(json_file)
        items.set(json_data)

def get_news_by_tag(ref, tag):
    matching_news = []

    news = ref.get()["news_items"]
    for news_item in news:
        lowercase_tags = [item_tag.lower() for item_tag in news_item["tags"]]
        if tag.lower() in lowercase_tags:
            matching_news.append(news_item)

    return matching_news


# Take your credentialing file and put it in the creds folder named "credentials.json"
# This means it won't be uploaded to the repo but will be found by the program
cred = credentials.Certificate("creds/credentials.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': "https://jie-0333-default-rtdb.firebaseio.com/"
})

ref = db.reference('')
items = ref.child("news_items")

