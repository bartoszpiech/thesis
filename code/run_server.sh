#!/bin/sh

export FLASK_APP="blockchain"       # program name
export FLASK_ENV="development"      # development -- allows to debug more easily
flask run                           # run app using flask