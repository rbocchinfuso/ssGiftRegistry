# Smartsheet Clone

## Summary
Gift registry automation using the Smartsheet API.

_Note: If you have any questions or comments you can always DM me on the twitter @rbocchinfuso._

#### The Idea
Exhausted by spreadsheets, email and humans doing highly repetitive and easily automated work for which the computer was invented.

#### Looking Ahead
The approach I taken with this project which I hacked in 2016 while at OSCON will become the basis for other sentiment analysis projects.  For example, mining ServiceNow Incident and Request notes via the SNOW API and determine sentiment by incident/request, agent, company, engagement channel (phone, email, service portal), CI, etc...  Of course these projects will be written in Python.

## Requirements
- Smartsheet Python SDK: https://github.com/smartsheet-platform/smartsheet-python-sdk
- configparser: https://docs.python.org/3/library/configparser.html#module-configparser

## Usage
- Download code from GitHub
```
git clone https://github.com/rbocchinfuso/ssGiftRegistry.git
```
- Note:  If you don't have Git installed you can also just grab the zip: https://github.com/rbocchinfuso/ssGiftRegistry/archive/master.zip
- Create config.ini 
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