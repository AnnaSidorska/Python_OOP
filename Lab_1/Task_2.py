# Write a Python-script that performs the standard math functions on the data.
# The name of function and data are set on the command line when the script is run.
# The script should be launched like this:
# >>python my_task.py add 1 2

import sys

dictionaryOfOperators = {
    'add': '+',
    'minus': '-',
    'multiply': '*',
    'divide': '/'
}
operator = dictionaryOfOperators.get(sys.argv[1])
print(eval(sys.argv[2] + operator + sys.argv[3]))

