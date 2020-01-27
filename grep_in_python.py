search = ".jpg"
f = "electronics395.txt"

file = open(f, 'r')
for line in file:
    if re.search(search, line):
        print(line)