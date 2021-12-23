#!/bin/sh

export FLASK_APP="server"       # program name
export FLASK_ENV="development"      # development -- allows to debug more easily
flask run --host=192.168.0.143                            # run app using flask
