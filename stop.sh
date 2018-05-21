#!/bin/bash

kill -9 $(cat /var/run/gunicorn.pid)