#!/usr/bin/env python

"""ssShare.py: Shares sheets based on user to sheet map csv input file."""

__author__ = "Rich Bocchinfuso"
__copyright__ = "Copyright 2020, A Plannet far far away"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Rich Bocchinfuso"
__email__ = "rbocchinfuso@gmail.com"
__status__ = "beta"

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
    print ('...Sharing sheet ' + sheetID + ' with ' + name + ' <' + email + '>')
    response = smartsheet_client.Sheets.share_sheet(
      sheetID,                                  # sheet_id from csv
      smartsheet.models.Share({
        'access_level': 'EDITOR',
        'email': email,
        'subject': name + ' Gift Registry',
        'message': 'Hello, ' + name + ', you are receiving this automated message from Smartsheet because the previous process for requesting and policing the gift registry lacked a certain level of elegance, and it troubled me to see a human being doing a job so well suited for a computer.  Fueled by frustration and a lack of nostalgia for the quill, I volunteered my services to add a little elegance by empowering the computer to execute this repetitive task with precision and efficiency.\n\nPlease take a few minutes and complete your ' + config['local']['period'] + ' gift registry, your registry needs to be completed by COB Friday, January 24, 2020.  Automated reminders are enabled to ensure compliance.\n\nNOTE: If you have no gifts to report please make a single entry in your Gift Registry selecting "Ack of No Gifts".\n\nThis is release 0.1, and it has not exactly undergone extensive QA and UAT, so if you encounter any issues, I would appreciate you logging them in the git repo (https://github.com/rbocchinfuso/ssGiftRegistry/issues) or email me at richard.bocchinfuso@computacenter.com.\n\nThanks\n-Rich'
      }),
      True                                      # sendEmail
    )

