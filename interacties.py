import speelveld

def antwoord():
    """"""

def stel_vraag(speler):
    """

    :param speler: mens, ai
    :return:
    """

    if speler == 'mens':
        mens = _vraag_mens()
        return mens

    else:
        ai = _vraag_ai()
        return ai


def _vraag_mens():
    vraag = input("Voer hier een mogelijke combinatie in: ")

    return vraag

def _vraag_ai():
     return 0

def afsluiten():
    """"""

