from .contrib import get_fb_posts_fb_page
from .contrib import get_fb_comments_from_fb
from .settings import Constants
import logging
logging.basicConfig(level=Constants.LOGGING_LEVEL)


class Scraper:

    def __init__(self, scrapingstrategy: staticmethod = None) -> object:
        if scrapingstrategy is not None:
            self.scrape = scrapingstrategy

    def scrape(self):
        logging.error("The default Scraper scrape() method was called. This should never happen.")


def facebook_scraping(page_id: str) -> None:
    logging.info("facebook_scraping(" + page_id + ") was called.")
    app_id = Constants.FB_APP_PUBLIC_ID
    app_secret = Constants.FB_APP_SECRET_ID
    logging.info("Scraping FB page http://facebook.com/" + page_id + ". App ID is " + app_id + ".")
    get_fb_posts_fb_page.scrapeFacebookPageFeedStatus(page_id, app_id + "|" + app_secret)
    get_fb_comments_from_fb.scrapeFacebookPageFeedComments(page_id, app_id + "|" + app_secret)


def ilgiornale_scraping(url: str) -> None:
    logging.info("ilgiornale_scraping(" + url + ") was called.")
    logging.error("Unsupported method.")
