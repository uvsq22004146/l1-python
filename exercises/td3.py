#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    temps =  (temps[0], temps[1], temps[2], temps[3])
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    secondes = (temps[3] + temps[2]*60 + temps[1]*60*60 + temps[0]*24*60*60)

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jour = seconde // (24*60*60)
    seconde = seconde % (24*60*60)
    heure = seconde // (60*60)
    seconde = seconde % (60*60)
    minute = seconde * 60
    seconde = seconde % 60
    return (jour, heure, minute, seconde)

temps = secondeEnTemps(100000)
print(temps[0], "jours", temps[1], "heures", temps[2], "minutes", temps[3], "secondes")


#fonction auxiliaire ici
def affiche_pluriel(valeur,mot) :
    if(valeur != 0):
        print(valeur, "", end="")
        print(mot, end="")
        if(valeur > 1):
            print("s", end="")

def afficheTemps(temps) :
    affiche_pluriel(temps[0], "jour")
    affiche_pluriel(temps[1], "heure")
    affiche_pluriel(temps[2], "minute")
    affiche_pluriel(temps[3], "seconde")
    
afficheTemps((1, 0, 14, 23))    


def sommeTemps(temps1, temps2):
    return secondeEnTemps(tempsEnSeconde(temps1) + tempsEnSeconde(temps2))

sommeTemps((2,3,4,25), (5,22,57,1))
