from functions import newsInterface, reviewsInterface

def main():
    while True:
        newsInterface.updateNewsCollection()
        reviewsInterface.updateReviewsCollection()