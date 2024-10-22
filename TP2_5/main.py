# Importation des fonctions utilisateur et du jeu
from user_function import *
from game_function import *

print("Bienvenue au jeu ZCasino !")

# Initialisation de la cagnotte du joueur
print("Votre cagnotte est de 0€.")
cagnotte_actuelle = depot_cagnotte()


# Boucle de jeu : le joueur joue tant qu'il a de l'argent
while cagnotte_actuelle > 0:
    cagnotte_actuelle = zcasino(cagnotte_actuelle)
    
    if cagnotte_actuelle <= 0:
        print("Votre cagnotte est épuisée. Merci d'avoir joué.")
        break

    # Demander au joueur s'il veut rejouer
    nlle_partie = input("Souhaitez-vous faire une autre partie ? Oui ou Non : ").strip().lower()
    if nlle_partie == "non":
        print(f"Votre cagnotte est de {cagnotte_actuelle}€. Au revoir.")
        break
    elif nlle_partie != "oui":
        print("Réponse non valide, veuillez répondre par Oui ou Non.")

