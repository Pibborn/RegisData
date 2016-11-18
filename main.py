import sys
from scraper.scraping import *

from scraper.to_gsheets import *


def main(args):
    ## example gsheet updating

    creds = get_credentials()

    #spreadsheet = create_spreadsheet(creds, 'Attempt-18nov')
    worksheet = get_worksheet(creds, 'Attempt-18nov', 1)
    csv_to_gsheet(worksheet, "foobar")


    ## example scraping
    #firstscraper = Scraper(facebook_scraping)

    #logging.info("Calling firstScraper.scrape()")
    #firstscraper.scrape("salviniofficial")


main(sys.argv)
