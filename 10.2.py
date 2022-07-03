name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts= dict()
for line in handle:
        line.rstrip()
        if line.startswith('From:'):
            continue
        if line.startswith('From'):
            words = line.split()
            time = words[5]
            hours = time.split(':')
            hour=hours[0]
            counts[hour] = counts.get(hour,0) + 1
temp = []
for k,v in counts.items():
    temp.append((k,v))
temp=sorted(temp)
for k,v in temp:
    print(k, v)
