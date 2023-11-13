# Title: Brute Force Attack - Cäser-Chiffre
# Beschreibung: Geht alle möglichkeiten für das Entschlüsseln des Cäser-Chiffre durch

import os
os.system("clear")

strText = str(input("EINGABE Geheimtext: "))

# Prüfen ob der String nur Buchstaben enthält
if strText.isalpha():
    
    # Text in Großbuchstaben umwandeln
    strText = strText.upper()

    strAusgabeText = "\nAUSGABE Klartext\n"

    for iCodeKey in range(1,25):
        strAusgabeText = strAusgabeText + str(iCodeKey).zfill(2) + ": "

        for cCurPos in strText:
            cipher = ord(cCurPos)
            cipher = cipher - iCodeKey

            if(cipher < 65):  
                cipher = cipher + 26
    
            strAusgabeText = strAusgabeText + str(chr(cipher))

        strAusgabeText = strAusgabeText + "\n"
else:
    strAusgabeText = "Ungültige Eingabe: Es sind nur Buchstaben erlaubt!"

print(strAusgabeText + "\n\n")
