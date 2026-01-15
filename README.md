# **SecureCat** 

## Syfte/Mål
Detta projekt syftar till att skapa ett script som genererar säkra och kontrollerade lösenord. <br>
Lösenord som inte kan knäckas genom exempelvis social engineering. <br>
Målet är att användaren ska få ett säkert lösenord som är kontrollerat mot HaveIbeenpwnd.com och kända dataläckor. <br>

## Funktion
Scriptet skapar ett slumpmässigt lösenord baserat på siffror, små och stora bokstäver samt specialtecken. <br>
Användaren kan därefter välja att spara ner lösenordet i en fil till sin dator. Filen hamnar i samma mapp som SecureCat.py. <br>

## Framtida förbättringar
 - Krypterad lösenordsfil. Det är inte säkert att spara en fil med lösenord på datorn.
 - Alternativt spara lösenordet i en lösenordshanterare.
 - Användaren ska kunna mata in ett eget lösenord och se om det har läckt. <br>
   Lösenordet ska uppfylla vissa kriterier för att vara säkert.

## Systemkrav
Python-scriptet fungerar i följande miljöer:  <br>
 - Linux  <br>
 - Windows  <br>
 - Mac OS  <br>

## Instruktioner för körning
- Ladda ner repot (SecureCat.py) <br>
- Kör SecureCat.py i din terminal  <br>

### Kommandon Powershell: <br>
- cd <insert hela sökvägen till där SecureCat.py ligger på din dator> <br>
- python SecureCat.py <br>

### Kommandon Linux:  <br>
- chmod +x SecureCat.py
- python3 ./SecureCat.py <br>

### Mac OS <br>
- python3 SecureCat.py

## Film <br>
https://youtu.be/ukBOVXCo3V8
