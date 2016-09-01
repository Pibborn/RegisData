import sys
from scraper.scraping import *


def main(args):
    firstscraper = Scraper(facebook_scraping)
    secondscraper = Scraper(ilgiornale_scraping)

    logging.info("Calling firstScraper.scrape()")
    firstscraper.scrape("127.0.0.1")

    logging.info("Calling secondScraper.scrape()")
    secondscraper.scrape("127.0.0.1")

main(sys.argv)
