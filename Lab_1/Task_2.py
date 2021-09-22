import sys

dictionaryOfOperators = {
    'add': '+',
    'sub': '-',
    'multiply': '*',
    'divide': '/'
}
operator = dictionaryOfOperators.get(sys.argv[1])
if len(sys.argv) == 4 and sys.argv[2].isdigit() and sys.argv[3].isdigit():
    try:
        print(eval(sys.argv[2] + operator + sys.argv[3]))
    except ZeroDivisionError:
        print("Division on zero is impossible!")
else:
    print("Wrong input! Try again.")


