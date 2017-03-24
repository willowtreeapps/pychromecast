#!/bin/sh
python setup.py build
python setup.py install
python examples/castit.py CharlieF-Personal http://192.168.143.162:3333/board_cycle
