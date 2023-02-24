import itertools
import random
import interacties
import interacties as interactie
# import speelveld

dict_mogelijke_feedback = {(0, 0): 0, (0, 1): 0, (0, 2): 0, (0, 3): 0, (0, 4): 0, (1, 0): 0, (1, 1): 0, (1, 2): 0, (1, 3): 0, (2, 0): 0, (2, 1): 0, (2, 2): 0, (3, 0): 0, (4, 0): 0}
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
        if antwoord == interactie.antwoord(code, stel_vraag):
            nieuwe_zoekruimte.append(code)
    # print(nieuwe_zoekruimte)
    return nieuwe_zoekruimte

def simpele_strategie():
    """"""
    keuze = reduceer_zoekruimte()[0]

    return keuze

def frequentie_tabel(combinaties):
    frequentie_tabel = {}
    for i in combinaties:
        # print(i)
        frequentie_tabel[i] = dict_mogelijke_feedback.copy()
        for j in combinaties:
            antwoord = interacties.antwoord(j, i)
            frequentie_tabel[i][(antwoord[0], antwoord[1])] += 1

    return frequentie_tabel

def worst_case_strategie(frequentie_tabel):
    max = 999
    max_vraag = []
    for i in frequentie_tabel:
       maximum = 0
       for j in frequentie_tabel[i]:
           if frequentie_tabel[i][j] > maximum:
               maximum = frequentie_tabel[i][j]
       if maximum < max:
            max = maximum
            max_vraag = i

    return max_vraag

def eigen_strategie(resterende_combintaties):
    keuze = random.choice(resterende_combintaties)

    return keuze
