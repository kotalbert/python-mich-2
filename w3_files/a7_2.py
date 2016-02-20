# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)

def getConfidence(line):
    di = line.find("0");
    return float(line[di:]);

s = 0.0;
c = 0;

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    s += getConfidence(line);
    c += 1;

print "Average spam confidence: %.12g" %(s/c);

print "Done"
