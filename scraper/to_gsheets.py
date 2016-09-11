import os
import gspread

from apiclient import discovery
from oauth2client import client, file, tools
from httplib2 import Http


try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

from .settings import Constants
import logging

"""
Taken from http://stackoverflow.com/questions/12741303/creating-empty-spreadsheets-in-google-drive-using-drive-api-in-python
"""
def get_credentials():
    credential_path = os.path.join(Constants.MY_DIR, 'google-apis-credentials.json')
    store = file.Storage(credential_path)
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(Constants.CLIENT_SECRET_FILE, Constants.SCOPES)
        if flags:
            creds = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            creds = tools.run(flow, store)
        logging.info("New GAPI credentials stored at " + credential_path)
    else:
        logging.info("Credentials @ " + credential_path + " were found valid.")
    return creds

def create_spreadsheet(creds, name):
    SHEETS = discovery.build('sheets', 'v4', http=creds.authorize(Http()))
    data = {'properties': {'title': name}}
    sheet = SHEETS.spreadsheets().create(body=data).execute()
    return sheet

def get_worksheet(creds, name, number):
    gc = gspread.authorize(creds)
    wk = gc.open(name).sheet1
    return wk

def hello_worksheet(wk):
    wk.update_acell('A2', 'Hi!')