# Cvičení 5 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Hody dvěma kostkami. Vnořenými cykly vypiš všechny možné hody
#    dvěma kostkami (každá má čísla 1 až 6) a u každého i jejich součet.
#    Každý řádek bude vypadat třeba takhle: 2 + 5 = 7


for kosticka1 in range (1,7):
    for kosticka2 in range (1,7):
        print (kosticka1, "+", kosticka2, "=", kosticka1 + kosticka2)

