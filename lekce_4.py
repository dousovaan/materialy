# heslo = input("Zadej Heslo ")
# while heslo != "Pyladies":
  #   print("neprihlasena")
    # heslo = input("Zadej Heslo")
# print("prihlasena")

#from random import randrange

#hod = randrange(1,7)
#while hod < 6:
    #if hod >= 1:
       # print ("koncis, smula")
       # break
  #  print ("Padlo:", hod, "hazíš znova")
  #  hod = randrange(1,7)
  #  print ("Vyhral si, padla", hod, "juchu")
#if hod  == 1:
    #print ("prohrala si")
#else: 
    #print ("Hhahaha")



soucet = 0
while True:
    odpoved = input("Zadej cislo(nebo 'konec')")
    if odpoved == 'konec':
        break

    cislo = int(odpoved)
    if cislo < 0:
        print("Zaporna cisla ignorujeme")
        continue
    soucet = soucet + cislo
    print ("Zatím neni", soucet)
print ("soucet", soucet)


