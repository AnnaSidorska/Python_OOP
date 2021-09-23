import sys
operators = ['+', '-']


def check_formula(user_input):
    """ Checks user input for the accuracy. """

    formula_flag = True
    for current_element in user_input:
        if current_element.isdigit():
            formula_flag = True
        elif formula_flag and current_element in operators:
            formula_flag = False
        else:
            return 0
    if formula_flag:
        return 1
    return 0


if __name__ == "__main__":
    result = ''
    for index in range(1, len(sys.argv)):
        result += sys.argv[index]
    if check_formula(result):
        print('(True, {})'.format(eval(result)))
        """ Calculate the result if it is correct. """

    else:
        print('(False, None)')
