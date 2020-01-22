#!/usr/bin/env python

"""ssRemind.py: Sends gift registry to reminders."""

__author__ = "Rich Bocchinfuso"
__copyright__ = "Copyright 2020, A Plannet far far away"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Rich Bocchinfuso"
__email__ = "rbocchinfuso@gmail.com"
__status__ = "dev"

import smartsheet, configparser
import csv

# read and parse config file
config = configparser.ConfigParser()
config.read('config.ini')
config.sections()

smartsheet_client = smartsheet.Smartsheet(config['smartsheet']['token'])

fh = csv.reader(open(config['local']['user_sheet_map']), delimiter=',')
for line in fh:
    name = line[0]
    email = line[1]
    sheetID = line[2]
    url = line[3]
    print ('...Sending gift registry sheet (' + sheetID + ') reminder to ' + name + ' <' + email + '>')
    response = smartsheet_client.Sheets.send_sheet(
      sheetID,           # sheet_id
      smartsheet.models.SheetEmail({
        'send_to': [
          smartsheet.models.Recipient({'email': email})
        ],
        'subject': name + ' Gift Registry Reminder',
        'message': 'Hello, ' + name + ', this is a reminder to complete your ' + config['local']['period'] + ' gift registry.\n\n' + name + ', if you have not completed your ' + config['local']['period'] + ' gift registry, please do so by clicking the following URL:\n' + url + '\n\nMy apoogies ' + name + ', if you have already completed your ' + config['local']['period'] + ' gift registry, the logic to only pester those who have not completed their regitsty is not yet complete.\n\nPlease log any issues in the git repo () or email me at richard.bocchinfuso@computacenter.com.\n\nThanks\n-Rich',
        'cc_me': False,
        'format': 'PDF',
        'format_details': smartsheet.models.FormatDetails({
          'paper_size': 'Legal'
        })
      })
    )

