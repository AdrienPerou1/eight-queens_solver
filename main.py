from random import randint
import sym_rotation_reflexion
import time
n = 8


def dansLigne(grille, ligne):
  """
  Fonction qui vérifie si la ligne est libre 
  """
  for i in range(n):
    if grille[ligne][i] == 1:
      return False
  return True


def dansDiagonale(grille, ligne, colonne):
  """
  Fonction qui vérifie si la diagonale est libre 
  """
  # On vérifie la diagonale en haut à gauche
  i = ligne - 1
  j = colonne - 1
  while i >= 0 and j >= 0:
    if grille[i][j] == 1:
      return False
    i -= 1
    j -= 1

  # On vérifie la diagonale en bas à droite
  i = ligne + 1
  j = colonne + 1
  while i < n and j < n:
    if grille[i][j] == 1:
      return False
    i += 1
    j += 1

  # On vérifie la diagonale en haut à droite
  i = ligne - 1
  j = colonne + 1
  while i >= 0 and j < n:
    if grille[i][j] == 1:
      return False
    i -= 1
    j += 1

  # On vérifie la diagonale en bas à gauche
  i = ligne + 1
  j = colonne - 1
  while i < 0 and j >= 0:
    if grille[i][j] == 1:
      return False
    i += 1
    j -= 1
  return True


def dansColonne(grille, colonne):
  """
  Fonction qui vérifie si la colonne est libre 
  """
  for i in range(n):
    if grille[i][colonne] == 1:
      return False
  return True


def afficherGrille(grille, n):
  print("Grille :")
  for i in range(n):
      for j in range(n):
          if grille[i][j] == 1:
              print("Q", end=" ")
          else:
              print("_", end=" ")
      print()
  print()


def backtracking2(grille, numeroReine=1, numeroCase=0):
  #Grille résolue
  if numeroReine == n:
    print("----------------")
    afficherGrille(grille,8)
    return 1
  elif numeroCase!=n*n:
    #On récupère les coordonnées de la case
    ligne = int(numeroCase / n)
    colonne = int(numeroCase % n)

    # On vérifie si la case est libre
    if grille[ligne][colonne] == 0:
      # On essaie de placer un 1
      
      if (dansLigne(grille, ligne) and dansColonne(grille, colonne)
          and dansDiagonale(grille, ligne, colonne)):
        grille[ligne][colonne] = 1
        # On avance dans la grille
        if backtracking2(grille, numeroReine + 1, numeroCase + 1):
          return 1
        # Retour en arrière car échec de l'avancement de la grille
        grille[ligne][colonne] = 0 
        
      # On avance dans la grille
      if backtracking2(grille, numeroReine, numeroCase + 1):
        return 1
        
    else:
      # On avance dans la grille
      if backtracking2(grille, numeroReine, numeroCase + 1):
        return 1
      
  return 0


#############
#   MAIN    #
#############

grille = []
for _ in range(n):
  grille.append([0] * n)

numeroCase = grille[randint(0, 7)][randint(0, 7)] = 1

print("Choisissez l'algorithme à utiliser :")
print("1. Backtracing")
print("2. Symétrie, rotation et réflexion")
choix = input("Entrez votre choix (1 ou 2) : ")

if choix == "1":
    # Appel de la fonction backtracing_2
    start = time.time()
    backtracking2(grille)
    end = time.time()
    elapsed = end - start
    afficherGrille(grille, 8)
elif choix == "2":
    # Appel de la fonction sym_rotation_reflexion.resoudre_8_reines()
    start = time.time()
    solutions = sym_rotation_reflexion.resoudre_8_reines()
    end = time.time()
    elapsed = end - start
    sym_rotation_reflexion.afficher_solutions(solutions, n)
else:
    print("Choix invalide.")

print(f'Temps d\'exécution : {elapsed:.2}ms')






