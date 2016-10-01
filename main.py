import sys
from scraper.scraping import *

from scraper.to_gsheets import *


def main(args):
    ## example gsheet updating

    creds = get_credentials()

    worksheet = get_worksheet(creds, 'Attempt', 1)
    csv_to_gsheet(worksheet, "foobar")


    ## example scraping
    #firstscraper = Scraper(facebook_scraping)

    #logging.info("Calling firstScraper.scrape()")
    #firstscraper.scrape("LIntraprendente")


main(sys.argv)
