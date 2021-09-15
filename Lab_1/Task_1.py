# Write a Python-script that performs simple arithmetic operations: '+', '-', '*', '/'.
# The type of operator and data are set on the command line when the script is run.
# The script should be launched like this:
# >>python my_task.py 1 * 2

import sys
print(eval(sys.argv[1] + sys.argv[2] + sys.argv[3]))
