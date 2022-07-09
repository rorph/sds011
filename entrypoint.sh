#!/bin/bash

cd /opt
echo "-- Running SDS011..."
python sds011.py
RT=$?
echo "-- Exiting with code: $RT"
exit $?
