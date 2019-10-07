#!/usr/bin/env python3

import os
from templatize import env_override, templatize

progdir = os.path.dirname(os.path.realpath(__file__))

template = progdir + '/templates/run_gunicorn.sh'
outfile = '/run_gunicorn.sh'

defaults = env_override( {
  'PROJECT_NAME':        'projname',
  'WORKER_CONNECTIONS':  1,
  'NGINX_USER':           "nginx",
  'NGINX_GROUP':          "nginx",
} )

with open(outfile, 'w') as f:
  f.write(templatize(template, defaults))

os.chmod(outfile, 0o770)
