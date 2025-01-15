#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            i = "{}".format("FizzBuzz")
        elif i % 3 == 0:
            i = "{}".format("Fizz")
        elif i % 5 == 0:
            i = "{}".format("Buzz")
        else:
            i
        print(f"{i}", end=' ')
