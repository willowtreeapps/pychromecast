"""
A script to cast a url to a chromecast
"""

from __future__ import print_function
import time
import sys
import logging
import os

import pychromecast
import pychromecast.controllers.dashcast as dashcast

if len(sys.argv) != 3:
    print("Wrong args.")
    print("Usage: python castit.py <castname> <url>")
    sys.exit(1)

castName = sys.argv[1];
url = sys.argv[2];

casts = pychromecast.get_chromecasts()
if len(casts) == 0:
    print("No Devices Found")
    exit()

cast = next(cc for cc in casts if cc.device.friendly_name == castName)
# cast = next(cc for cc in casts if cc.device.friendly_name == "Inara")
cast.wait();
#This isn't working v
if not cast.is_idle:
    print("Cast is currently showing something - exiting")
    sys.exit()

cast.start_app("DCCDFF7E")
print()
print(cast.device)
time.sleep(1)
print()
print(cast.status)
print()

time.sleep(10)

dc = dashcast.DashCastController()
cast.register_handler(dc)
dc.request_dash(url)
time.sleep(10)