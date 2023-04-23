#!/bin/sh
export FLASK_APP=./vf-hack/index.py
pipenv run flask --debug run -h 0.0.0.0