cen = float(input("Introduzca la cantidad de moneda:"))

eur = 0.8965
yen = 101.5744
bp = 0.7702
mxn = 19.7843

dolar = (cen/100)

a = dolar*eur
b = dolar*yen
c = dolar*bp
d = dolar*mxn

print("Convertir a euro:" + str(a))
print("Convertir a yen:" + str(b))
print("Convertir a bp:" + str(c))
print("Convertir a mxn:" + str(d))
