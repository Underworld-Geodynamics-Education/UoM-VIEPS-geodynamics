#!/bin/sh

# Docker build command for the base underworld image
# Currently we are at version 2017.03.29

# 1.05 includes the jupyter notebook extensions but not litho1pt0 and stripy
# The latter are built at the next level up (using the modules in this repo)


set -e
cd $(dirname "$0")/..

docker build -f Docker/Dockerfile-unimelb-underworld-dev-base -t lmoresi/unimelb-debian-uw:2017.03.29 .
