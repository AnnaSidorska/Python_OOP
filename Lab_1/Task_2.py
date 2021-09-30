import sys

dictionaryOfOperators = {
    'add': '+',
    'sub': '-',
    'multiply': '*',
    'divide': '/'
}
""" Makes a dictionary of the operators. """

operator = dictionaryOfOperators.get(sys.argv[1])
""" Get the right operator in the dictionary. """

if len(sys.argv) == 4 and sys.argv[2].isdigit() and sys.argv[3].isdigit():
    """ Checks if the input is right and have 4 arguments. """
    
    try:
        print(eval(sys.argv[2] + operator + sys.argv[3]))
        """ Prints the result. """
        
    except ZeroDivisionError:
        print("Division on zero is impossible!")
else:
    print("Wrong input! Try again.")


