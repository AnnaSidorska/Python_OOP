import sys

operators = ['/', '*', '-', '+']
if len(sys.argv) == 4 and sys.argv[1].isdigit() and sys.argv[2] in operators and sys.argv[3].isdigit():
    try:
        print(eval(sys.argv[1] + sys.argv[2] + sys.argv[3]))
    except ZeroDivisionError:
        print("Division on zero is impossible!")
else:
    print("Wrong input! Try again.")
