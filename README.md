# Mastermind Project

Author: Filip Steenbergen

Studentnummer: 1831554

Klas: AI-V1A

In dit project maak ik het spel Mastermind in Python3. Het spel is speelbaar in de Command Line Interface. 

In het bestand 'main.py' staat de werkende code, je hebt alleen wel de andere .py bestanden nodig om de main normaal te kunnen runnen. 
Download alle bestanden en hou dit in 1 directory op je computer. 

Er is ook een mogelijkheid het spel zichzelf te laten oplossen door een van de drie algoritmes die zijn toegevoegd.
De drie algoritmes om te gebruiken zijn:

De simpele strategie: Deze kijkt steeds of de eerste index, index 0, overeenkomt met de code en gaat aan de hand daarvan de lijst met mogelijke combinatie verkleinen en eruit te halen wat overeenkomt met de code en de huidige vraag. Deze stap herhaalt zich tot de code is gevonden of de beurten om zijn. 

De worst case strategie: Deze kijkt wat de combinatie is die de lijst het snelst reduceert om in zo min mogelijk stappen het spel te winnen. 

De random strategie: Deze strategie is een variant op de simpele strategie. Wat deze anders doet is in plaats van de eerste index altijd te controleren, kiest deze een willekeurige combinatie uit de lijst die vervolgens de lijst met combinaties kan reduceren. Het is dus mogelijk dat deze het spel snel wint, maar ook dat hij er langer over doet dan de worst case. 
