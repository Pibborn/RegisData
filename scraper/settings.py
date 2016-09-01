import logging
import os

class Constants:
    FB_APP_PUBLIC_ID = "1774319916115816"
    FB_APP_SECRET_ID = "nicetry"
    FILE_ID = "prova"
    LOGGING_LEVEL = logging.INFO
    MY_DIR = os.path.expanduser('./')
    CLIENT_SECRET_FILE = 'client_secret.json'
    APPLICATION_NAME = 'Google Sheets API Python Quickstart'
    # Both are needed: the first one to create a spreadsheet, the second one to write values in it
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://spreadsheets.google.com/feeds']