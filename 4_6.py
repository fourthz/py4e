def computepay (hours, rate):
  if hours <= 40:
    pay = (hours * rate) 
  else:
    pay = (40 * rate) + (hours-40)*rate*1.5 
  return pay
