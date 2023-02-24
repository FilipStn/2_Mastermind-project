import random


# sla deze functie op in een variabelen
def geheime_code():
    """
    Genereert de geheime code voor het raden.
    :return: list
    """
    colors = ['a', 'b', 'c', 'd', 'e', 'f']
    # random keuze van 4 elementen uit 'colors'
    choice = random.choices(colors, k=4)
    # voor debuggen
    # print(choice)

    return choice


"De functie onder pijltjes was hoe ik eerst het spel starten, dit gaf error's over circular import."
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
    """
    Lijst aanmaken poging(beurtnummer), vraag en het antwoord toevoegd aan de bestaande lijst 'eerdere_pogingen'.
    :param eerdere_pogingen: bestaande lijst met eerdere pogingen
    :param poging: nummer van de beurt
    :param vraag: de gok die gedaan is
    :param antwoord: wat wel en niet goed was
    :return: geüpdatet lijst
    """
    # voeg aan de bestaande lijst een f-string met de waardes: poging, vraag en antwoord.
    eerdere_pogingen.append(f'{poging}: {vraag} : {antwoord}')

    return eerdere_pogingen


def einde_spel(poging, antwoord, code):
    """
    Vergelijk het antwoord, is deze 4,0 dan return False om het spel te stoppen.
    Hetzelfde geldt voor de aantal pogingen,
    als deze gelijk staan aan 9 is het niet in 8 pogingen gelukt. Returned False om het spel te stoppen.
    Als False gereturned word, break de while loop.
    :param poging: poging nummer
    :param antwoord: zwarte en witte pinnen.
    :return: bool
    """
    # vergelijk antwoord met de waardes die eruit moeten komen, 4,0 is spel gewonnen.
    if antwoord == (4, 0):
        print(f'Gefeliceerd, je hebt de geheime code geraden in {poging} pogingen.')
        # return False om uit de while loop te breken.
        return False
    # als poging gelijk is aan 9 is het niet gelukt om het binnen 8 beurten te doen en is het spel verloren.
    elif poging == 9:
        print(f'Helaas heb je het niet geraden in 8 pogingen. Het juiste antwoord was: {code}.')
        # return False om uit de while loop te breken.
        return False

    return True


    # if gewonnen:
    #     print(f'Gefeliceerd, je hebt de geheime code geraden in {poging} pogingen.')
    #
    # else:
    #     print(f'Helaas heb je het niet geraden in 8 pogingen. Het juiste antwoord was: {code}.')

    # print(f'Wil je het nog een keer proberen?')
    #
    # keuze = input('Voer hier uw keuze in: ').lower()
    #
    # if keuze == 'ja':
    #     return True
    #
    # else:
    #     print('Fijne dag!')
    #     return False
