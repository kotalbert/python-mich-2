"""

9.4 Write a program to read through the mbox-short.txt and figure out who has
the sent the greatest number of mail messages. The program looks for 'From '
lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to
a count of the number of times they appear in the file. After the dictionary is
produced, the program reads through the dictionary using a maximum loop to find
the most prolific committer.
"""

import re

# name = raw_input("Enter file:")
# if len(name) < 1:
name = "mbox-short.txt"
h = open(name)

d = dict()

for line in h:
    line = line.rstrip()
    x = re.findall('^From *([A-Za-z1-9.]+@[A-Za-z1-9.]+)', line)
    if len(x) > 0:
        x = x[0]
        d[x] = d.get(x, 0) + 1

m = 0
for k in d:
    if d[k] > m:
        m = d.get(k)
        kMax = k
print kMax, d[kMax]
