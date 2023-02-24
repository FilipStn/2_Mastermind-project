import speelveld
import interacties
import strategiën



# Als een mens speelt
def gok_mens():

    poging = 0
    playing = True
    eerdere_pogingen = []
    geheime_code = speelveld.geheime_code()

    while playing:
        huidige_vraag = interacties.mens_vraag()
        # print(huidige_vraag)
        huidige_antwoord = interacties.antwoord(geheime_code, huidige_vraag)
        # print(huidige_antwoord)
        poging += 1
        speelveld.opslaan_speelveld(eerdere_pogingen, poging, huidige_vraag, huidige_antwoord)
        for p in eerdere_pogingen:
            print(p, end='\n')
        # speelveld.displayboard(eerdere_pogingen)
        playing = speelveld.einde_spel(poging, geheime_code, huidige_vraag)

    kies_game_mode()

# Als de simpele strategie wordt aangeroepen
def ai1_strategie_simpel():
    poging = 0
    playing = True
    eerdere_pogingen = []
    geheime_code = speelveld.geheime_code()
    resterende_combinaties = strategiën.alle_combinaties()
    while playing:
        huidige_vraag = resterende_combinaties[0]
        poging+=1
        # print(huidige_vraag)
        huidige_antwoord = interacties.antwoord(geheime_code, huidige_vraag)
        # print(huidige_antwoord)
        speelveld.opslaan_speelveld(eerdere_pogingen, poging, huidige_vraag, huidige_antwoord)
        resterende_combinaties = strategiën.reduceer_zoekruimte(resterende_combinaties, huidige_antwoord, huidige_vraag)
        # speelveld.displayboard(eerdere_pogingen)
        playing = speelveld.einde_spel(poging, huidige_antwoord)
    for p in eerdere_pogingen:
        print(p, end='\n')
    kies_game_mode()


def ai2_strategie_simpel():
    poging = 0
    playing = True
    eerdere_pogingen = []
    geheime_code = speelveld.geheime_code()
    resterende_combinaties = strategiën.alle_combinaties()
    while playing:
        if poging == 0:
            huidige_vraag = ('a', 'a', 'b', 'b')
        else:
            frequentie_tabel = strategiën.frequentie_tabel(resterende_combinaties)
            huidige_vraag = strategiën.worst_case_strategie(frequentie_tabel)
        poging += 1
        # print(huidige_vraag)
        huidige_antwoord = interacties.antwoord(geheime_code, huidige_vraag)
        # print(huidige_antwoord)
        speelveld.opslaan_speelveld(eerdere_pogingen, poging, huidige_vraag, huidige_antwoord)
        resterende_combinaties = strategiën.reduceer_zoekruimte(resterende_combinaties, huidige_antwoord, huidige_vraag)
        # speelveld.displayboard(eerdere_pogingen)
        playing = speelveld.einde_spel(poging, huidige_antwoord)
    for p in eerdere_pogingen:
        print(p, end='\n')
    kies_game_mode()

def ai3_strategie_simpel():
    """
    Deze functie roept alle
    :return: niks
    """
    poging = 0
    playing = True
    eerdere_pogingen = []
    geheime_code = speelveld.geheime_code()
    resterende_combinaties = strategiën.alle_combinaties()
    while playing:
        huidige_vraag = strategiën.eigen_strategie(resterende_combinaties)
        poging+=1
        # print(huidige_vraag)
        huidige_antwoord = interacties.antwoord(geheime_code, huidige_vraag)
        # print(huidige_antwoord)
        speelveld.opslaan_speelveld(eerdere_pogingen, poging, huidige_vraag, huidige_antwoord)
        resterende_combinaties = strategiën.reduceer_zoekruimte(resterende_combinaties, huidige_antwoord, huidige_vraag)
        # speelveld.displayboard(eerdere_pogingen)
        playing = speelveld.einde_spel(poging, huidige_antwoord)
    for p in eerdere_pogingen:
        print(p, end='\n')
    kies_game_mode()

def kies_game_mode():
    print('Welkom bij Mastermind! Je krijgt de opties uit "a, b, c, d, e, f".\n'
          'Bij dit spel is het de bedoeling de code te kraken door de juiste combinatie te maken.')
    print("Het is mogelijk om de computer het spel te laten oplossen, maar uiteraard is het leuker om zelf te spelen."
          "Hiervoor zijn 3 verschillende algoritmes waar je uit kunt kiezen.\n"
          "Door in kleine letters 'ai1', 'ai2', 'ai3' of 'mens' te typen maak je een keuze")
    game_mode = input('Kies hier voor welke optie je kiest: ').lower()

    if game_mode == 'mens':
        gok_mens()
    elif game_mode == 'ai1':
        ai1_strategie_simpel()
    elif game_mode == 'ai2':
        ai2_strategie_simpel()
    elif game_mode == 'ai3':
        ai3_strategie_simpel()


kies_game_mode()
