import feedparser
from newsitem import NewsItem
from datetime import datetime

def match_tags(headline, snippet):
    tags = []
    # get potential tags from source
    # compare headline and snippet with tags to see which match
    return tags

def firebase_last_ran():
    # connect to firebase
    # get the last time the scraper ran and return as datetime object

    # for now it's just february 10 2021
    return datetime.strptime("02/10/2021", "%m/%d/%Y")

def update_firebase_last_ran():
    # push the current date and time to firebase
    # to update the entry for when we last ran the scraper
    pass

def cdc_rss():
    cdc = feedparser.parse("https://tools.cdc.gov/podcasts/feed.asp?feedid=183")
    entries = cdc["entries"]

    newsitems = []
    for entry in entries:
        # convert the string date representation into a python datetime object
        date_object = datetime.strptime(entry["updated"], "%Y-%m-%dT%H:%M:%SZ")

        headline = entry["title"]
        source = "Centers for Disease Control"
        publish_date = date_object
        snippet = entry["summary"]
        url = entry["link"]
        tags = match_tags(headline, snippet)
        
        newsitem_entry = NewsItem(headline, source, publish_date, snippet, url, tags)
        newsitems.append(newsitem_entry)

    return newsitems
        


def nih_rss():
    nih = feedparser.parse("https://www.nih.gov/news-releases/feed.xml")
    entries = nih["entries"]

    newsitems = []
    for entry in entries:
        # convert the string date representation into a python datetime object
        date_object = datetime.strptime(entry["published"], "%Y-%m-%d %H:%M:%S")

        headline = entry["title"]
        source = "National Insitutes of Health"
        publish_date = date_object
        snippet = entry["summary"]
        url = entry["link"]
        tags = match_tags(headline, snippet)

        # compile the information into the shared object format
        newsitem_entry = NewsItem(headline, source, publish_date, snippet, url, tags)
        newsitems.append(newsitem_entry)

    return newsitems


def nyt_rss():
    nyt = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/Health.xml")
    entries = nyt["entries"]

    newsitems = []
    for entry in entries:
        # convert the string date representation into a python datetime object
        date_object = datetime.strptime(entry["published"], "%a, %d %b %Y %H:%M:%S %z")
        # remove the time zone offset so we can compare it to other articles
        date_object = date_object.replace(tzinfo = None)

        headline = entry["title"]
        source = "The New York Times"
        publish_date = date_object
        # some NYT articles have empty snippets, should we skip these 
        # or try to create one?
        snippet = entry["summary"]
        url = entry["link"]
        tags = match_tags(headline, snippet)
        # NYT has tags in entry["tags"] - do we want to use these?
        # problem is they will likely not line up with the ones we generate

        newsitem_entry = NewsItem(headline, source, publish_date, snippet, url, tags)
        newsitems.append(newsitem_entry)

    return newsitems


def collect_articles():
    nih_articles = nih_rss()
    cdc_articles = cdc_rss()
    nyt_articles = nyt_rss()
    articles = nih_articles + cdc_articles + nyt_articles

    # just get the articles that have been added to the RSS feeds since the
    # last time we ran the scraper
    last_ran_scraper = firebase_last_ran()
    recent_articles = [article for article in articles if article.publish_date > last_ran_scraper]

    return recent_articles

if __name__ == "__main__":
    articles_to_upload = collect_articles()
    update_firebase_last_ran()
