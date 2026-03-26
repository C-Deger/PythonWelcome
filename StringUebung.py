#Strings üben 

vorname = input("Was ist dein Vorname?")
nachname = input("Was ist dein Nachname?")

while True: 
    try: 
        x = input("Möchtest du deine Initialien sehen? (j/n)")
        if x == "j" or x == "J":
            print("Deine Initialien sind: " + vorname[0] + nachname[0])
            break
        elif x == "n" or x == "N":
            print("Okay, vielleicht später!")
            break
    except:
        print("Das ist keine gültige Eingabe. Bitte gib 'j' oder 'n' ein.")