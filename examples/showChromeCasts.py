"""
A script to get all IPs of chromecasts the machine can see
"""

from __future__ import print_function
import time
import sys
import logging
import os

import pychromecast
import pychromecast.controllers.dashcast as dashcast

casts = pychromecast.get_chromecasts()
if len(casts) == 0:
    print("No Devices Found")
    exit()

for cast in casts:
    print(cast.device.friendly_name+": "+cast.host)
