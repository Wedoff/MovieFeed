from classes.review import Review

__REVIEWS_SOURCES = []


def updateReviewsCollection(lastServerReviewsDate):
    """Function gets last server's review's date
        and saves to server all reviews which were
        posted after that date on sources"""

    newReviews = []    #contains reviews from sources which are not on the server yet

    for source in REVIEWS_SOURCES:
        newReviews.extend(__getListOfNewReviewsFromSource(source))

    newReviews.sort(key = __sortByDate)

    __saveReviews(newReviews)



def __getListOfNewReviewsFromSource(source):
    return

def __sortByDate(news):
    return news.date

def __saveReviews(newReviews):
    return