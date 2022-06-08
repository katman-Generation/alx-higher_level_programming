#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    New_list = (list(map(lambda x: x * number, my_list)))
    return New_list
