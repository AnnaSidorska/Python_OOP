import os
import timeit
import random


def gen_file():
    with open("my_file.txt", "w") as f:
        size = os.path.getsize("my_file.txt")
        while size < 1400000:
            f.write(str(random.randint(0, 100)) + "\n")


def read_lines():
    s = 0
    with open("my_file.txt", "r") as f:
        u_lines = f.readlines()
        for i in u_lines:
            if i.strip().isdigit():
                s += int(i.strip())


def lines():
    s = 0
    with open("my_file.txt", "r") as f:
        for i in f:
            if i.strip().isdigit():
                s += int(i.strip())


def generator():
    s = sum(int(i.strip()) for i in open("my_file.txt") if i.strip().isdigit())


def main():
    #gen_file()
    print(timeit.timeit(read_lines, number=1))
    print(timeit.timeit(lines, number=1))
    print(timeit.timeit(generator, number=1))


main()
