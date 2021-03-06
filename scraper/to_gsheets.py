import os
import gspread
import csv
import time

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

def prepare_comment_row(wk, cell_row, status_csv_line, comment_csv_line):
    # we always start from the first column
    cell_column = 1
    # prepare an empty cell row list
    cell_row_list = []

    status_string = status_csv_line[1]
    comment_status_id = comment_csv_line[1]

    # first cell on each row is the status identifier
    status_id_cell = wk.cell(cell_row, cell_column)
    status_id_cell.value = comment_csv_line[1]
    cell_row_list.append(status_id_cell)
    cell_column += 1

    # then what is written on the status the comment was written under
    status_string_cell = wk.cell(cell_row, cell_column)
    status_string_cell.value = status_string
    cell_row_list.append(status_string_cell)
    cell_column += 1

    # then the actual comment string
    comment_cell = wk.cell(cell_row, cell_column)
    comment_cell.value = comment_csv_line[3]
    cell_row_list.append(comment_cell)
    cell_column += 1

    # some time information
    time_tokens = comment_csv_line[5].split(" ")
    comment_date = time_tokens[0]
    comment_hour = time_tokens[1]
    date_cell = wk.cell(cell_row, cell_column)
    date_cell.value = comment_date
    cell_row_list.append(date_cell)
    cell_column += 1

    hour_cell = wk.cell(cell_row, cell_column)
    hour_cell.value = comment_hour
    cell_row_list.append(hour_cell)
    cell_column += 1

    return cell_row_list


def csv_to_gsheet(wk, csv_file):
    # TODO: set up settings.py so that this is automatically understood
    status_csv = open(Constants.MY_DIR + 'LIntraprendente_facebook_statuses.csv', 'r')
    comment_csv = open(Constants.MY_DIR + 'LIntraprendente_facebook_comments.csv', 'r')
    status_csv_reader = csv.reader(status_csv)
    comment_csv_reader = csv.reader(comment_csv)

    # skipping csv headers
    next(status_csv_reader)
    next(comment_csv_reader)
    comment_csv_line = next(comment_csv_reader)

    cell_column = 1
    cell_row = 1
    cell_row_list = []

    i = 0
    for status_csv_line in status_csv_reader:
        status_id = status_csv_line[0]
        status_string = status_csv_line[1]

        comment_status_id = comment_csv_line[1]

        # we should not move on from this loop until
        # we processed each comment that is relative to the
        # status that has status_id as an identifier
        while comment_status_id == status_id:
            cell_row_list = prepare_comment_row(wk, cell_row, status_csv_line, comment_csv_line)

            wk.update_cells(cell_row_list)

            # set up loop for next iteration
            cell_row_list = []
            cell_row += 1

            comment_csv_line = next(comment_csv_reader)
            comment_status_id = comment_csv_line[1]

def tic():
    global startTime_for_tictoc
    startTime_for_tictoc = time.time()

def toc():
    import time
    if 'startTime_for_tictoc' in globals():
        print ("Elapsed time is " + str(time.time() - startTime_for_tictoc) + " seconds.")
    else:
        print ("Toc: start time not set")