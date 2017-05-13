#!/bin/bash
# Master script.

cd "$(dirname "$0")"
source ~/.virtualenvs/matricula/bin/activate
exec uwsgi --ini uwsgi.cfg
