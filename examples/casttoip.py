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

print("Looking for chromecast "+castName)
print()
# info = ServiceInfo("_http._tcp.local.", "Paul's Test Web Site._http._tcp.local.", socket.inet_aton("10.0.1.2"), 80, 0, 0, desc, "ash-2.local.")

# cast = pychromecast._get_chromecast_from_host(('192.168.73.37', 8009, UUID('7c7233cc-9ea0-979d-af53-eae68dcb6ab9'), 'Chromecast', 'Inara'))
cast = pychromecast.Chromecast(castName)
# if len(casts) == 0:
#     print("No Devices Found")
#     exit()

# cast = next(cc for cc in casts if cc.device.friendly_name == castName)
# cast = next(cc for cc in casts if cc.device.friendly_name == "Inara")
cast.wait();
print("Connected:")
print(cast.device)
print(cast.status)
print()

#This isn't working
# if cast.app_id != "E8C28D3C":
if not cast.is_idle:
    print("Cast is currently showing something - exiting")
    sys.exit()

print("Starting Dashcast")
cast.start_app("DCCDFF7E")
time.sleep(5)
print("Sending url: "+url)
dc = dashcast.DashCastController()
cast.register_handler(dc)
dc.request_dash(url)