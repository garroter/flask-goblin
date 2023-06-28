#!/usr/bin/env bash
gunicorn --access-logfile - --error-logfile -  -b 0.0.0.0:5000  run:app --timeout 360

