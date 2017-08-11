#!/usr/bin/python

import sys

def do_reduce(word, val1, val2, val3, val4):
    return word, max(val1), max(val2), max(val3), max(val4)

prev_key = None
values1 = []
values2 = []
values3 = []
values4 = []

for line in sys.stdin:
    key, v1, v2, v3, v4 = line.split()
    if key != prev_key and prev_key is not None:
        result_key, r_v1, r_v2, r_v3, r_v4 = do_reduce(prev_key, values1, values2, values3, values4)
        print(result_key + "\t" + str(r_v1) + "\t" + str(r_v2) + "\t" + str(r_v3) + "\t" + str(r_v4))
        values1 = []
        values2 = []
        values3 = []
        values4 = []
    prev_key = key
    values1.append(int(v1))
    values2.append(int(v2))
    values3.append(int(v3))
    values4.append(int(v4))

if prev_key is not None:
    result_key, r_v1, r_v2, r_v3, r_v4 = do_reduce(prev_key, values1, values2, values3, values4)
    print(result_key + "\t" + str(r_v1) + "\t" + str(r_v2) + "\t" + str(r_v3) + "\t" + str(r_v4))
