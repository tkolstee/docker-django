#!/usr/bin/env python3

from templatize import env_override, templatize
import socket
import re
import os

progdir = os.path.dirname(os.path.realpath(__file__))

template = progdir + '/templates/nginx.conf'
outfile = '/etc/nginx/nginx.conf'

defaults = env_override( {
  'WORKER_PROCESSES':     1024,
  'NGINX_USER':           "nginx",
  'NGINX_GROUP':          "nginx",
  'WORKER_CONNECTIONS':   5,
  'FAIL_TIMEOUT':         0,
  'CLIENT_MAX_BODY_SIZE': "4G",
  'KEEPALIVE_TIMEOUT':    5,
  'STATIC_FILES_PATH':    "current/public",
  'PROXY_BUFFERING':      True,
} )

try:
  with open('/etc/hostname', 'r') as f:
    hostname = f.read().strip()
except:
  hostname = socket.gethostname()

sn = os.environ.get('SERVER_NAMES')
if sn:
  defaults['SERVER_NAMES'] = re.split('[^a-zA-Z0-9\.]', sn)
else:
  defaults['SERVER_NAMES'] = [ hostname ]

with open(outfile, 'w') as f:
  f.write(templatize(template, defaults))

