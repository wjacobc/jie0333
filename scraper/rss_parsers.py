import feedparser
import ssl
from newsitem import NewsItem
from datetime import datetime

# patch ssl library for newer versions of python where feedparser has an issue
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

def gather_all_news():
    all_news = nih_rss() + cdc_rss() + nyt_rss() + lat_rss() + who_rss() \
        + nejm_rss() + healthyUNH_rss()
    return all_news

def lat_rss():
    lat = feedparser.parse("https://www.latimes.com/science/rss2.0.xml")
    entries = lat["entries"]

    newsitems = []
    for entry in entries:
        date_object = datetime.strptime(entry["published"], "%a, %d %b %Y %H:%M:%S %z")

        date_object = date_object.replace(tzinfo = None)

        headline = entry["title"]
        source = "The Los Angeles Times"
        publish_date = date_object
        snippet = entry["summary"]
        url = entry["link"]

        newsitem_entry = NewsItem(headline, source, publish_date, snippet, url)
        newsitems.append(newsitem_entry)

    return newsitems

def who_rss():
    who = feedparser.parse("https://www.who.int/feeds/entity/csr/don/en/rss.xml")
    entries = who["entries"]
    newsitems = []
    for entry in entries:
        date_object = datetime.strptime(entry["published"], "%a, %d %b %Y %H:%M:%S %Z")
        date_object=date_object.replace(tzinfo=None)
        headline = entry["title"]
        source = "World Health Organization"
        publish_date = date_object
        snippet = entry["summary"]
        url = entry["link"]

        newsitem_entry = NewsItem(headline, source, publish_date, snippet, url)
        newsitems.append(newsitem_entry)

    return newsitems

def healthyUNH_rss():
    healthyUNH = feedparser.parse("https://www.unh.edu/healthyunh/blog.xml")
    entries = healthyUNH["entries"]

    newsitems = []
    for entry in entries:
        date_object = datetime.strptime(entry["published"], "%a, %d %b %Y %H:%M:%S %z")

        date_object = date_object.replace(tzinfo = None)

        headline = entry["title"]
        source = "Healthy UNH"
        publish_date = date_object
        snippet = entry["summary"]
        url = entry["link"]

        newsitem_entry = NewsItem(headline, source, publish_date, snippet, url)
        newsitems.append(newsitem_entry)

    return newsitems

def nejm_rss():
    nejm = feedparser.parse(
        "https://www.nejm.org/action/showFeed?jc=nejm&type=etoc&feed=rss")
    # print(nejm['entries'].keys)
    entries = nejm["entries"]

    newsitems = []
    for entry in entries:
        # convert the string date representation into a python datetime object
        date_object = datetime.strptime(
            entry["updated"], "%Y-%m-%dT%H:%M:%SZ"
        )
        headline = entry["title"]
        source = "New England Journal of Medicine"
        publish_date = date_object
        snippet = entry["summary"]
        url = entry["link"]

        newsitem = NewsItem(headline, source, publish_date, snippet, url)
        newsitems.append(newsitem)

    return newsitems

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

        newsitem_entry = NewsItem(headline, source, publish_date, snippet, url)
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

        # compile the information into the shared object format
        newsitem_entry = NewsItem(headline, source, publish_date, snippet, url)
        newsitems.append(newsitem_entry)

    return newsitems


def nyt_rss():
    nyt = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/Health.xml")
    entries = nyt["entries"]

    newsitems = []
    for entry in entries:
        # convert the string date representation into a python datetime object
        date_object = datetime.strptime(entry["published"], "%a, %d %b %Y %H:%M:%S %z")
        # remove the time zone offset so we can compare it to other newsitems
        date_object = date_object.replace(tzinfo = None)

        headline = entry["title"]
        source = "The New York Times"
        publish_date = date_object
        # some NYT articles have empty snippets, should we skip these
        # or try to create one?
        snippet = entry["summary"]
        url = entry["link"]
        # NYT has tags in entry["tags"] - do we want to use these?
        # problem is they will likely not line up with the ones we generate

        newsitem_entry = NewsItem(headline, source, publish_date, snippet, url)
        newsitems.append(newsitem_entry)

    return newsitems
