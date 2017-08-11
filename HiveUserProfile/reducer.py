#!/usr/bin/python

import sys

def do_reduce(word, values):
    return word, sum(values)

prev_key = None
values = []

for line in sys.stdin:
    key1, key2, value = line.split()
    key = key1 + "\t" + key2
    if key != prev_key and prev_key is not None:
        result_key, result_value = do_reduce(prev_key, values)
        if result_value>9:
            print(result_key + "\t" + str(result_value))
        values = []
    prev_key = key
    values.append(int(value))

if prev_key is not None:
    result_key, result_value = do_reduce(prev_key, values)
    if result_value > 9:
        print(result_key + "\t" + str(result_value))
