#!/bin/bash

dieifnoproc() {
  pgrep "${1}" >/dev/null
  if [ $? != "0" ]; then
    echo "Process ${1} not running... exiting."
    exit 255
  fi
}

trap "exit 0" SIGINT SIGTERM

echo "Container entrypoint starting."

echo "Rewriting nginx configuration file..."
/configurator/nginx.conf.py
echo "Rewriting gunicorn configuration file..."
/configurator/run_gunicorn.py

echo "Starting GUnicorn..."
/run_gunicorn.sh &
echo "Starting nginx..."
nginx &

echo "Waiting..."
sleep 5

echo "Checking for processes..."
for a in nginx gunicorn; do
  dieifnoproc ${a}
done

echo "All is well. Container is up."
while true; do
  sleep 1
done
