# Cvičení 4 – Podmínky
# Doplň kód pod zadání a soubor spusť (Run).

# Máš proměnnou barva se stavem semaforu ("červená", "oranžová"
#    nebo "zelená"). Vypiš, co má řidič udělat:
#    "červená" → "Stůj", "oranžová" → "Připrav se", "zelená" → "Jeď",
#    cokoli jiného → "Neznámý signál".
barva = "ZELLOW"
if barva == "red":
     print ("stuj")
elif barva == "orange":
        print ("priprav se")
elif barva == "green":
        print ("jed")
else:
      print ("chyba semaforu")  