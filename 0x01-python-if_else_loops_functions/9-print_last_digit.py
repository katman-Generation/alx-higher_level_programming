#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        lastd = number % 10
    if number < 0:
        lastd = (number % -10) * -1
    print("{:d}".format(lastd), end='')
    return lastd
