#!/usr/bin/env bash

rsync -a -f"+ */" -f"+ *.py" -f"- *" $(pwd)/ osmc@192.168.1.4:/home/osmc/Developer/vz_bill_watcher/
