

def antwoord(code, stel_vraag):
    """"""
    rood = 0
    wit = 0
    lst_idx = -1

    for element in stel_vraag:
        if element in code:
            lst_idx = stel_vraag.index(element)
            if stel_vraag[lst_idx] == code[lst_idx]:
                rood += 1

            else:
                wit += 1

    return f'Rood: {rood}, Wit: {wit}'

def _voorgekomen_antwoord():
    """
    Houd een lijst bij met de al voorgekomen karakters om dubbele notaties te voorkomen.
    :return:
    """


def stel_vraag(speler):
    """
    Kijk of de input een speler of computer is.
    Als de speler een mens is opent functie _mens_vraag().
    Anders opent _ai_vraag()

    :param speler: mens, ai
    :return:
    """

    # als de invoer van wie er speelt gelijk is aan 'mens',
    # opent de functie '_mens_vraag()'.
    if speler == 'mens':
        mens = _mens_vraag()
        return mens

    # als de invoer van wie er speelt gelijk is aan 'computer',
    # opent de functie '_ai_vraag()'.
    else:
        ai = _ai_vraag()
        return ai


def _mens_vraag():
    """
    Deze functie vraagt input aan de speler.
    De input wordt gesplit op spaties.

    :return: vraag.split()
    """
    # vraag input van de speler
    vraag = input("Voer hier een mogelijke combinatie in: ").lower().strip()

    # return de vraag met een split op de spatie
    return vraag.split(' ')

def _ai_vraag():
     return 0

def afsluiten():
    """"""

