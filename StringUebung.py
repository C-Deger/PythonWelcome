#Strings üben 


# Nachname validieren: nur Buchstaben und Bindestriche
def ist_gueltiger_name(name):
    name = name.strip()
    if not name:
        return False

    # erlaubte Zeichen: Buchstaben, Leerzeichen, Bindestrich
    if not all(char.isalpha() or char in "-" or char == " " for char in name):
        return False

    # keine Bindestriche am Anfang/Ende jeder Wortkomponente
    parts = [p for p in name.split() if p]
    for part in parts:
        if part.startswith("-") or part.endswith("-"):
            return False
        if "--" in part:
            return False

    return True

vorname = input("Was ist dein Vorname?")
while not ist_gueltiger_name(vorname):
    print("Der Vorname darf nur Buchstaben und Bindestriche enthalten (z. B. Marie-Michelle).")
    vorname = input("Was ist dein Vorname?")


nachname = input("Was ist dein Nachname?")
while not ist_gueltiger_name(nachname):
    print("Der Nachname darf nur Buchstaben und Bindestriche enthalten (z. B. Müller-Schmidt).")
    nachname = input("Was ist dein Nachname?")

# Vorname/Name normalisieren
vorname = vorname.strip()
nachname = nachname.strip()

# Gemeinsame Funktion: Trennt bei Leerzeichen + Bindestrichen
# Beispiel: "Anna Maria" -> ["Anna", "Maria"]
# Beispiel: "Müller-Schmidt" -> ["Müller", "Schmidt"]
# Beispiel: "Anna Maria-Maria" -> ["Anna", "Maria", "Maria"]
def split_name_parts(name):
    return [teil for token in name.split() for teil in token.split("-") if teil]

vornamen_teile = split_name_parts(vorname)
nachnamen_teile = split_name_parts(nachname)

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