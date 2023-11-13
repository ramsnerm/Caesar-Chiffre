# Title: Decrypt - Cäser-Chiffre
# Beschreibung: Entschlüsseln von bestimmten Text mit dem richtigen Schlüssel

import os
os.system("clear")

strText = str(input("EINGABE Geheimtext: "))

# Prüfen ob der String nur Buchstaben enthält
if strText.isalpha():
    
    # Text in Großbuchstaben umwandeln
    strText = strText.upper()

    iCodeKey = int(input("Entschlüsselungscode (1-25): "))

    strAusgabeText = ""

    if iCodeKey < 1 or iCodeKey > 25:
        strAusgabeText = "Ungültige Eingabe: Der Code muss > 0 und < 26 sein."
    else:
        strAusgabeText = "AUSGABE Klartext: "

        for cCurPos in strText:
            cipher = ord(cCurPos)
            cipher = cipher - iCodeKey

            if(cipher < 65):  
                cipher = cipher + 26
    
            strAusgabeText = strAusgabeText + str(chr(cipher))
else:
    strAusgabeText = "Ungültige Eingabe: Es sind nur Buchstaben erlaubt!"

print(strAusgabeText + "\n\n")
