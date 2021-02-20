import feedparser
import ssl
import firebase_utils
from newsitem import NewsItem
from datetime import datetime

# patch ssl library for newer versions of python where feedparser has an issue
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context


def check_case_insensitive(word, headline, snippet):
    return word.lower() in headline or word.lower() in snippet


def match_tags(news_list):
    # get potential tags from source
    # compare headline and snippet with tags to see which match
    with open("keywords.txt", "r") as keywords_file:
        keywords = keywords_file.read().split("\n")[:-1]
        for newsitem in news_list:
            headline_words = newsitem.headline.lower().split(" ")
            snippet_words = newsitem.snippet.lower().split(" ")

            for word in keywords:
                if check_case_insensitive(word, headline_words, snippet_words):
                    newsitem.tags.append(word)


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


def collect_news():
    nih_news = nih_rss()
    cdc_news = cdc_rss()
    nyt_news = nyt_rss()
    all_news = nih_news + cdc_news + nyt_news

    # just get the items that have been added to the RSS feeds since the
    # last time we ran the scraper
    last_ran_scraper = firebase_utils.last_ran_scraper()
    recent_news = [newsitem for newsitem in all_news if newsitem.publish_date > last_ran_scraper]

    match_tags(recent_news)

    return recent_news


if __name__ == "__main__":
    news_to_upload = collect_news()
    firebase_utils.upload_newsitems(news_to_upload)
    firebase_utils.update_last_ran()
