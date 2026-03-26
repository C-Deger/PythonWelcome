#Strings üben 

vorname = input("Was ist dein Vorname?")

# Nachname validieren: nur Buchstaben und Bindestriche
def ist_gueltiger_nachname(name):
    name = name.strip()
    if not name:
        return False
    if name.startswith("-") or name.endswith("-"):
        return False
    if "--" in name:
        return False
    return all(char.isalpha() or char == "-" for char in name)

nachname = input("Was ist dein Nachname?")
while not ist_gueltiger_nachname(nachname):
    print("Der Nachname darf nur Buchstaben und Bindestriche enthalten (z. B. Müller-Schmidt).")
    nachname = input("Was ist dein Nachname?")

# Vorname/Name normalisieren
vorname = vorname.strip()
nachname = nachname.strip()

# Vorname in Teile splitten (z.B. "Anna Maria")
vornamen_teile = [teil for teil in vorname.split() if teil]

# Nachname kann Bindestrich enthalten (z.B. "Müller-Schmidt")
# dann behandeln wir es wie zwei Teile, damit beide Initialien genutzt werden
nachnamen_teile = []
for teil in nachname.split():
    hyphen_teile = teil.split("-")
    nachnamen_teile.extend([h for h in hyphen_teile if h])

if not vornamen_teile:
    vornamen_teile = ["?"]
if not nachnamen_teile:
    nachnamen_teile = ["?"]

initialien = "".join([teil[0].upper() for teil in vornamen_teile]) + "".join([teil[0].upper() for teil in nachnamen_teile])

while True: 
    x = input("Möchtest du deine Initialien sehen? (j/n)")
    if x.lower() == "j":
        print("Deine Initialien sind: " + initialien)
        break
    elif x.lower() == "n":
        print("Okay, vielleicht später!")
        break
    else:
        print("Das ist keine gültige Eingabe. Bitte gib 'j' oder 'n' ein.")