str = 'X-DSPAM-Confidence: 0.8475'
atpos = str.find(':')
var = str [atpos+1:]
var = float(var)
print ('This is a floating point number %g.' % (var))
