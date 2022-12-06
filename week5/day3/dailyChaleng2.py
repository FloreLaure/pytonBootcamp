from translate import Translator
translator= Translator(to_lang="en",from_lang="fr")
french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
english_words= {}
for x in french_words:
    english_words.update({x : translator.translate(x)})
print(english_words)