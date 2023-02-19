import random

import interacties
from interacties import *
# itertools.product

# sla deze functie op in een variabelen
def geheime_code():
    colors = ['a', 'b', 'c', 'd', 'e', 'f']
    # random keuze van 4 elementen uit 'colors'
    choice = random.sample(colors, 4)
    # voor debuggen
    print(choice)

    return choice


geheime_code()


def start_spel():
    """
    deze functie moet het spel starten
    hoeveel je mag kiezen
    wat de keuze is,
    wie er speelt,
    while loop door blijven vragen
    optioneel: aantal kleuren
    """

    print('Welkom bij Mastermind! Je krijgt de opties uit "a, b, c, d, e, f".\n'
          'Bij dit spel is het de bedoeling de code te kraken door de juiste combinatie te maken.')
    print("Het is mogelijk om de computer het spel te laten oplossen, maar uiteraard is het leuker om zelf te spelen."
          "Door in kleine letters 'computer' of 'mens' te typen maak je een keuze")
    speler = input("Wie speelt er: ").lower()
    code = geheime_code()
    vraag = ''
    poging = 0
    eerdere_pogingen = []


    while vraag != code:
        vraag = interacties.stel_vraag(speler)
        antwoord = ''
        if vraag != code:
            antwoord = interacties.antwoord(code, vraag)
            poging += 1
            opslaan_speelveld(eerdere_pogingen, poging, vraag, antwoord)
            for p in eerdere_pogingen:
                print(p, end='\n')

        elif poging == 9 and vraag != code:
            einde_spel(False, code)

        elif vraag == code:
            einde_spel(True, code)


def opslaan_speelveld(eerdere_pogingen, poging, vraag, antwoord):
    """dict aanmaken om met de key de row aanmaken en de value is de ingevoerde waarde van de speler."""

    eerdere_pogingen.append(f'{poging}: {vraag} : {antwoord}')

    return eerdere_pogingen



def update_speelveld():
    """Eerdere pogingen tonen"""


def einde_spel(gewonnen, code):
    """"""
    if gewonnen:
        print('Gefeliceerd, je hebt de geheime code geraden.')

    else:
        print(f'Helaas heb je het niet geraden in 8 pogingen. Het juiste antwoord was: {code}.')

    print(f'Wil je het nog een keer proberen?')

    keuze = input('Voer hier uw keuze in: ').lower()

    if keuze == 'ja':
        start_spel()

    else:
        print('Fijne dag!')
    exit()


# main
start_spel()