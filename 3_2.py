ho = input('Enter Hours:')
ra = input('Enter Rate:')

try:
  hours = float(ho)
  rate = float (ra)
  if hours <= 40:
    pay = hours * rate
  else:
    pay = ((hours - 40) * (1.5 * rate)) + (40 * rate)
  print ('Pay =', pay)
except:
    print('Error, please enter numeric input')
