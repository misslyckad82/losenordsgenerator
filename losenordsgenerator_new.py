#!/usr/bin/env python3
"""
Beskrivning: Detta Python-script genererar slumpmässiga lösenord bestående av både siffror, bokstäver och specialtecken. Lösenordet kontrolleras mot haveIbeenpwned.com för att se om det har upptäckts i kända läckor.
Författare: Sanna Rytilahti 
ASCII-konst: Sanna Rytilahti
Senast ändrad: 2026-01-13
"""


print()
print()
print("    \033[1;95m VÄLKOMMEN TILL LÖSENORDSGENERATORN SOM GENERERAR KONTROLLERADE OCH SÄKRA LÖSENORD \033[0m")
print()
print()
print('                                      /\\________/\\')
print("                                     /            \\")
print("                                    |   o      o   |           LÖSENORD = MJAU?")
print("                                  ==|       *      |==")
print("                                     \\      ^     /")
print("                             .o(')o. /            \\ .o(')o.")
print("=============================================================================================")
print()
print()

def starta_program():

    while True:

        svar = input("\033[1;95mVill du ha ett lösenord?\033[0m (ja/nej): ")
        # Output till användaren, kräver input.

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
    # För att ändra lösenordets längd, ändra siffran i range.

    langd = len(losenord)
    # len() räknar antalet tecken i en sträng.
    print() 
    print("\033[1;95mDitt nya lösenord är:\033[0m", losenord)
    # Output lösenord.
    print()
   
    print(f"\033[1;95mLösenordets längd är:\033[0m {langd} \033[1;95mtecken.\033[0m")
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
        # suffix = resten av hashvärdet.
        # API:t returnerar alla SHA-1-hashar som börjar med prefixet.
        # Scriptet skickar endast de första fem tecknen i hashvärdet för att inte exponera lösenordet mot internet (säkerhetsrisk).
        
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        # API:t returnerar alla SHA-1-hashar som börjar med prefixet.
    
        req = urllib.request.Request(url, headers={"User-Agent": "losenordsgenerator.py"})
        # Skapar en request med en User-agent då haveIbeenpwned kräver att man anger en. I detta fall losenordsgenerator.py.
        
        with urllib.request.urlopen(req, timeout=10) as response:
            data = response.read().decode("utf-8")
            # Skickar förfrågan. Läser svaret som text.
            # data innehåller rader i formatet hash_suffix:count.

        for line in data.splitlines():
            hash_suffix, count = line.split(":")
            if hash_suffix == suffix:
                return int(count)
            # Varje rad delas upp i hash_suffix = de sista 35 tecknen av hashvärdet. count = hur många gånger lösenordet har läckt.
            # Om suffixet matchar lösenordets suffix = lösenordet finns i databasen. 
            # Returnerar antal läckor.

        return 0
        # Inga träffar = lösenordet finns inte i haveIbeenpwned-databasen.

    antal = kontrollera_losenord_hibp(losenord)
    # Kör funktionen med genererat lösenord som argument. Funktionen returnerar ett heltal (antal gånger lösenordet har hittats i dataläckor). 
    # Värdet sparas i variabeln antal.

    if antal > 0:
        print(f"Lösenordet har läckt {antal} gånger!")
        # Output antal gånger lösenordet läckt.

    else:
        print("Lösenordet har kontrollerats mot haveibeenpwned.com och finns inte med i några kända dataläckor.")
        # Output lösenordet finns inte med i några läckor enligt haveIbeenpwned.

    print()

    while True:
        sakertsvar = input("\033[1;95mÄr du nöjd med ditt nya lösenord?:\033[0m (ja/nej) ")
        # Output till användaren om hen är nöjd med det genererade lösenordet, kräver input.
        if sakertsvar.lower() == "ja":
            print("Lösenordsgeneratorn avslutas.")
            exit()
            
        elif sakertsvar.lower() == "nej":
            print("Lösenordsgeneratorn startar om.")
            break

        else:
            print("Ogiltigt svar. Svara ja eller nej.")

    print()
    print()

while True:
    starta_program()
    # Scriptet körs från början, om användaren inte är nöjd med det genererade lösenordet.
