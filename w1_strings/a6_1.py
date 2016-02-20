text = "X-DSPAM-Confidence:    0.8475";

# 0 index
di = text.find("0");
d = float(text[di:]);

print(d);
