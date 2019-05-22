#!/usr/bin/scl enable rh-python36 -- python
import subprocess
import sys
import os
with open(os.devnull, 'w') as devnull:
	process = subprocess.run(["systemctl","status",str(sys.argv[1])],stdout=devnull)
	print(process.returncode)
