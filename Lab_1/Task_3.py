import sys
signs = '+-'

def checkFormula(userInput):
    indicator = True
    for userFormula in userInput:
        if userFormula.isdigit():
            indicator = True
        elif indicator and userFormula in signs:
            indicator = False
        elif indicator == True and (userFormula == '(' or ')'):
            indicator = True
        else:
            return 0
    if indicator:
        return 1
    return 0

if __name__ == "__main__":
    result = ''
    for index in range(1, len(sys.argv)):
        result += sys.argv[index]
    if checkFormula(result):
        print('(True, {})'.format(eval(result)))
    else:
        print('(False, None)')
