FROM lmoresi/unimelb-underworld-dev-base:v2016.Q2

## =============================================================
## base - image ... whatever functionality you want to provide !
## This is the underworld dev image with some altered defaults.
##
## Build this from the root directory ...
##
## % docker build -t geodynamics-course-image -f Docker/Dockerfile
##
## The dockerfile builds an image from this content, and the underworld user guide
## and serves the sample web pages and notebooks at port 8888
##
## % docker run -p 8181:8888 --name="docker-web-notebooks-test" -t lmoresi/lmoresi/docker-web-notebooks-module
## and then browse the docker VM ip address on port 8181 (for example)
##
## OR just use kitematic and click on the preview image
##
## =============================================================

## Grab (this) content from github

## Link your content to the "docs" directory at the root level of this module
## If you don't have any content then use the example content !!

RUN pip install mkdocs

RUN mkdir /geodynamics && \
    chown -R profldiablo:profldiablo /geodynamics

WORKDIR /geodynamics

## These are the build templates etc
COPY docs docs
COPY jupyter-server-theme jupyter-server-theme
COPY scripts scripts
COPY mkdocs.yml mkdocs.yml

RUN rsync -av /underworld/underworld2/docs/examples /geodynamics/docs/Underworld/     && \
    rsync -av /underworld/underworld2/docs/user_guide /geodynamics/docs/Underworld/   && \
    rsync -av /underworld/underworld2/docs/publications /geodynamics/docs/Underworld/

RUN chown -R profldiablo:profldiablo /geodynamics

USER profldiablo

RUN ./scripts/run-sitebuilder

ENV SHELL=/bin/bash

# Launch the notebook server from the Notebook directory
# but perhaps there is something else that would do this.

CMD scripts/run-jupyter -p 8888
CMD ["scripts/run-jupyter", "-p", " 8888"]
