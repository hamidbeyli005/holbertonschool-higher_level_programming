#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            count += 1
            print(my_list[i], end='')
    except IndexError:
        pass
    finally:
        print()
    return count
