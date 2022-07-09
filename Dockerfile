FROM python:2.7.18

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC
ENV DOCKER_FLAG=1
ENV TERM=linux
ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE

# configurables
ENV OUTPUT_FN=/pm_log.csv
ENV TTY_DEV=/dev/ttyUSB0
ENV TTY_SPEED=9600
ENV BUCKET_SIZE=60

ADD sds011.py /opt/sds011.py
ADD entrypoint.sh /opt/entrypoint.sh

RUN python -m pip install pyserial && mkdir /output && chmod +x /opt/entrypoint.sh

SHELL [ "/bin/bash", "-c" ]
WORKDIR /opt
ENTRYPOINT [ "/opt/entrypoint.sh" ]