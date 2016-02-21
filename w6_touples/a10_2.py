import re

name = "mbox-short.txt"
handle = open(name)

d = dict()

for line in handle:
    line = line.rstrip()
    x = re.findall("^From .+([0-9][0-9]):[0-9][0-9]:[0-9][0-9]", line)
    if len(x) > 0:
        x = x[0]
        d[x] = d.get(x, 0) + 1

lst = list()
for k,v in d.items():
    lst.append((k, v))

lst.sort()

for k, v in lst:
    print k, v
