# Detta Python-script genererar slumpmässiga lösenord bestående av både siffror, bokstäver och specialtecken. 
# Lösenordet kontrolleras mot haveIbeenpwned.com för att se om det har upptäckts i kända läckor.



print()
print()
print("    \033[1;95m VÄLKOMMEN TILL LÖSENORDSGENERATORN SOM GENERERAR KONTROLLERADE OCH SÄKRA LÖSENORD \033[0m")
print()
print()
print('                                      /\\________/\\')
print("                                     /            \\")
print("                                    |   o      o   |           MJAU?")
print("                                  ==|       *      |==")
print("                                     \\      ^     /")
print("                             .o(')o. /            \\ .o(')o.")
print("=============================================================================================")
print()
print()

def starta_program():
    while True:

        svar = input("Vill du ha ett lösenord? (ja/nej): ")

        if svar.lower() == "ja":
            print("Ditt lösenord genereras och kontrolleras därefter mot haveibeenpwned.com.")
            break
        elif svar.lower() == "nej":
            print("Då får du hitta på ett eget lösenord.")
            exit()
        else:
            print("Ogiltigt svar. Ange ja eller nej.")

    import secrets
    # Importerar kryptografiskt säkra lösenord.
    import string
    # Importerar Pythons inbyggda modul string.

    slumpat_losenord = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    # Skapar ett slumpmässigt lösenord bestående av siffror, små och stora bokstäver samt specialtecken.

    losenord = ''.join(secrets.choice(slumpat_losenord) for _ in range(15))
    # '' används för att blanksteg inte ska infogas mellan genererade tecken. Det vill säga alla tecken sammanfogas till en sträng.
    # secrets.choice() väljer ett slumpmässigt tecken från listan slumpat_losenord.
    # För att ändra lösenordets längd, ändra siffran inom parentes efter range.

    langd = len(losenord)
    print() 
    print("\033[1;95mDitt nya lösenord är:\033[0m", losenord)
    print(f"Lösenordets längd är {langd} tecken.")
    
    import hashlib
    # Importerar Pythons inbyggda modul för hash-funktioner.
    import urllib.request
    # Importerar Pythons inbyggda modul för att göra HTTP-förfrågningar.

    def kontrollera_losenord_hibp(losenord: str) -> int:
        sha1 = hashlib.sha1(losenord.encode("utf-8")).hexdigest().upper()

        prefix = sha1[:5]
        suffix = sha1[5:]

        url = f"https://api.pwnedpasswords.com/range/{prefix}"
    
        req = urllib.request.Request(url, headers={"User-Agent": "losenordsgenerator.py"})

        with urllib.request.urlopen(req, timeout=10) as response:
            data = response.read().decode("utf-8")

        for line in data.splitlines():
            hash_suffix, count = line.split(":")
            if hash_suffix == suffix:
                return int(count)

        return 0

    antal = kontrollera_losenord_hibp(losenord)

    if antal > 0:
        print(f"Lösenordet har läckt {antal} gånger!")
    else:
        print("Lösenordet har kontrollerats mot haveibeenpwned.com och finns inte med i några kända dataläckor.")
    # Lösenordet ska kontrolleras mot haveibeenpwned. Dock ska inte hela lösenordet kontrolleras mot databasen då det kan vara en säkerhetsrisk om 
    # hela lösenordet exponeras mot internet.

    print()

    while True:
        sakertsvar = input("Är du nöjd med ditt nya lösenord?: (ja/nej) ")
        if sakertsvar.lower() == "ja":
            print("Scriptet avslutas.")
            exit()

        elif sakertsvar.lower() == "nej":
            print("Scriptet startar om.")
            break
        else:
            print("Ogiltigt svar. Svara ja eller nej.")
    print()
    print()

while True:
    starta_program()
    # Scriptet körs från början, om användaren inte är nöjd med det genererade lösenordet.
