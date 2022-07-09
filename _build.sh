#!/bin/bash

TAG=${TAG-z3n666/sds011:latest}

docker build . -t ${TAG} -f Dockerfile
RT=$?

if [ "$RT" -eq "0" ] ; then
    echo "-- Built: $TAG"
else
    echo "-- Error building: $TAG"
    exit 1
fi