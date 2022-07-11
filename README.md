# SDS011 Dockerized Monitor

A simple sds011 sensor monitor within a docker.

This works with a simple serial connection to any sds011 sensor types.

## ENV Configurables

|variable|default|description|
|---|---|---|
|`OUTPUT_FN`|`/pm_log.csv`|Output metrics|
|`TTY_DEV`|`/dev/ttyUSB0`|Path to tty device|
|`TTY_SPEED`|`9600`|TTY device speed|
|`BUCKET_SIZE`|`1800`|Bucket size for averaging|
|`PRINT_TIME`|`1800`|Print status every number of seconds|

## Building

`./_build.sh`

## Running

`./_run.sh`
