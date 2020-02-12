# Smartsheet Gift Registry

## Summary
Gift registry automation using the Smartsheet API.

_Note: If you have any questions or comments you can always DM me on the twitter @rbocchinfuso._

#### Why
Exhausted by spreadsheets, email and humans doing highly repetitive and easily automated work for which the computer was invented.

#### How
- Uses smartsheet api to clond individual gift registries from a gift registry gold copy
- Uses _peeps.txt (peeps.example)_ to create individual gift registries
- Uses _user_sheet_map.csv (user_sheet_map.example)_ to map user sheets to sheet ids and urls

#### What
- Clones gift registry smartsheet from gold copy
- Shares gift registry smartsheet with appropriate person
- Sends emails to users with link to gift registry sheet to update gift registry sheets
- Sends reminders _(via cron job)_ to users with link to update gift registry 

#### Todo
- Check to see if the sheet has been updated by the user and use exeception based reminders


## Requirements
- Smartsheet Python SDK: https://github.com/smartsheet-platform/smartsheet-python-sdk
- configparser: https://docs.python.org/3/library/configparser.html#module-configparser

## Usage
- Download code from GitHub
```
git clone https://github.com/rbocchinfuso/ssGiftRegistry.git
```
- Note:  If you don't have Git installed you can also just grab the zip: https://github.com/rbocchinfuso/ssGiftRegistry/archive/master.zip

- Create config.ini, peeps.txt and user_sheet_map.csv files from .example files

- Clone Smartsheet from template
```
python ssClone.py
```
- Share cloned smatsheets
```
python ssShare.py
```
- Configure reminder cron job
```
python ssRemind.py
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request ツ

## History
-  version 0.1 (initial release) - 2020/01/21

## Credits
Rich Bocchinfuso <<rbocchinfuso@gmail.com>>

## License
MIT License

Copyright (c) [2020] [Richard J. Bocchinfuso]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.