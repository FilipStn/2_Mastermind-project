import strategiën

def antwoord(code, stel_vraag):
    """
    # Source: https://github.com/peterstark72/mastermind/blob/master/mastermind.py
    Deze code komt van de Github van Lin:
    https://github.com/LinaBlijlevenHU/StructuredProgramming2023/commit/0d7fd46fdc07529685a2e45e80b5258c396816c0
    de maker van de werkende code stat bij source.

    Functie kijkt welke elementen in de code wel en niet goed staan.
    Als ze goed staan returned de functie het aantal zwarte.
    Als ze erin zitten maar niet op de juiste plek het aantal witte.
    Als het helemaal niet goed is wordt er niks gereturned.
    :param code: de geheime code
    :param stel_vraag: de huidige vraag om te controleren
    :return: tupel
    """
    "onder de puntjes staat mijn vorige code die niet helemaal werkend te krijgen was."
    # zwart, wit = 0, 0
    # lst_idx = -1
    # gebruikt = []

    # for element in stel_vraag:
    #     if element in code:
    #         lst_idx = stel_vraag.index(element)
    #         if stel_vraag[lst_idx] == code[lst_idx]:
    #             zwart += 1
    #             gebruikt.append(element)
    # else:
    #     wit += 1

    # for positie in range(len(stel_vraag)):
    #     if stel_vraag[positie] == code[positie]:
    #         zwart += 1
    #         gebruikt.append(positie)
    #
    # code_kopie = code[::]
    # for positie in gebruikt:
    #     code_kopie.remove(code[positie])
    # for i in range(len(stel_vraag)):
    #     if i not in gebruikt:
    #         if stel_vraag[i] in code_kopie:
    #             wit += 1
    #             code_kopie.remove(code[i])
    #
    #
    # return (zwart, wit)


    # Bepaal een set van alle indices bijv. (0, 1, 2, 3)
    positions = set(range(len(code)))

    # Bepaal de posities waar de pinnen al op de goede plek staan.
    black_positions = set(
        [pos for pos, vraag in enumerate(stel_vraag) if vraag == code[pos]])
    # Bepaal hoeveel pinnen al goed staan.
    blacks = len(black_positions)

    # Vergelijk de sets met indices om te kijken welke pinnetjes nog over zijn
    remains_pos = positions - black_positions
    # Selecteer de onderdelen van de code die nog over zijn
    remains = [code[pos] for pos in remains_pos]

    # Teller voor correcte kleur/verkeerde positie pinnetjes
    whites = 0
    # Set van kleuren waar al witte pinnetjes voor uitgedeeld zijn
    awarded_duplicates = set()
    # Voor elke index van een overgebleven pin
    for pos in remains_pos:
        # Bepaal de kleur
        color = stel_vraag[pos]
        # Staat de kleur verderop in de code? Én zijn er minder of even veel van deze kleur in
        # de overgebleven code en de geheime code.
        if color in remains and stel_vraag.count(color) <= code.count(color):
            # Voeg een witte pin toe
            whites += 1
        # Als anders de kleur verderop in de code staat en de kleur nog niet in
        elif color in remains and color not in awarded_duplicates:
            # Voeg een witte pin toe
            whites += 1
            # We kunnen verder geen witte pinnen meer toevoegen voor deze kleur
            awarded_duplicates.add(color)

    # Geef het resultaat terug als tuple
    return (blacks, whites)


def mens_vraag():
    """
    Deze functie vraagt input aan de speler.
    De input wordt gesplit op spaties.

    :return: vraag.split()
    """
    # vraag input van de speler, maakt deze lowercase en stript op overbodige spaties
    vraag = input("Voer hier een mogelijke combinatie in: ").lower().strip()

    # return de vraag met een split op de spatie
    return vraag.split(' ')

