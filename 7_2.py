filename = input("Enter file name: ")
fh = open(filename)
count = 0
avg = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    avg += float(line[20:-1].strip())
    count = count + 1 
    
print("Average spam confidence:", (avg/count))