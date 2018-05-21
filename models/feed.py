class NewsFeed(object):

    def __init__(self, title, link, published_date):
        self.title = title
        self.link = link
        self.published_date = published_date

    def __str__(self):
        return u"Title: {title}\nURL: {url}".format(title=self.title, url=self.link).encode('utf-8') 
