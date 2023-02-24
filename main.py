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
        # deze strategie doet een random keuze uit een lijst
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
    """
    Deze functie roept alle benodigde functies voor de 2e ai vorm op.
    Vervolgens worden de waardes hiervan opgeslagen in variabelen.
    In de while loop herhalen alle stappen zich
    zodat de uiteindelijke ai keuzes minder worden.
    :return: niks
    """
    # start van de pogingen, eerste
    poging = 0
    # de conditie voor de while loop zodat deze blijft lopen
    playing = True
    # hou een lijst bij met alle eerdere pogingen/zetten
    eerdere_pogingen = []
    # genereer een random code om te raden
    geheime_code = speelveld.geheime_code()
    # maak een lijst met alle mogelijke combinaties
    resterende_combinaties = strategiën.alle_combinaties()

    while playing:
        # de functie in deze variabele pakt altijd de eerste index van de resterende combinaties
        huidige_vraag = resterende_combinaties[0]
        # per poging kom er 1 bij poging bovenop
        poging += 1
        # het antwoord wat hoort bij de vergelijking van huidige vraag en de code
        huidige_antwoord = interacties.antwoord(geheime_code, huidige_vraag)
        # de laatste poging wordt toegevoegd aan de lijst 'eerdere_pogingen'
        speelveld.opslaan_speelveld(eerdere_pogingen, poging, huidige_vraag, huidige_antwoord)
        # op basis van de gestelde vraag wordt de lijst met mogelijkheden gereduceerd
        resterende_combinaties = strategiën.reduceer_zoekruimte(resterende_combinaties, huidige_antwoord, huidige_vraag)

        # als deze waarde wijzigt naar False stopt het spel
        playing = speelveld.einde_spel(poging, huidige_antwoord)

    # print de eerdere pogingen onder elkaar
    for p in eerdere_pogingen:
        print(p, end='\n')

    # geeft als de while loop breekt de mogelijkheid opnieuw een spel te kiezen
    kies_game_mode()


# Als de worst case strategie wordt aangeroepen
def ai2_worst_case():
    """
    Deze functie roept alle benodigde functies voor de 2e ai vorm op.
    Vervolgens worden de waardes hiervan opgeslagen in variabelen.
    In de while loop herhalen alle stappen zich
    zodat de uiteindelijke ai keuzes minder worden.
    :return: niks
    """
    # start van de pogingen, eerste
    poging = 0
    # de conditie voor de while loop zodat deze blijft lopen
    playing = True
    # hou een lijst bij met alle eerdere pogingen/zetten
    eerdere_pogingen = []
    # genereer een random code om te raden
    geheime_code = speelveld.geheime_code()
    # maak een lijst met alle mogelijke combinaties
    resterende_combinaties = strategiën.alle_combinaties()

    while playing:
        # als het de eerste poging is doet hij de onderstaande code omdat deze altijd naar bovenkomt als eerst.
        # dit maakt de code een stuk sneller.
        if poging == 0:
            huidige_vraag = ('a', 'a', 'b', 'b')
        #     anders wordt de volgende code gestart
        else:
            # eerst wordt er een frequentie gemaakt en opgeslagen in de variablen
            frequentie_tabel = strategiën.frequentie_tabel(resterende_combinaties)
            # de huidige vraag wordt door de functie 'worst_case_strategie()' bepaald
            huidige_vraag = strategiën.worst_case_strategie(frequentie_tabel)
        # per poging kom er 1 bij poging bovenop
        poging += 1
        # het antwoord wat hoort bij de vergelijking van huidige vraag en de code
        huidige_antwoord = interacties.antwoord(geheime_code, huidige_vraag)
        # de laatste poging wordt toegevoegd aan de lijst 'eerdere_pogingen'
        speelveld.opslaan_speelveld(eerdere_pogingen, poging, huidige_vraag, huidige_antwoord)
        # op basis van de gestelde vraag wordt de lijst met mogelijkheden gereduceerd
        resterende_combinaties = strategiën.reduceer_zoekruimte(resterende_combinaties, huidige_antwoord, huidige_vraag)

        # als deze waarde wijzigt naar False stopt het spel
        playing = speelveld.einde_spel(poging, huidige_antwoord)

    # print de eerdere pogingen onder elkaar
    for p in eerdere_pogingen:
        print(p, end='\n')
    # geeft als de while loop breekt de mogelijkheid opnieuw een spel te kiezen
    kies_game_mode()


# Als de random choice strategie wordt aangeroepen
def ai3_random_choice():
    """
    Deze functie roept alle benodigde functies voor de 3e ai vorm op.
    Vervolgens worden de waardes hiervan opgeslagen in variabelen.
    In de while loop herhalen alle stappen zich
    zodat de uiteindelijke ai keuzes minder worden.
    :return: niks
    """

    # start van de pogingen, eerste
    poging = 0
    # de conditie voor de while loop zodat deze blijft lopen
    playing = True
    # hou een lijst bij met alle eerdere pogingen/zetten
    eerdere_pogingen = []
    # genereer een random code om te raden
    geheime_code = speelveld.geheime_code()
    # maak een lijst met alle mogelijke combinaties
    resterende_combinaties = strategiën.alle_combinaties()

    while playing:
        # deze strategie doet een random keuze uit een lijst
        huidige_vraag = strategiën.eigen_strategie(resterende_combinaties)
        # per poging kom er 1 bij poging bovenop
        poging += 1
        # het antwoord wat hoort bij de vergelijking van huidige vraag en de code
        huidige_antwoord = interacties.antwoord(geheime_code, huidige_vraag)
        # de laatste poging wordt toegevoegd aan de lijst 'eerdere_pogingen'
        speelveld.opslaan_speelveld(eerdere_pogingen, poging, huidige_vraag, huidige_antwoord)
        # op basis van de gestelde vraag wordt de lijst met mogelijkheden gereduceerd
        resterende_combinaties = strategiën.reduceer_zoekruimte(resterende_combinaties, huidige_antwoord, huidige_vraag)

        # als deze waarde wijzigt naar False stopt het spel
        playing = speelveld.einde_spel(poging, huidige_antwoord)

    # print de eerdere pogingen onder elkaar
    for p in eerdere_pogingen:
        print(p, end='\n')

    # geeft als de while loop breekt de mogelijkheid opnieuw een spel te kiezen
    kies_game_mode()


# De start van het spel waar een gamemode wordt gekozen.
def kies_game_mode():
    """
    Deze functie geeft de gebruiker een keuze om de game mode te kiezen om te spelen.
    Aan de hand van die keuze wordt een functie aangeroepen.
    :return: niks
    """
    print('\nWelkom bij Mastermind! \n\nMaak een keuze uit "a, b, c, d, e, f".\n')
    print("Het is mogelijk om de computer het spel te laten oplossen, maar uiteraard is het leuker om zelf te spelen.\n"
          "Hiervoor zijn 3 verschillende algoritmes waar je uit kunt kiezen.\n"
          "Simpele strategie = 'ai1'\n"
          "Worst case strategie = 'ai2'\n"
          "Random choice strategie = 'ai3'\n"
          "Zelf spelen = 'mens'\n"
          "Stop spel = 'stop'")
    game_mode = input('Kies hier voor welke optie je kiest: ').lower()

    # input van game_mode wordt gecheckt met onderstaande opties.
    if game_mode == 'mens':
        gok_mens()
    elif game_mode == 'ai1':
        ai1_strategie_simpel()
    elif game_mode == 'ai2':
        ai2_worst_case()
    elif game_mode == 'ai3':
        ai3_random_choice()
    elif game_mode == 'stop':
        exit()


kies_game_mode()
