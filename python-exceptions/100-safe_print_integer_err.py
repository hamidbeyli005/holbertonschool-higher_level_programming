#!/usr/bin/python3
def safe_print_integer_err(value):
    if isinstance(value, str):
        return True
    else:
        try:
            print("{:d}".format(value))
            return True
        except Exception as ex:
            print(ex)
            return False
