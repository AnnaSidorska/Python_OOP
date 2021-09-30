import sys

operators = ['/', '*', '-', '+']
""" Makes a list of the operators. """

if len(sys.argv) == 4 and sys.argv[1].isdigit() and sys.argv[2] in operators and sys.argv[3].isdigit():
    """ Checks if the input is right and have 4 arguments. """
    
    try:
        print(eval(sys.argv[1] + sys.argv[2] + sys.argv[3]))
        """ Prints the result. """
        
    except ZeroDivisionError:
        print("Division on zero is impossible!")
else:
    print("Wrong input! Try again.")
