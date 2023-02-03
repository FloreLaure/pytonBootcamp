class Game:
    def get_user_item(self):
        while True:
            choix = input("\npierre ou (1)/papier ou (2)/ciseaux ou (3), quel est votre choix: ")
            if choix == "1":
                choix = "pierre"
            elif choix == "2":
                choix = "papier"
            elif choix == "3":
                choix = "ciseaux"
            if choix == "pierre" or choix == "papier" or choix == "ciseaux":
                return choix.lower()

    def get_computer_item(self):
        import random
        tab = ["pierre", "papier", "ciseaux"]
        return random.choice(tab)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif user_item == "pierre" and computer_item == "ciseaux":
            return "win"
        elif user_item == "ciseaux" and computer_item == "papier":
            return "win"
        elif user_item == "papier" and computer_item == "pierre":
            return "win"
        else:
            return "loss"

    def play(self):
        user = self.get_user_item()
        ordi = self.get_computer_item()
        result = self.get_game_result(user, ordi)
        print(f"Vous avez choisi {user} et l'ordinateur {ordi}.\nResutats : {result}")
        return result