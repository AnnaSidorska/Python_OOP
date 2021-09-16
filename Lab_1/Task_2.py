import sys

dictionaryOfOperators = {
    'add': '+',
    'sub': '-',
    'multiply': '*',
    'divide': '/'
}
operator = dictionaryOfOperators.get(sys.argv[1])
print(eval(sys.argv[2] + operator + sys.argv[3]))

