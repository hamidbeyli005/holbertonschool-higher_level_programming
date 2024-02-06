#!/usr/bin/python3
"""7-add_item module"""


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

json_name = 'add_item.json'

try:
    my_list = load_from_json_file(json_name)
except Exception as ex:
    my_list = []
for i in sys.argv[1:]:
    my_list.append(i)

save_to_json_file(my_list, json_name)
