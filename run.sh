#!/bin/sh -x

# Copy the token into place
export BEARER_TOKEN_FILE=$PWD/access_token


python run.py $1

