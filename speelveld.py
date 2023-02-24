import random
# import main

import interacties
from interacties import *
# itertools.product

# sla deze functie op in een variabelen
def geheime_code():
    colors = ['a', 'b', 'c', 'd', 'e', 'f']
    # random keuze van 4 elementen uit 'colors'
    choice = random.choices(colors, k=4)
    # voor debuggen
    print(choice)

    return choice


# geheime_code()


# def start_spel():
#     """
#     deze functie moet het spel starten
#     hoeveel je mag kiezen
#     wat de keuze is,
#     wie er speelt,
#     while loop door blijven vragen
#     optioneel: aantal kleuren
#     """
#
#     print('Welkom bij Mastermind! Je krijgt de opties uit "a, b, c, d, e, f".\n'
#           'Bij dit spel is het de bedoeling de code te kraken door de juiste combinatie te maken.')
#     print("Het is mogelijk om de computer het spel te laten oplossen, maar uiteraard is het leuker om zelf te spelen."
#           "Door in kleine letters 'computer' of 'mens' te typen maak je een keuze")
#     speler = input("Wie speelt er: ").lower()
#     code = geheime_code()
#     vraag = ''
#     poging = 0
#     eerdere_pogingen = []
#
#
#     while vraag != code:
#         vraag = interacties.stel_vraag(speler)
#         antwoord = ''
#         if vraag != code:
#             antwoord = interacties.antwoord(code, vraag)
#             poging += 1
#             opslaan_speelveld(eerdere_pogingen, poging, vraag, antwoord)
#             if speler != 'mens':
#                 for p in eerdere_pogingen:
#                     print(p, end='\n')
#
#         elif poging == 9 and vraag != code:
#             einde_spel(False, code)
#
#         elif vraag == code:
#             einde_spel(True, code)


def opslaan_speelveld(eerdere_pogingen, poging, vraag, antwoord):
    """dict aanmaken om met de key de row aanmaken en de value is de ingevoerde waarde van de speler."""

    eerdere_pogingen.append(f'{poging}: {vraag} : {antwoord}')

    return eerdere_pogingen


def ai_simpele_strategie():
    ronde = 1

    nieuwe_zoekruimte = []


def update_speelveld():
    """Eerdere pogingen tonen"""


def einde_spel(poging, code ,vraag):
    """"""
    if vraag == code:
        print(f'Gefeliceerd, je hebt de geheime code geraden in {poging} pogingen.')

    elif poging == 9 and vraag != code:
        print(f'Helaas heb je het niet geraden in 8 pogingen. Het juiste antwoord was: {code}.')

    # if gewonnen:
    #     print(f'Gefeliceerd, je hebt de geheime code geraden in {poging} pogingen.')
    #
    # else:
    #     print(f'Helaas heb je het niet geraden in 8 pogingen. Het juiste antwoord was: {code}.')

    print(f'Wil je het nog een keer proberen?')

    keuze = input('Voer hier uw keuze in: ').lower()

    if keuze == 'ja':
        return True

    else:
        print('Fijne dag!')
        return False




# main
# start_spel()