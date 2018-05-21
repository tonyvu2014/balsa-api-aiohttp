#!/bin/bash

gunicorn app:web_app -b 0.0.0.0:8000 -k aiohttp.GunicornWebWorker -p /var/run/gunicorn.pid --error-logfile /var/log/balsa/error.log --access-logfile /var/log/balsa/access.log -D