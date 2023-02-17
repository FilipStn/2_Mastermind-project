import random
# itertools.product

# sla deze functie op in een variabelen
def geheime_code():
    colors = ['a', 'b', 'c', 'd', 'e', 'f']
    # random keuze van 4 elementen uit 'colors'
    choice = random.sample(colors, 4)

    return choice


print(geheime_code())

def start_spel():
    # deze functie moet het spel starten
    print('Welkom bij Mastermind! Je krijgt de opties uit "a, b, c, d, e, f"')

    code = geheime_code()


def opslaan_speelveld():



# def update_speelveld():

# def einde_spel():
