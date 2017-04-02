#!/bin/sh

# Docker build command for the base python image
# Currently we are at version 1.05

# 1.05 includes the jupyter notebook extensions but not litho1pt0 and stripy


set -e
cd $(dirname "$0")/..

docker build -t lmoresi/docker-vieps-geo:2017 -f Docker/Dockerfile-unimelb-uw  .
docker build -t lmoresi/docker-vieps-geo-8user:2017 -f Docker/Dockerfile-unimelb-uw8user  .
