import random

kleuren = ['r', 'g', 'y', 'b', 'o', 'p']

max_pogingen = 10

def geheime_code():
    geheime_code = input("(R,G,Y,B,O,P):")

    return list(geheime_code)

def vraagstellen():
    vraag = input("Wat wilt u vragen? (R,G,Y,B,O,P):")
    vraag.capitalize()
    return list(vraag)

def antwoord():
        x = 0
        antwoord = []
        geheim = geheime_code()
        vraag = vraagstellen()
        while True:
            if x == 4:
                return antwoord
            if vraag[x] == geheim[x]:
                antwoord.append('Z')
                x += 1
            elif vraag[x] in geheim:
                antwoord.append('W')
                x += 1
            else:
                antwoord.append('X')
                x += 1


print(antwoord())
