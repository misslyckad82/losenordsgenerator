#!/usr/bin/env python3

"""
Beskrivning: Detta Python-script genererar slumpmässiga lösenord av både siffror, bokstäver och specialtecken. Lösenordet kontrolleras mot haveIbeenpwned.com för att se om det har upptäckts i kända dataläckor. 
             Därefter kan man välja om man vill spara lösenordet i en fil på sin dator.
Författare: Sanna Rytilahti 
ASCII-konst: Sanna Rytilahti
Senast ändrad: 2026-01-13
"""


print()
print()
print("    \033[1;95m VÄLKOMMEN TILL SECURECAT SOM GENERERAR KONTROLLERADE OCH SÄKRA LÖSENORD \033[0m")
print()
print()
print('                                      /\\________/\\')
print("                                     /            \\")
print("                                    |   o      o   |           \033[38;5;218mLÖSENORD = MJAU?\033[0m")
print("                                  ==|       *      |==")
print("                                     \\      ^     /")
print("                             .o(')o. /            \\ .o(')o.")
print("====================================================================================")


def starta_program():

    while True:

        svar = input("\033[1;95mVill du ha ett lösenord?\033[0m (ja/nej) ")
        # Output till användaren, kräver input.

        if svar.lower() == "ja":
            print("\033[38;5;218mDitt lösenord genereras.\033[0m")
            break

        elif svar.lower() == "nej":
            print("\033[38;5;218mDå får du hitta på ett eget lösenord.\033[0m")
            print("SecureCat avslutas.")
            exit()

        else:
            print("\033[38;5;218mOgiltigt svar. Ange ja eller nej.\033[0m")
            print()

    import secrets
    # Importerar kryptografiskt säkra lösenord.
    import string
    # Importerar Pythons inbyggda modul string.

    slumpat_losenord = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    # Skapar ett slumpmässigt lösenord bestående av siffror, små och stora bokstäver samt specialtecken.

    losenord = ''.join(secrets.choice(slumpat_losenord) for _ in range(15))
    # '' används för att blanksteg inte ska infogas mellan genererade tecken. Det vill säga alla tecken sammanfogas till en sträng.
    # secrets.choice() väljer ett slumpmässigt tecken från listan slumpat_losenord.
    # För att ändra lösenordets längd, ändra siffran i range.

    langd = len(losenord)
    # len() räknar antalet tecken i en sträng.
    print() 
    print("\033[1;95mDitt nya lösenord är:\033[0m", losenord)
    # Output lösenord.
   
    print(f"\033[1;95mLösenordets längd är:\033[0m {langd} tecken.")
    # Output lösenordets längd.
    
    import hashlib
    # Importerar Pythons inbyggda modul för hash-funktioner.

    import urllib.request
    # Importerar Pythons inbyggda modul för att göra HTTP-förfrågningar.


    def kontrollera_losenord_hibp(losenord: str) -> int:
    # Funktionen tar ett lösenord som sträng och returnerar ett heltal. Heltalet är antal gånger lösenordet läckt enligt haveIbeenpwned.

        sha1 = hashlib.sha1(losenord.encode("utf-8")).hexdigest().upper()
        # .encode("utf-8") gör om lösenordet till bytes. Det hashas med SHA-1 då haveIbeenpwned kräver SHA-1.
        # .hexidigest() gör om hashvärdet till en hex-sträng.
        # .upper() gör om bokstäverna A-F till versaler då haveIbeenpwned kräver detta.

        prefix = sha1[:5]
        # prefix = de fem första tecknen i SHA-1-hashen. 

        suffix = sha1[5:]
        # suffix = resten av hashvärdet i SHA-1-hashen.
        # API:t returnerar alla SHA-1-hashar som börjar med prefixet.
        # Scriptet skickar endast de första fem tecknen i hashvärdet för att inte exponera lösenordet mot internet (säkerhetsrisk).
        
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        # API:t returnerar alla SHA-1-hashar som börjar med prefixet.
    
        req = urllib.request.Request(url, headers={"User-Agent": "secure_cat.py"})
        # Skapar en request med en User-agent då haveIbeenpwned kräver att man anger en. I detta fall secure_cat.py.
        
        with urllib.request.urlopen(req, timeout=10) as response:
            data = response.read().decode("utf-8")
            # Skickar förfrågan. Läser svaret som text.
            # data innehåller rader i formatet hash_suffix:count.

        for line in data.splitlines():
            hash_suffix, count = line.split(":")
            # Varje rad delas upp i hash_suffix = de sista 35 tecknen av hashvärdet. count = hur många gånger lösenordet har läckt.
            if hash_suffix == suffix:
            # Om suffixet matchar lösenordets suffix = lösenordet finns i databasen.
                return int(count)
            # Returnerar antal läckor.

        return 0
        # Inga träffar = lösenordet finns inte i haveIbeenpwned-databasen.

    antal = kontrollera_losenord_hibp(losenord)
    # Kör funktionen med genererat lösenord som argument. Funktionen returnerar ett heltal (antal gånger lösenordet har hittats i dataläckor). 
    # Värdet sparas i variabeln antal.

    if antal > 0:
        print(f"\033[38;5;218mLösenordet har läckt {antal} gånger!")
        # Output antal gånger lösenordet läckt.

    else:
        print("\033[38;5;218mLösenordet har kontrollerats mot haveibeenpwned.com:s databas och finns inte med i några kända läckor.")
        # Output lösenordet finns inte med i några läckor enligt haveIbeenpwned.

    print()

    while True:
        sakertsvar = input("\033[1;95mÄr du nöjd med ditt lösenord?\033[0m (ja/nej) ")
        # Output till användaren om hen är nöjd med det genererade lösenordet, kräver input.
        if sakertsvar.lower() == "ja":
            while True:
                sparalosenord = input("\033[1;95mÖnskar du spara ditt lösenord i en fil?\033[0m (ja/nej) ")
                if sparalosenord.lower() == "ja":
                   
                    filnamn = input("\033[1;95mVad vill du att filen ska heta? \033[0m")
                    with open(filnamn + ".txt", "w", encoding="utf-8") as fil:
                        fil.write(losenord)
                        
                        print("\033[38;5;218mLösenordet har sparats!\033[0m")
                        print()
                        exit()

                    exit()
                elif sparalosenord.lower() == "nej":
                    print("\033[38;5;218mSecureCat avslutas.\033[0m")
                    print()
                    exit()
                 
                else:
                    print("\033[38;5;218mOgiltigt svar. Svara ja eller nej.\033[0m")
                    print()
            
        elif sakertsvar.lower() == "nej":
            print("\033[38;5;218mSecureCat startar om.\033[0m")
            print()
            break

        else:
            print("\033[38;5;218mOgiltigt svar. Svara ja eller nej.\033[0m")
            print()

print()
print()

while True:
    starta_program()
    # Scriptet körs från början, om användaren inte är nöjd med det genererade lösenordet.

