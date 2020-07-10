sco=input("Please type a sco between 0.0 and 1.0:")
try:
  float(sco)
  if float(sco) >= 0.9 and float(sco) <= 1.0:
    print("A")
  elif float(sco) >= 0.8 and float(sco) <= 0.9:
    print("B")
  elif float(sco) >= 0.7 and float(sco) <= 0.8:
    print("C")
  elif float(sco) >= 0.6 and float(sco) <= 0.7:
    print("D")
  elif float(sco) > 0 and float(sco) <= 0.6:
    print("F")
  else:
    print("Bad score.  Please run the program again.")
except:
    print("Bad score.  Please run the program again.")
  
