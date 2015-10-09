# py3-online

py3-online is a simple internet tester for [py3status](https://github.com/ultrabug/py3status).

py3-online makes a few changes from the `online_status` module which is distributed with py3status:

- Executes `curl` instead of using urlopen in Python, which fixes some [network access bugs](http://stackoverflow.com/questions/33042478/socket-getaddrinfo-fails-if-network-started-offline)
  which prevent it from running properly if you aren't connected to ethernet at startup.
- Checks for redirects (which would be served for a captive portal). If it finds one, it displays a different (configurable) message to indicate that a login is required.

## Installing

Copy [online.py](online.py) to your modules directory (by default `.i3/py3modules`) and add `online` to your `i3status/config` file.
