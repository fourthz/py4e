fhand = open("romeo.txt")
words =[]
for line in fhand:
  llist = line.lower().split(" ")
  for word in llist:
    print(word)
    word = word.strip()
    if word not in words:
      words.append(word)
print(sorted(words))
