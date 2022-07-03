fname = input("Enter file name: ")
fh = open(fname)
counts = dict()
for line in fh:
    line.rstrip()
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
        words = line.split()
        word = words[1]
        counts[word] = counts.get(word,0) + 1
maxadd = None
maxval = None
for word, count in counts.items():
    if maxval is None or count > maxval:
        maxadd = word
        maxval = count
print (maxadd, maxval)
