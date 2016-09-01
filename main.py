import sys
from scraper.scraping import *


def main(args):
    firstscraper = Scraper(facebook_scraping)

    logging.info("Calling firstScraper.scrape()")
    firstscraper.scrape("coolieband")


main(sys.argv)
