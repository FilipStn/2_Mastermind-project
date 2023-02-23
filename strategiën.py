import itertools
import interacties as interactie
# import speelveld

def alle_combinaties():
    """
    Maak alle combinaties mogelijk

    :return: copy van de gemaakte lijst.
    """
    colors = ['a', 'b', 'c', 'd', 'e', 'f']

    combinaties = list(itertools.product(colors, repeat=4))

    return combinaties


print(len(alle_combinaties()))


def alle_antwoorden(alle_combinaties):
    """
    Deze functie onthoudt alle al gegeven antwoorden
    :return: copy van de gemaakte lijst
    """
    # interacties.antwoord(stel_vraag, code)



def reduceer_zoekruimte(resterende_combinaties, antwoord, stel_vraag):
    """"""
    nieuwe_zoekruimte = []

    for code in resterende_combinaties:
        if antwoord == interactie.antwoord(interactie.antwoord()[2], interactie.stel_vraag(speler)):
            nieuwe_zoekruimte.append(code)

    return nieuwe_zoekruimte

def simpele_strategie():
    """"""
    keuze = reduceer_zoekruimte()[0]

    return keuze