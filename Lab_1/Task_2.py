<<<<<<< HEAD
import sys

dictionaryOfOperators = {
    'add': '+',
    'minus': '-',
    'multiply': '*',
    'divide': '/'
}
operator = dictionaryOfOperators.get(sys.argv[1])
print(eval(sys.argv[2] + operator + sys.argv[3]))

=======
import sys

dictionaryOfOperators = {
    'add': '+',
    'minus': '-',
    'multiply': '*',
    'divide': '/'
}
operator = dictionaryOfOperators.get(sys.argv[1])
print(eval(sys.argv[2] + operator + sys.argv[3]))

>>>>>>> 3323380d7fef3aaa5571d1013bb3baacc558667d
