#!/usr/bin/env python

"""ssClone.py: Clones Smartsheets from a source Smartsheet Template."""

__author__      = "Rich Bocchinfuso"
__copyright__   = "Copyright 2020, A Plannet far far away"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Rich Bocchinfuso"
__email__ = "rbocchinfuso@gmail.com"
__status__ = "beta"

import smartsheet, configparser

# read and parse config file
config = configparser.ConfigParser()
config.read('config.ini')
config.sections()

smartsheet_client = smartsheet.Smartsheet(config['smartsheet']['token'])

fh = open(config['local']['peeps'])
for line in fh:
    print('Cloining Gift Registry Template to ' + line.rstrip() + ' Gift Registry')
    inc_list = ['data']                                                # include sheet data in clone
    response = smartsheet_client.Sheets.copy_sheet(
      int(config['smartsheet']['template_sheet_id']),                  # sheet_id
      smartsheet.models.ContainerDestination({
        'destination_type': 'folder',                                  # folder, workspace, or home
        'destination_id': int(config['smartsheet']['folder_id']),      # folder_id
        'new_name': line + ' Gift Registry'
      }),
      include = inc_list
    )    
fh.close()
