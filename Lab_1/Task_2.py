import sys

dictionaryOfOperators = {
    'add': '+',
    'minus': '-',
    'multiply': '*',
    'divide': '/'
}
operator = dictionaryOfOperators.get(sys.argv[1])
print(eval(sys.argv[2] + operator + sys.argv[3]))

