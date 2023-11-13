# Implementierung der Cäsar Chiffre
# Zur GUI implementierung wird TKinter herangezogen

# Einbinden der grafischen Benutzer Oberflächen Bibliothek
import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image
import pathlib

# Einbinden von Webbrowser Funktionen
import webbrowser

# Wenn der Code verändert wird wird das Bild gedreht und entweder der Text neu ver- oder etnschlüsselt
def on_ChiffreCode_changed(event):
    imgCipherDisk = Image.open(str(pathlib.Path(__file__).parent.resolve()) + "/CipherDisk.png").resize((gui.winfo_height(),gui.winfo_height()))
    imgCipherDisk = imgCipherDisk.rotate(rngChiffreCode.get()*(365/25))
    photoCipherDisk = ImageTk.PhotoImage(imgCipherDisk)
    lblImage.configure(image=photoCipherDisk)
    lblImage.image = photoCipherDisk
    gui.update()

    if radio_Text.get() == "Klartext":
        encrypt(event)
    else:
        decrypt(event)

# Je nach Wahl mit den Optionsschaltflächen wird entweder das Klartext Feld 
# zu Eingabe freigegeben oder das Geheimtextfeld
def on_select():
    selected_option = radio_Text.get()
    if selected_option == "Klartext":
        txtKlartext.config(state=tk.NORMAL)
        txtKlartext.focus()
        txtKlartext.delete("1.0", tk.END)
        txtGeheimtext.delete("1.0", tk.END)
        txtGeheimtext.config(state = tk.DISABLED)
        gui.update() 
    else:
        txtGeheimtext.config(state=tk.NORMAL)
        txtGeheimtext.focus()
        txtGeheimtext.delete("1.0", tk.END)
        txtKlartext.delete("1.0", tk.END)
        txtKlartext.config(state = tk.DISABLED)
        gui.update() 

# Unterprogramm: Öffne den Wikipedia Artikel in einem neuen Browser Tab
def lblErklaerung_lClicked(event):
    webbrowser.open('https://de.wikipedia.org/wiki/Caesar-Verschlüsselung#Entzifferung_und_Sicherheit', new=2)

# Bereinigt den übergebene Sterings und lässt nur die großen Buchstaben bzw. das Leerzeichen zu
def cleanInput(ToClean):
    cleanedText = ""

    chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ ')
    for cCurChar in ToClean.upper():
        if cCurChar in chars:
            cleanedText = cleanedText + cCurChar

    return cleanedText

# Verschlüsselung des Textes im Feld Klartext
def encrypt(event):
    if radio_Text.get() == "Klartext":   
        resultcleanInput = cleanInput(txtKlartext.get("1.0",tk.END))
        txtKlartext.delete("1.0", tk.END)
        txtKlartext.insert(tk.END, resultcleanInput)

    cCipher = ""

    for iCurChar in resultcleanInput:
        if iCurChar == " ":
            cCipher = cCipher + chr(ord(iCurChar))
        else:
            if (ord(iCurChar) + rngChiffreCode.get()) > 90 :
                cCipher = cCipher + chr(ord(iCurChar) + rngChiffreCode.get() - 26)
            else:
                cCipher = cCipher + chr(ord(iCurChar) + rngChiffreCode.get())

    txtGeheimtext.config(state = tk.NORMAL)
    txtGeheimtext.delete("1.0", tk.END)
    txtGeheimtext.insert("1.0", cCipher)
    txtGeheimtext.config(state=tk.DISABLED)
    gui.update()

# Entschlüssellung des Textes Geheinmtext
def decrypt(event):
    if radio_Text.get() == "Geheimtext":   
        resultcleanInput = cleanInput(txtGeheimtext.get("1.0",tk.END))
        txtGeheimtext.delete("1.0", tk.END)
        txtGeheimtext.insert(tk.END, resultcleanInput)

    cCipher = ""

    for iCurChar in resultcleanInput:
        if iCurChar == " ":
            cCipher = cCipher + chr(ord(iCurChar))
        else:
            if (ord(iCurChar) - rngChiffreCode.get()) < 65 :
                cCipher = cCipher + chr(ord(iCurChar) - rngChiffreCode.get() + 26)
            else:
                cCipher = cCipher + chr(ord(iCurChar) - rngChiffreCode.get())

    txtKlartext.config(state = tk.NORMAL)
    txtKlartext.delete("1.0", tk.END)
    txtKlartext.insert("1.0", cCipher)
    txtKlartext.config(state=tk.DISABLED)
    gui.update()

