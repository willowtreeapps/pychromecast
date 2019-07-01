#!/bin/bash
###
#  This script scans for local chromecasts on the network and shows their IPs.
#  This does depend on pipenv being installed on your local system.
#
#  NOTE - Due to how mDNS works this script needs to be run in the buildings the chromecasts are on
#  NOTE - Also - due to the inconsistency of mDNS you might need to run this multiple times before you get results
###
pipenv run python examples/showChromeCasts.py
