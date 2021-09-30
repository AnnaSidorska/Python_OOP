import sys
numbers = '0123456789'
sign = '-+'

def formula(string):
    index = 1
    for input in string:
        if input in numbers:
            index = 1
        elif index and input in sign:
            index = 0
        elif index == 1 and (input == '(' or ')'):
            index = 10
        else:
            return 0
    if index:
        return 1
    return 0

solution = ''
for index in range(1, len(sys.argv)):
    solution += sys.argv[index]
if formula(solution):
    print('(True, {})'.format(eval(solution)))
else:
    print('(False, None)')
