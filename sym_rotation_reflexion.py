def resoudre_8_reines():
  solutions = []

  def est_valide(grille, ligne, colonne):
    """ Vérifie la ligne est les diagonales de la grille"""
    for i in range(ligne):
      if grille[i] == colonne or grille[i] - i == colonne - ligne or grille[
          i] + i == colonne + ligne:
        return False
    return True

  def placer_reines(grille, ligne):
    if ligne == 8:  # Toutes les reines sont placées
      solutions.append(grille[:])  # Copie la grille
      return
    for colonne in range(8):
      if est_valide(grille, ligne, colonne):
        grille[
            ligne] = colonne  # Place la reine à la colonne valide de la ligne
        placer_reines(grille, ligne + 1)

  placer_reines(
      [0] * 8, 0
  )  # Initialise une grille vide de 8x8 en commençant par la première ligne

  toutes_solutions = []
  for solution in solutions:
    toutes_solutions.append(solution)
    for i in range(7):
      nouvelle_solution = [
          solution[(j + 1) % 8] for j in range(8)
      ]  # Effectue une rotation sur une solution à partir de i
      toutes_solutions.append(nouvelle_solution)
      nouvelle_solution = [
          7 - x for x in nouvelle_solution
      ]  # Effectue une réflexion sur une solution à partir de x
      toutes_solutions.append(nouvelle_solution)

  return toutes_solutions


def afficher_solutions(solutions, n=8):
  cpt = 0
  for solution in solutions:
    print("Solution :")
    cpt += 1
    for i in range(n):
      for j in range(n):
        if j == solution[i]:
          print("Q", end=" ")
        else:
          print("_", end=" ")
      print()
    print()
  print(cpt, "solutions trouvées")
