# -*- coding: utf-8 -*-
"""
Display if an internet connection is available and, if so, whether a login is required.

Configuration parameters:
    - cache_timeout : how often to run the check (in seconds)
    - timeout : how long to wait for a response before deciding we're offline
    - format_online : what to display when online
    - format_captive : what to display when a captive portal login is required
    - format_offline : what to display when offline
    - url : connect to this url to check the connection status

@author tylermenezes
"""

from time import time
import re
import socket
import fcntl
import struct
import shlex
from subprocess import Popen, PIPE
try:
    # python3
    from urllib.request import urlopen
except:
    from urllib2 import urlopen


class Py3status:
    """
    """

    # available configuration parameters
    cache_timeout = 15
    timeout = 3
    format_online = 'Online'
    format_captive = 'Login Needed'
    format_offline = 'Offline'
    url = "http://www.apple.com/library/test/success.html"

    # internal use
    _STATE_ONLINE = 1
    _STATE_CAPTIVE = 0
    _STATE_OFFLINE = -1

    def _connection_present(self):
        process = Popen(["curl", "-s", "-o", "/dev/null", "-m", str(self.timeout), "-I", "-w", "%{http_code}", self.url], stdout=PIPE)
        (output, err) = process.communicate()
        exit_code = process.wait()

        if output == "000":
            return self._STATE_OFFLINE
        elif output == "200":
            return self._STATE_ONLINE
        else:
            return self._STATE_CAPTIVE


    def online(self, i3s_output_list, i3s_config):
        response = {
            'cached_until': time() + self.cache_timeout
        }

        connected = self._connection_present()
        if connected == self._STATE_ONLINE:
            response['full_text'] = self.format_online
            response['color'] = i3s_config['color_good']
        elif connected == self._STATE_CAPTIVE:
            response['full_text'] = self.format_captive
            response['color'] = i3s_config['color_bad']
        else:
            response['full_text'] = self.format_offline
            response['color'] = i3s_config['color_bad']

        return response

if __name__ == "__main__":
    """
    Test this module by calling it directly.
    """
    from time import sleep
    x = Py3status()
    config = {
        'color_good': '#00FF00',
        'color_bad': '#FF0000',
    }
    while True:
        print(x.online([], config))
        sleep(1)
