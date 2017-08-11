import sys

def do_reduce(key, values):
    avg =  1.*sum(values)/len(values)
    print ('%.1f\t1' % avg)

prev_key = None
values = []

for line in sys.stdin:
    key, value = line.split("\t")
    if key != prev_key and prev_key is not None:
        do_reduce(prev_key, values)
        values = []
    prev_key = key
    values.append(int(value))

if prev_key is not None:
    do_reduce(prev_key,values)
