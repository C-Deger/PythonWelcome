#Schaltjahre berechnen
#Schaltjahre abfragen
while True:
    try:
        jahr = int(input("Gib ein Jahr ein: "))
        break
    except ValueError:
        print("Das ist kein Integer, bitte versuche es erneut.")

#Schaltjahr berechnen
if jahr % 4 == 0 and (jahr % 100 != 0 or jahr % 400 == 0):
    print(jahr, "ist ein Schaltjahr.")
else:
    print(jahr, "ist kein Schaltjahr.")
