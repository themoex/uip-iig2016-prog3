preg = input("Preguntale a Juan:")

if preg.endswith('?'):
    print ("Ofi")

elif preg >= 'A' and preg <= 'Z':
    print ("Chillea")

elif (len(preg)==0):
    print ("Mmm")
else:
    print ("Me da igual")