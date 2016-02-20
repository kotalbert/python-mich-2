# fname = raw_input("Enter file name: ")
# if len(fname) < 1 : fname = "mbox-short.txt"

fname = "mbox-short.txt"
fh = open(fname)
count = 0


def getMail(line):
    lst = line.split()
    return lst[1]


for line in fh:
    if line.startswith("From "):
        count += 1
        print getMail(line)

print "There were", count, "lines in the file with From as the first word"
