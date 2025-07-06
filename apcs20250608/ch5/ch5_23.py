import locale

print(locale.getpreferredencoding())
fin1 = open("Poem.txt")
line = fin1.readline()
while line:
    print(line,end="")
    line = fin1.readline()

fin2 = open("PoemUTF8.txt",encoding="utf-8")
line = fin2.readline()
while line:
    print(line,end="")
    line = fin2.readline()
