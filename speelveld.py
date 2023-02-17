import random

import interacties
from interacties import *
# itertools.product

# sla deze functie op in een variabelen
def geheime_code():
    colors = ['a', 'b', 'c', 'd', 'e', 'f']
    # random keuze van 4 elementen uit 'colors'
    choice = random.sample(colors, 4)

    return choice


print(geheime_code())

def start_spel():
    # deze functie moet het spel starten
    # hoeveel je mag kiezen
    """wat de keuze is,
    wie er speelt,
    while loop door blijven vragen
    optioneel: aantal kleuren
    """

    print('Welkom bij Mastermind! Je krijgt de opties uit "a, b, c, d, e, f"')
    print("Het is mogelijk om de computer het spel te laten oplossen, maar uiteraard is het leuker om zelf te spelen."
          "Door in kleine letters 'computer' of 'speler' te typen maak je een keuze")
    speler = input("Wie speelt er: ")
    code = geheime_code()

    while interacties.stel_vraag(speler) != code:
        poging = 0
        if interacties.stel_vraag() != code:
            poging +=1
        elif poging == 9 and interacties.stel_vraag() != code:
            einde_spel()

def opslaan_speelveld():
    """dict aanmaken om met de key de row aanmaken en de value is de ingevoerde waarde van de speler."""
    # key = poging


def update_speelveld():
    """"""


def einde_spel():
    """"""
    print('Helaas heb je het niet geraden in 8 pogingen. Wil je het nog een keer proberen?')
    keuze = input('Voer hier uw keuze in: ')

    if keuze == 'ja' or 'JA' or 'Ja':
        start_spel()
    else:
        print('Fijne dag!')
        exit()