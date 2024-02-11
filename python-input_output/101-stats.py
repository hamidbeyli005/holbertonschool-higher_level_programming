#!/usr/bin/python3
"""parse log module"""


import sys

def print_status():
    """
    Prints the total file size and the number of each HTTP status code.

    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    Output format: Prints the total file size and the number of each HTTP status code every 10 lines.
    """
    counter = 0
    size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

    for line in sys.stdin:
        parts = line.split()
        try:
            size += int(parts[-1])
            code = parts[-2]
            status_codes[code] += 1
        except IndexError:
            pass
        
        if counter == 9:
            print("File size:", size)
            for code, count in sorted(status_codes.items()):
                if count:
                    print(f"{code}: {count}")
            counter = 0
        counter += 1

    if counter < 9:
        print("File size:", size)
        for status_code, count in sorted(status_codes.items()):
            if count:
                print(f"{status_code}: {count}")


if __name__ == "__main__":
    print_status()

