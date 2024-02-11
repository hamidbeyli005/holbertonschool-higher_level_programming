#!/usr/bin/python3
  
import sys


def print_log(size, status_codes):
    print('File size: {}'.format(size))
    for code in sorted(status_codes.keys()):
        print('{}: {}'.format(code, status_codes[code]))


def log_parsing():
    size = 0
    status_codes = {}
    valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    count = 0
    try:
        for line in sys.stdin:
            if count == 10:
                print_log(size, status_codes)
                count = 0
                size = 0
                status_codes = {}
            else:
                count += 1

            # space split
            line = line.split()

            size += int(line[-1])

            if int(line[-2]) in valid_codes:
                if status_codes.get(line[-2], -1) == -1:
                    status_codes[line[-2]] = 1
                else:
                    status_codes[line[-2]] += 1

        print_log(size, status_codes)

    except KeyboardInterrupt:
        print_log(size, status_codes)

log_parsing()

