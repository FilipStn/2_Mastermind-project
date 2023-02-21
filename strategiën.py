import itertools
from itertools import combinations

def alle_combinaties():
    """
    Maak alle combinaties mogelijk

    :return: copy van de gemaakte lijst.
    """
    colors = ['a', 'b', 'c', 'd', 'e', 'f']

    combinaties = []

    for combinatie in itertools.combinations_with_replacement(colors, 4):
        combinaties.append(combinatie)

    # for r in range(len(colors) + 1):
    #     for combinatie in itertools.combinations(colors, r):
    #         combinaties.append(combinatie)

    return combinaties


print(len(alle_combinaties()))


def alle_antwoorden():
    """
    Deze functie onthoudt alle al gegeven antwoorden
    :return: copy van de gemaakte lijst
    """


def reduceer_zoekruimte():
    """"""


def simpele_strategie():
    """"""