"""Ce module contient toutes fonctions relatives au joueur"""

def depot_cagnotte():
    """
    Cette fonction permet de déposer de l'argent sur la cagnotte de l'utilisateur
    """
    while True :
        try :
            montant_depose = int(input("Veuillez saisir le montant que vous souhaitez déposer sur votre cagnotte : "))
            if montant_depose >= 10 :
                print (f"Votre Cagnotte actuelle est de {montant_depose}€")
                return montant_depose  

            else :
                print("La mise minimum est de 10€")
                
        except ValueError:
            print("Veuillez saisir un montant valide.")

def cagnotte_status(cagnotte_actuelle, mise, status):
    """
    Met à jour la cagnotte du joueur en fonction de l'issue de la partie.
    
    Parameters:
        cagnotte_actuelle (int): La cagnotte actuelle du joueur.
        mise (int): Le montant misé par le joueur.
        status (str): Le statut du résultat de la partie ("win", "same_color", ou "Lost").
    
    Returns:
        int: La nouvelle cagnotte du joueur après la mise à jour.
    """

    gain_multiplicateur = 3
    remboursement_same_color = 0.5
    
    #mise à jour de la cagnotte selon le statut
    if status == "win" :
        nouvelle_cagnotte = (cagnotte_actuelle - mise) + (mise * gain_multiplicateur)
        print(f"Bravo ! Vous avez gagné {mise * gain_multiplicateur}€. Nouvelle cagnotte : {nouvelle_cagnotte}€")

    elif status == "same_color" : 
        nouvelle_cagnotte = (cagnotte_actuelle - mise) + (mise * remboursement_same_color)
        print(f"Vous avez perdu mais la couleur est la même. Vous récupérez la moitié de votre mise. Nouvelle cagnotte : {nouvelle_cagnotte}€")

    elif status == "lost" :
        nouvelle_cagnotte = cagnotte_actuelle - mise
        print(f"Désolée, vous avez perdu {mise}€. Nouvelle cagnotte : {nouvelle_cagnotte}€")

    else :
        nouvelle_cagnotte = cagnotte_actuelle
        print(f"Votre cagnotte est de : {nouvelle_cagnotte}€")

    return nouvelle_cagnotte

def choix_mise(cagnotte_actuelle):
    """ Cette fonction permet au joueur de choisir un nombre en 0 et 49 et de placer une mise"""

    while True :
        try :
            choix_nombre = int(input("Veuillez choisir un nombre entre 0 et 49 : "))
            if 0 <= choix_nombre <= 49 :
                break
            else :
                print("Le nombre doit être entre 0 et 49.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    while True :
        try :
            montant_mise = int(input(f"Combien souhaitez vous miser sur le numéro {choix_nombre} ? : "))

            #vérification que la mise ne dépasse pas la cagnotte actuelle
            if montant_mise > cagnotte_actuelle :
                print(f"Erreur : la mise de {montant_mise} dépasse la cagnotte disponible ({cagnotte_actuelle}).")

            elif montant_mise > 0 :
                break
            else : 
                print("La mise doit être positive")
        except ValueError:
            print("Veuillez entrer une mise valide")

    return choix_nombre, montant_mise

#input_user = choix_mise()
#print(input_user)
#cagnotte_joueur=500
#cagnotte_joueur=cagnotte(cagnotte_joueur,100,"win")