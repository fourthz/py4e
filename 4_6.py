def computepay (hours, rate):
  if hours <= 40:
    pay = (hours * rate) 
  else:
    pay = (40 * rate) + (hours-40)*rate*1.5 
  return pay

def hoursnum ():
  string=True
  while string:
    hours = input('Hours: ')
    try:
      hours = float(hours)
      string = False
      return hours
    except:
      print ('Error, please enter a number, you great supine protoplasmic invertebrate jelly!')
 
def ratenum ():
  string=True
  while string:
    rate = input('Rate: ')
    try:
      rate = float(rate)
      string = False
      return rate
    except:
      print ('Error, please enter a number you absoloute degenrate scum!')
    
hours=hoursnum ()
rate=ratenum ()
paycheck = computepay (hours, rate)
print ("Your pay is " + str(paycheck))

