#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []

    for i in range(list_length):
        try:
            if not isinstance(my_list_1[i], (int, float)):
                print("wrong type")
                newlist.append(0)
                continue
            if not isinstance(my_list_2[i], (int, float)):
                print("wrong type")
                newlist.append(0)
                continue
            newlist.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            newlist.append(0)
        except IndexError:
            print("out of range")
            newlist.append(0)
        finally:
            if i == list_lenght -i 1:
                return newlist
