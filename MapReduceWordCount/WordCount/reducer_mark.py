import sys

def do_reduce(key, values):
    avg =  1.*sum(values)/len(values)
    if avg >= 4.5:
        yield key, avg

prev_key = None
values = []

for line in sys.stdin:
    key, value = line.split("\t")
    if key != prev_key and prev_key is not None:
        for result_key, result_value in do_reduce(prev_key, values):
            print(result_key + "\t" + str(result_value))
        values = []
    prev_key = key
    values.append(int(value))

if prev_key is not None:
    for result_key, result_value in do_reduce(prev_key, values):
        print(result_key + "\t" + str(result_value))