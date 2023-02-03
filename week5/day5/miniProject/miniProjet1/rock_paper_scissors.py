from game import Game
# jeu = Game()
# jeu.play()

# Partie II - Pierre-Papier-Ciseaux.Py

def get_user_menu_choice():
    choix = input("Pour Jouer une nouvelle partie entrez 1\nPour Afficher les scores entrez 2\nPour Quitter tapez 'x' ou 'q': ")
    return choix

def print_results(results):
    print("\tHISTORIQUE\n")
    for x in results:
        print(f"{x} --- Nombre : {results[x]}")

def main():
    results = {
        "win": 0,
        "draw": 0,
        "loss": 0
    }
    while True:
        a = get_user_menu_choice()
        if a == "x" or a == "q":
            print_results(results)
            return 0
        elif a == "1":
            jeu = Game()
            result = jeu.play()
            results.update({result: results[result] + 1})
        elif a == "2":
            print_results(results)
        print("")
main()