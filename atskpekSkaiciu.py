import random
import string

# f-ja, kuri išvalo failą nuo senų duomenų
def valytiFaila():
    with open('reg.txt', 'w') as f:
        pass

# f-ja rašo info į failą reg01.txt
def rasytiIFaila(txt):
    with open('reg.txt', 'a', encoding='utf-8') as f:
        f.write(txt + '\n')

valytiFaila()
zaidSk = 0
while True:
    zaidSk += 1  # žaidimų skaičius
    rasytiIFaila(f'{zaidSk} ŽAIDIMAS')
    n = int(input('Įveskite sveiką teigiamą skaičių:... '))
    rasytiIFaila(f'Vartotojas įvedė skaičių {n}')
    nRan = random.randint(1,n) # sugeneruotas kompiuterio skaičius imtinai
    rasytiIFaila(f'Sugeneruotas atsitiktinis skaičius {nRan}\n')
    gSpej = bSpej = 0 # teisingų ir neteisingų spėjimų kiekis
    while True:
        spej = input('Spėkite skaičių (Raidė nutraukia žaidimą)... ')
        if spej in string.ascii_letters:
            print ('Žaidimas nutraukas. Viso gero...')
            rasytiIFaila(f'Vartotojas nutraukė žaidimą.')
            break
        else:
            spej = int(spej)
            if spej > n or spej < 0:
                print('Įvestas skaičius yra neteisingas.')
                #rasytiIFaila('! vartotojas įvedė neteisingą skaičių.')
                bSpej += 1
            elif spej > nRan:
                gSpej += 1
                print(f'Sugeneruotas skaičius yra mažesnis už {spej}. Atliksite {gSpej+1} spėjimą.')
                rasytiIFaila(f'{gSpej} spėjimu vartotojas įvedė {spej}. Atsakymas - sugeneruotas skaičius mažesnis.')
            elif spej < nRan:
                gSpej += 1
                print(f'Sugeneruottas skaičius yra didesnis už {spej}. Atliksite {gSpej+1} spėjimą.')
                rasytiIFaila(f'{gSpej} spėjimu vartotojas įvedė {spej}. Atsakymas - sugeneruotas skaičius didesnis.')
            else:
                gSpej += 1
                print(f'\nSveikinam! Atspėjote :)')
                rasytiIFaila(f'{gSpej} spėjimu vartotojas atspėjo skaičių.')
                break
    print(f'\nAčiū už žaidimą! Kompiuterio sugeneruotas skaičius yra {nRan}.\nIš viso atlikta spėjimų: {gSpej}\nBandymai įvesti netinkamą skaičių: {bSpej}\n')
    rasytiIFaila(f'{bSpej} bandymas(ai) įvesti netinkamą skaičių.\n')
    ats = input('Ar norite žaisti žaidimą?(T/N) ')
    if ats != 'T' and ats != 't':
        print ('Viso gero...')
        rasytiIFaila(f'\nĮ užklausą „Ar žaisite dar“ pasirinko „Ne“.')
        break

rasytiIFaila(f'Vartotojas žaidė {zaidSk} kartą(us).')