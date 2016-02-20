fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()

def isInList(word, lst):
    if word in lst:
        return True
    else:
        return False


fh = open("romeo.txt")

for line in fh:
    words = line.split()
    for word in words:
        if not isInList(word, lst):
            lst.append(word)
        else:
            continue

lst.sort()
print lst
