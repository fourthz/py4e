fhand= open("mbox-short.txt")
lines = 0
for line in fhand:
  if line.startswith("From "):
    lines+=1

print("There are",lines,"lines in the file with From as the first word")