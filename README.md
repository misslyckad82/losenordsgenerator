# **SecureCat** 

## Syfte/Mål
Detta projekt syftar till att skapa ett script som genererar säkra och kontrollerade lösenord. <br>
Lösenord som inte kan knäckas genom exempelvis social engineering. <br>
Målet är att användaren ska få ett säkert lösenord som är kontrollerat mot HaveIbeenpwnd.com och kända dataläckor. <br>

## Funktion
Scriptet skapar ett slumpmässigt lösenord med 15 tecken baserat på siffror, små och stora bokstäver samt specialtecken. <br>
Användaren kan välja att få ett nytt lösenord om det första inte är okej. <br>
Användaren kan därefter välja att spara ner lösenordet i en fil till sin dator. Filen hamnar i samma mapp som SecureCat.py. <br>

## Framtida förbättringar
 - Kunna köra scriptet offline.
 - Generera krypterad lösenordsfil. Det är inte säkert att spara en fil med lösenord på datorn.
 - Alternativt spara lösenordet i en extern lösenordshanterare.
 - Användaren ska kunna mata in ett eget lösenord och se om det har läckt. <br>
   Lösenordet ska uppfylla vissa kriterier för att vara säkert.
 - Kontrollera lösenordet mot Rockyou.txt.

## Systemkrav
Python-scriptet fungerar i följande miljöer:  <br>
 - Linux  <br>
 - Windows  <br>
 - Mac OS  <br>

## Instruktioner för körning
- Klona repot https://github.com/misslyckad82/SecureCat.git <br>
- Kör SecureCat.py i din terminal.  <br>

#### Kommandon Powershell: <br>
- cd <insert hela sökvägen till där SecureCat.py ligger på din dator> <br>
- python SecureCat.py <br>

#### Kommandon Linux:  <br>
- chmod +x SecureCat.py
- python3 SecureCat.py <br>

#### Kommandon Mac Terminal <br>
- python3 SecureCat.py

## Film <br>
https://youtu.be/UTZUxXx-QUo