# Hauptfenster erstellen und Fenster Eigenschaften einrichten
gui = tk.Tk()
gui.title("Cäsar-Verschlüsselung")
gui.geometry("800x500")
gui.resizable(False, False)
gui.update() 

# Font FETT für Labels definieren
fontLabel = font.Font(weight="bold")

# Bild: Cipher Disk auf der rechten Seite zur Hälfte Anzeigen
imgCipherDisk = Image.open(str(pathlib.Path(__file__).parent.resolve()) + "/CipherDisk.png").resize((gui.winfo_height(),gui.winfo_height()))
photoCipherDisk = ImageTk.PhotoImage(imgCipherDisk)
lblImage = tk.Label(gui, image=photoCipherDisk)
lblImage.place(x = -int(gui.winfo_height()/2) - 10)

# Einführungstext mit Hyperlink auf Wikipedia Seite
lblTitel = tk.Label(gui, anchor="w", justify="right", text="Was ist eine Cäsar Chiffre?", font=fontLabel)
lblErklaerung = tk.Label(gui, wraplength = 210, anchor="w", justify="center", \
                        text = "Die Cäsar-Verschlüsselung ist ein einfaches symmetrisches Verschlüsselungsverfahren.\n\nAls eines der einfachsten und unsichersten Verfahren dient es hauptsächlich dazu, Grundprinzipien der Kryptologie anschaulich darzustellen (Quelle: Wikipedia).\n\nZur Vereinfachung werden in dieser Implementierung nur die 26 Buchstaben des lateinischen Alphabets ohne Unterscheidung von Groß- und Kleinbuchstaben als Alphabet für Klartext und Geheimtext verwendet.\n\nSonderzeichen, Ziffern, Satzzeichen usw. werden nicht unterstützt. Leerzeichen werden beibehalten")

lblTitel.place(x = 255, y = 45)
lblErklaerung.place(x = 240, y = 45+30)

# Create a variable to hold widget values
radio_Text = tk.StringVar(value="Klartext")

# Widgets anlegen
txtKlartext = tk.Text(gui, width = 40, height = 10, highlightthickness=1)
txtGeheimtext = tk.Text(gui, width = 40, height = 10, highlightthickness=1, state = tk.DISABLED)
rngChiffreCode = tk.Scale(gui, from_ = 0, to = 25, orient=tk.HORIZONTAL,command=on_ChiffreCode_changed)
radio_Klartext = tk.Radiobutton(gui, text="Klartext", variable=radio_Text, value="Klartext", command=on_select)
radio_Geheimzahl = tk.Radiobutton(gui, text="Geheimtext", variable=radio_Text, value="Geheimtext", command=on_select)

# Event Verknüpfungen diverser Widgets
txtKlartext.bind('<KeyRelease>', encrypt)
txtGeheimtext.bind('<KeyRelease>', decrypt)
lblErklaerung.bind("<Button-1>", lblErklaerung_lClicked)

# Widgets anordnen auf der GUI
yStart = 45
xStart = 480
txtKlartext.place(x = xStart, y = yStart + 30)
txtGeheimtext.place(x = xStart, y = yStart + 270)
rngChiffreCode.place(x = xStart, y= 225, width = 280)
radio_Klartext.place(x = xStart, y = yStart)
radio_Geheimzahl.place(x = xStart, y = yStart + 240)

# Initilise the startup state of the widgets
txtKlartext.focus()

# GUI Starten und das Program als "Endlosschleife ausführen - Auf Events warten"
gui.mainloop()