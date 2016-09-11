import sys
from scraper.scraping import *

from scraper.to_gsheets import *


def main(args):
    creds = get_credentials()
    #create_spreadsheet(creds, 'Attempt2')

    worksheet = get_worksheet(creds, 'Attempt', 1)
    hello_worksheet(worksheet)

    #create_spreadsheet(creds)
    #firstscraper = Scraper(facebook_scraping)

    #logging.info("Calling firstScraper.scrape()")
    #firstscraper.scrape("coolieband")


main(sys.argv)
