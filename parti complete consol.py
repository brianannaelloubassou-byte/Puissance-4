#CONSTANTES
NOMBRE_LIGNES = 6
NOMBRE_COLONNES = 7
CASE_VIDE=" "


# FONCTION 1 : créer une grille vide

def creer_grille():
    """
    Crée une grille vide de 6 lignes et 7 colonnes.
    Chaque case contient un espace "   ".
    Retourne la grille.
    """
    grille = []
    for numero_ligne in range(NOMBRE_LIGNES):
        ligne = []
        for numero_colonne in range(NOMBRE_COLONNES):
            ligne.append(CASE_VIDE)
        grille.append(ligne)

    return grille

print("TEST creer_grille ")
grille_test = creer_grille()
print("Grille créée :")
for ligne in grille_test:
    print(ligne)
print()

def afficher_grille(grille):
    """
    Affiche la grille dans la console avec des séparateurs.
    """
    for ligne in grille:
        print("-" * (NOMBRE_COLONNES * 2 + 1))  
        texte_ligne = "|"
        for case in ligne:
            texte_ligne = texte_ligne + case + "|"
        print(texte_ligne)

    print("-" * (NOMBRE_COLONNES * 2 + 1))
    print(" 0 1 2 3 4 5 6")  # indices des colonnes
 
print("TEST afficher_grille ")
afficher_grille(grille_test)
print()

def poser_pion(grille, colonne, pion):
    """
    Place un pion ('J' ou 'R') dans la colonne donnée.
    Le pion tombe dans la première case vide à partir du bas.
    Retourne True si le pion a été placé, False sinon.
    """

    # On commence en bas de la grille
    ligne_actuelle = NOMBRE_LIGNES - 1

    while ligne_actuelle >= 0:
        if grille[ligne_actuelle][colonne] == CASE_VIDE:
            grille[ligne_actuelle][colonne] = pion
            return True
        else:
            ligne_actuelle = ligne_actuelle - 1

    # Si la colonne est pleine
    return False
 
print("TEST poser_pion ")
grille_test = creer_grille()
poser_pion(grille_test, 3, "J")  # colonne 3
poser_pion(grille_test, 3, "R")  # même colonne
afficher_grille(grille_test)
print()

def grille_pleine(grille):
    """
    Vérifie si toutes les cases sont remplies.
    Retourne True si la grille est pleine, False sinon.
    """
    for ligne in grille:
        for case in ligne:
            if case == CASE_VIDE:
                return False
    return True
 
print("TEST grille_pleine ")
grille_test = creer_grille()
print("Grille vide =>", grille_pleine(grille_test))  # Doit afficher False
for i in range(NOMBRE_LIGNES):
    for j in range(NOMBRE_COLONNES):
        grille_test[i][j] = "J"
print("Grille pleine =>", grille_pleine(grille_test))  # Doit afficher True
print()

def verifier_victoire(grille, pion):
    """
    Vérifie si un joueur a 4 pions alignés (horizontalement,verticalement , diagonale)
    Retourne True si le joueur gagne, sinon False.
    """

    # Vérification horizontale
    for ligne in range(NOMBRE_LIGNES):
        for colonne in range(NOMBRE_COLONNES - 3):
            if (grille[ligne][colonne] == pion and
                grille[ligne][colonne + 1] == pion and
                grille[ligne][colonne + 2] == pion and
                grille[ligne][colonne + 3] == pion):
                return True

    # Vérification verticale
    for ligne in range(NOMBRE_LIGNES - 3):
        for colonne in range(NOMBRE_COLONNES):
            if (grille[ligne][colonne] == pion and
                grille[ligne + 1][colonne] == pion and
                grille[ligne + 2][colonne] == pion and
                grille[ligne + 3][colonne] == pion):
                return True

    # Vérification diagonale descendante ️
    for ligne in range(NOMBRE_LIGNES - 3):
        for colonne in range(NOMBRE_COLONNES - 3):
            if (grille[ligne][colonne] == pion and
                grille[ligne + 1][colonne + 1] == pion and
                grille[ligne + 2][colonne + 2] == pion and
                grille[ligne + 3][colonne + 3] == pion):
                return True

    # Vérification diagonale montante ️
    for ligne in range(3, NOMBRE_LIGNES):
        for colonne in range(NOMBRE_COLONNES - 3):
            if (grille[ligne][colonne] == pion and
                grille[ligne - 1][colonne + 1] == pion and
                grille[ligne - 2][colonne + 2] == pion and
                grille[ligne - 3][colonne + 3] == pion):
                return True

    return False

print("TEST verifier_victoire ")
# Cas horizontal
grille_test = creer_grille()
for c in range(4):
    poser_pion(grille_test, c, "J")
afficher_grille(grille_test)
print("Victoire horizontale ?", verifier_victoire(grille_test, "J"))
print()

# Cas vertical
grille_test = creer_grille()
for l in range(4):
    grille_test[NOMBRE_LIGNES - 1 - l][2] = "R"
afficher_grille(grille_test)
print("Victoire verticale ?", verifier_victoire(grille_test, "R"))
print()

def jouer():
    """
    Fonction principale qui gère la partie complète.
    """

    grille = creer_grille()
    joueur1 = input("Nom du joueur 1 (pions jaunes 'J') : ")
    joueur2 = input("Nom du joueur 2 (pions rouges 'R') : ")

    joueur_actuel = joueur1
    pion_actuel = "J"
    partie_terminee = False

    while partie_terminee == False and grille_pleine(grille) == False:
        afficher_grille(grille)
        print(f"\nC’est à {joueur_actuel} de jouer. (Pion : {pion_actuel})")

        try:
            choix = input("Choisis une colonne (0 à 6) :")
            colonne_choisie = int(choix)

            if colonne_choisie < 0 or colonne_choisie >= NOMBRE_COLONNES:
                print("Colonne invalide.")
                continue

            coup_reussi = poser_pion(grille, colonne_choisie, pion_actuel)

            if coup_reussi:
                if verifier_victoire(grille, pion_actuel):
                    afficher_grille(grille)
                    print(f"Félicitations {joueur_actuel}, tu as gagné !")
                    partie_terminee = True
                else:
                    # changement de joueur
                    if pion_actuel == "J":
                        pion_actuel = "R"
                        joueur_actuel = joueur2
                    else:
                        pion_actuel = "J"
                        joueur_actuel = joueur1
            else:
                print("Colonne pleine, rejoue.")

        except ValueError:
            print("Tu dois entrer un nombre entre 0 et 6.")

    if partie_terminee == False:
        afficher_grille(grille)
        print("Match nul ! La grille est pleine")

if __name__ == "__main__":
    print("teste terminés")
    print(" debut de la partie ")
    jouer()
