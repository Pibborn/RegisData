from .settings import Constants
import logging
logging.basicConfig(level=Constants.LOGGING_LEVEL)


class Scraper:

    def __init__(self, scrapingstrategy: staticmethod = None) -> object:
        if scrapingstrategy is not None:
            self.scrape = scrapingstrategy

    def scrape(self):
        logging.error("The default Scraper scrape() method was called. This should never happen.")


def facebook_scraping(url: str) -> None:
    logging.info("facebook_scraping(" + url + ") was called.")
    appid = Constants.FB_APP_PUBLIC_ID
    logging.info("Scraping FB page " + url + ". App ID is " + appid + ".")


def ilgiornale_scraping(url: str) -> None:
    logging.info("ilgiornale_scraping(" + url + ") was called.")
    logging.error("Unsupported method.")
