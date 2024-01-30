#!/usr/bin/python3
def uniq_add(my_list=[]):
    newlist = []
    for a in mylist:
        if a not in newlist:
            newlist.append(a)
    return sum(newlist)
