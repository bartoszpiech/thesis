#!/bin/sh

IP="192.168.0.164"
export FLASK_APP="server"                           # program name
export FLASK_ENV="development"                      # development -- allows to debug more easily
flask run --host=$IP 2>server_logs.txt             # run app using flask
