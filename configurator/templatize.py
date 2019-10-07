#!/usr/bin/env python3

import os
from jinja2 import Template

def env_override(defaults):
  for x in list(defaults.keys()):
    y = os.environ.get(x)
    if y:
      defaults[x] = y
  return defaults

def templatize(templatefile, defaults):
  with open(templatefile, 'r') as f:
    tmpl = Template(f.read())
  return (tmpl.render(**defaults))
