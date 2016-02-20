# Use words.txt as the file name
fname = raw_input("Enter file name: ");

try:
    fh = open(fname);
    for line in fh:
        print line.rstrip().upper();

except:
    print "File not found";
