import os
import subprocess
process = subprocess.run(["systemctl","status","httpd"])
print(process.returncode)
