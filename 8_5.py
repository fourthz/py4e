
fileName = input("Enter the fileName:")
fileData = open(fileName, 'r') 
lines = fileData.readlines() 
i=0 
count=0
while(i<len(lines)): 
   words = lines[i].split(" ") 
   if(words[0]=='From'): 
       count=count+1 
       print(words[1])
   i=i+1
print ("There were",count,"lines in the file with From as the first word")