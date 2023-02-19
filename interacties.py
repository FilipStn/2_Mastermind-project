

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


def stel_vraag(speler):
    """

    :param speler: mens, ai
    :return:
    """

    if speler == 'mens':
        mens = _mens_vraag()
        return mens

    else:
        ai = _ai_vraag()
        return ai


def _mens_vraag():
    vraag = input("Voer hier een mogelijke combinatie in: ").lower().strip()
    # hier kan al gesplit worden
    # print(vraag)
    return vraag.split(' ')

def _ai_vraag():
     return 0

def afsluiten():
    """"""

