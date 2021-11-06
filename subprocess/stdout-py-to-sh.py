import subprocess
from subprocess import Popen, PIPE
vic='Testing 123 its the boy V-I-C'
output=subprocess.check_output("echo "+vic+"> a;cat a",shell=True)
print(output)
