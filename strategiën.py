import itertools
import random
import interacties
import interacties as interactie

# dict om over te nemen in functies
dict_mogelijke_feedback = {(0, 0): 0, (0, 1): 0, (0, 2): 0, (0, 3): 0, (0, 4): 0, (1, 0): 0, (1, 1): 0, (1, 2): 0, (1, 3): 0, (2, 0): 0, (2, 1): 0, (2, 2): 0, (3, 0): 0, (4, 0): 0}


# functie voor het genereren van de combinaties
def alle_combinaties():
    """
    Maak alle combinaties mogelijk

    :return: lijst
    """
    # lijst met alle opties
    colors = ['a', 'b', 'c', 'd', 'e', 'f']

    # genereert een lijst die alle mogelijke combinaties van de lijst 'colors' maakt
    combinaties = list(itertools.product(colors, repeat=4))

    return combinaties


# reduceer zoekruimte functie
def reduceer_zoekruimte(resterende_combinaties, antwoord, stel_vraag):
    """
    De functie kijkt welke opties uit de lijst nog wel kunnen en add deze aan een nieuwe lijst.
    :param resterende_combinaties: vorige lijst met combinaties
    :param antwoord: antwoord op de vraag
    :param stel_vraag: de gestelde vraag.
    :return: lijst
    """
    # lege lijst om in toe te voegen
    nieuwe_zoekruimte = []

    # loop door de resterende combinaties
    for code in resterende_combinaties:
        # als deze vergelijking klopt wordt 'code' toegevoegd aan de nieuwe lijst
        if antwoord == interactie.antwoord(code, stel_vraag):
            nieuwe_zoekruimte.append(code)

    return nieuwe_zoekruimte


def simpele_strategie():
    """
    Pak index 0 uit de lijst.
    :return: keuze
    """
    # maak variabele die index 0 pakt uit een lijst.
    keuze = reduceer_zoekruimte()[0]

    return keuze


def frequentie_tabel(combinaties):
    """
    Maakt een frequentietabel met de dict variabele bovenin het bestand.
    :param combinaties: lijst met resterende combinaties
    :return: dict
    """
    # maak een lege dict
    frequentie_tabel = {}

    # loop de lijst van combinaties
    for code in combinaties:
        # maak een kopie van de mogelijke feedback dictionary en voeg deze toe aan de frequentietabel
        frequentie_tabel[code] = dict_mogelijke_feedback.copy()
        # loop over alle codes in de lijst combinaties
        for code_2 in combinaties:
            # gebruik antwoordfunctie voor feedback op de huidige combinatie en de code uit de buitenste loop
            antwoord = interacties.antwoord(code_2, code)
            # verhoog de frequentie van de feedback in de frequentietabel
            frequentie_tabel[code][(antwoord[0], antwoord[1])] += 1

    return frequentie_tabel


def worst_case_strategie(frequentie_tabel):
    """
    Deze functie zoekt vraag(code) wat de lijst het snelst reduceert om zo min mogelijk zetten de code te raden.

    :param frequentie_tabel: dict van de frequentie van codes
    :return: lijst
    """
    # stel max aantal voorkomens in op 999
    max_voorkomens = 999
    # lijst die bijhoudt welke vraag het hoogste aantal unieke feedbacks oplevert
    max_vraag = []

    # loop door alle mogelijkheden in de frequentietabel
    for code in frequentie_tabel:
        # zet maximum op 0
        maximum = 0
        # loop door alle mogelijkheden van de huidige vraag in de frequentietabel
        for code_2 in frequentie_tabel[code]:
            # als de frequentie van de huidige feedback hoger is dan het huidige maximum,
            # wijzig maximum naar de frequentie van deze feedback
            if frequentie_tabel[code][code_2] > maximum:
                maximum = frequentie_tabel[code][code_2]
        # als maximum aantal keren dat een feedback voorkomt kleiner is dan huidige waarde van max,
        # wijzig max naar deze waarde en wijs de huidige vraag toe aan max_vraag
        if maximum < max_voorkomens:
            max_voorkomens = maximum
            max_vraag = code

    return max_vraag


def eigen_strategie(resterende_combintaties):
    """
    Dit is mijn eigenbedachte ai.
    Hij is misschien te simpel, maar het is interessant om te kijken hoe snel deze functie de code kan raden.
    Omdat deze code zo random is kan de lijst erg snel verkleint worden
    waardoor er snel een oplossing gevonden kan zijn.

    :param resterende_combintaties: nog beschikbare combinaties
    :return: keuze
    """
    # maakt random keuze uit de lijst van resterende combinaties
    keuze = random.choice(resterende_combintaties)

    return keuze
