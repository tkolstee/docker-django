#!/bin/bash

if [ ! -d /run ]; then mkdir /run; fi
chown {{NGINX_USER}}:{{NGINX_GROUP}} /run
chmod 0775 /run

cd /django

exec gunicorn {{PROJECT_NAME}}.wsgi:application \
  --name {{PROJECT_NAME}} \
  --workers {{WORKER_CONNECTIONS}} \
  --user {{NGINX_USER}} \
  --bind=unix:/run/gunicorn.sock
