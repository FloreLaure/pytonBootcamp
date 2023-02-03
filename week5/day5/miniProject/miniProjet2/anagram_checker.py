class AnagramChecker():
    def __init__(self,nomFic = "mot.txt"):
        with open(nomFic) as f:
            mot = []
            for line in f:
                mot.append(line[0:len(line) - 1])
        self.chaine = mot

    def is_valid_word(self, word):
        if word.upper() in self.chaine:
            return word
        elif word.count(' '):
            # Suppression des espaces blancs en début de phrase
            while True:
                word1 = ''
                if ' ' == word[0]:
                    for i in range(1,len(word)):
                        word1 += word[i]
                    word = word1
                else:
                    break
            # Suppression des espaces blancs en fin de phrase
            while True:
                word2 = ''
                print(word)
                if ' ' == word[-1]:
                    for i in range(0,len(word)-1):
                        word2 += word[i]
                    word = word2
                else:
                    break
            # Nombre de mots: après les traitements ci-dessus, 1 espace blanc signifie qu'il ya au moins deux mots
            if word.count(' '):
                print(f"Error!!! Plus d'un mot:")
                return False
            elif word.upper() in self.chaine:
                return word
        else:
            return False


    def get_anagrams(self, word):
        mots = []
        for mot in self.chaine:
            isAna = True
            if len(word) == len(mot):
                for x in word.upper():
                    if x not in mot:
                        isAna = False
                        break
                if isAna == True and mot != word.upper():
                    mots.append(mot)
        return mots

    def is_anagram(self, word1, word2):
        if len(word1) == len(word2):
            for x in word1.upper():
                if x not in word2.upper():
                    return False
            return True
        return False