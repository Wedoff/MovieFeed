from classes.news import News
import feedparser

__NEWS_SOURCES = ['https://st.kp.yandex.net/rss/news_feed.rss']


def updateNewsCollection(lastServerNewsDate):
    """Function gets last server's news date
        and saves to server all news which were
        posted after that date on sources"""

    newNews = []    #contains news from sources which are not on the server yet

    for source in __NEWS_SOURCES:
        newNews.extend(__getListOfNewNewsFromSource(source, lastServerNewsDate))

    newNews.sort(key = __sortByDate)

    __saveNews(newNews)



def __getListOfNewNewsFromSource(source, lastServerNewsDate):

    return feedparser.parse(source)

def __sortByDate(news):
    return news.date

def __saveNews(newNews):
    return

print(__getListOfNewNewsFromSource(__NEWS_SOURCES[0], 0)['entries'])