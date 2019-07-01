#!/bin/bash
###
#  This script sets up pychromecast locally
#  This does depend on pipenv being installed on your local system.
###
pipenv run pip install -r requirements.txt
pipenv run python setup.py build
pipenv run python setup.py install
