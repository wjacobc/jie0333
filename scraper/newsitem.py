import re

class NewsItem():
    def __init__(self, headline, source, publish_date, snippet, url):
        self.headline = headline
        self.source = source
        self.publish_date = publish_date
        self.snippet = self.remove_html_tags(snippet)
        self.url = url
        self.tags = {}


    def remove_html_tags(self, string):
        # use regular expression matching any html tag (<h1> for example) and replacing
        # it with nothing
        return re.sub(r"<[^>]*>", "", string)

    def __repr__(self):
        return f"{self.source}: {self.headline} - {self.snippet.strip()} - {self.publish_date}"


    def to_json(self):

        json_dict = {"headline": self.headline, "source": self.source, "publish_date": str(self.publish_date),
                        "snippet": self.snippet, "url": self.url, "tags": self.tags}
        return json_dict
