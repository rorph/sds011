#!/bin/bash

TAG=${TAG-z3n666/sds011:latest}
NAME=${NAME-sds011}
OUTPUT_FN=${OUTPUT_FN-/mnt/docker/pm_log.csv}

echo "-- Running TAG: ${TAG} as ${NAME}"

docker kill ${NAME} &> /dev/null
docker rm ${NAME} &> /dev/null

touch ${OUTPUT_FN}
docker run -d --privileged -e BUCKET_SIZE=1800 -e PRINT_TIME=1800 --restart unless-stopped -v ${OUTPUT_FN}:/output/pm_log.csv --name ${NAME} ${TAG}