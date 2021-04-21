import firebase_utils
import rss_parsers
from datetime import datetime


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
                    newsitem.tags[word] = True


def get_news_match_tags():
    all_news = rss_parsers.gather_all_news()

    # just get the items that have been added to the RSS feeds since the
    # last time we ran the scraper
    last_ran_scraper = firebase_utils.last_ran_scraper()
    recent_news = [newsitem for newsitem in all_news if newsitem.publish_date > last_ran_scraper]

    match_tags(recent_news)

    return recent_news


if __name__ == "__main__":
    news_to_upload = get_news_match_tags()
    firebase_utils.upload_newsitems(news_to_upload)
    firebase_utils.update_last_ran()
