#!/usr/bin/env python

from subprocess import call
import os
import time

# We want to start a server from each www directory
# where everything was built by the site-builder script

# Make sure jupyter defaults are correct (globally)

call("jupyter nbextension enable hide_input/main", shell=True)
call("jupyter nbextension enable rubberband/main", shell=True)
call("jupyter nbextension enable exercise/main", shell=True)

# This could be automated, but I am not sure how well the number of
# servers will scale ... so leave at 8 ... and hand build

# The root user is www

users   = { "www"       : ["vieps-geo-boss", 8080 ],
            "build/www1": ["vieps-geo-1",    8081 ],
            "build/www2": ["vieps-geo-2",    8082 ],
            "build/www3": ["vieps-geo-3",    8083 ],
            "build/www4": ["vieps-geo-4",    8084 ],
            "build/www5": ["vieps-geo-5",    8085 ],
            "build/www6": ["vieps-geo-6",    8086 ],
            "build/www7": ["vieps-geo-7",    8087 ],
            "build/www8": ["vieps-geo-8",    8088 ] }

# Maybe we need to quote the password in case it has odd characters in it

for dir in users.keys():
    password = users[dir][0]
    port     = users[dir][1]
    call( "cd {:s} && nohup jupyter notebook --port={:d} --ip=0.0.0.0 --no-browser\
           --NotebookApp.token={:s} --NotebookApp.default_url=/files/index.html &".format(dir, port, password), shell=True )

# Don't exit

while True:
    time.sleep(10)
