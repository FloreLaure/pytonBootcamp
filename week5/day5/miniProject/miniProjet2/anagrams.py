from anagram_checker import AnagramChecker as Ana
while True:
    choix = input("\n(s)aisir ou (q)uitter\nQuel est votre choix: ")
    print("")
    if choix.lower() == "s":
        test = Ana()
        mot = test.is_valid_word(input("Entrez votre mot: "))
        if mot:
            print(mot)
            print(test.get_anagrams(mot))
            if test.is_anagram(mot, "TAME"):
                print(f"\nteam est un anagramme de {mot}")
            else:
                print(f"\nteam n'est pas un anagramme de {mot}")
    elif choix.lower() == "q":
        break
    else:
        print("Entrez s ou q")