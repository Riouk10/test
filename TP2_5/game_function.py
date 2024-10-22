"""
Ce module contient les fonctions utiles au déroulement du jeu ZCasino

"""

import random
from user_function import *

def nbr_roulette() :
    """ Cette fonction choisi un nombre aléatoire entre 0 et 49. """
    nbr_roulette=random.randint(0,49)
    return nbr_roulette

def color_nbr(nbr):
    """ Cette fonction détermine la couleur d'un nombre. Blanc : nombre impair, Noir : nombre pair """
    if nbr % 2 == 0 :
        couleur="Noir"
    else:
        couleur="Blanc"
    return couleur

def rule_zcasino(user_nbr,nbr_roulette):

    """ 
    Cette fonction détermine le statut de la partie de l'utilisateur.
    win : si l'utilisateur a choisi le bon nombre
    
    same_color: si l'utilisateur n'a pas choisi le bon nombre mais un nombre de la même couleur que celle choisi par la roulette
    
    lost : si ni win ni same_color
    
    """
    if user_nbr==nbr_roulette :
        status="win"
        return status
    elif color_nbr(user_nbr)==color_nbr(nbr_roulette):
        status="same_color"
        return status
    else:
        status="lost"
        return status
    
def zcasino(cagnotte_actuelle):
    """
    Cette fonction exécute une partie du jeu ZCasino et met à jour la cagnotte.
    
    Parameters:
        cagnotte_actuelle (int): La cagnotte actuelle du joueur.
    
    Returns:
        int: La nouvelle cagnotte après le jeu.
    """
    
    # Lancement du jeu : choix du nombre de la roulette par l'ordinateur
    nbr = nbr_roulette()
    color = color_nbr(nbr)

    # Participation du joueur : proposition d'un nombre et d'une mise
    user_nbr, user_mise = choix_mise(cagnotte_actuelle)

    # Vérification du statut du jeu (gagné ou perdu)
    status = rule_zcasino(user_nbr, nbr)

    # Mise à jour de la cagnotte selon le résultat
    nouvelle_cagnotte = cagnotte_status(cagnotte_actuelle, user_mise, status)

    # Révélation du résultat de la roulette
    print(f"La roulette avait choisi : {nbr} ({color})")

    return nouvelle_cagnotte