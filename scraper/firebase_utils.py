from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("creds/credentials.json")

firebase_admin.initialize_app(cred, {
        'databaseURL': "https://jie-0333-default-rtdb.firebaseio.com/"
        })

def last_ran_scraper():
    # connect to firebase
    # get the last time the scraper ran and return as datetime object

    ref = db.reference("last_ran")
    return datetime.strptime(ref.get(), "%Y-%m-%d %H:%M:%S.%f")

def update_last_ran(latest):
    # push the current date and time to firebase
    # to update the entry for when we last ran the scraper
    last_ran = db.reference('last_ran')
    last_ran.set(str(latest))


def upload_newsitems(newsitem_list):
    newsitems_ref = db.reference("newsitems")
    for item in newsitem_list:
        newsitems_ref.push(item.to_json())

