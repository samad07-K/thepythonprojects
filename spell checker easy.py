from spellchecker import SpellChecker
spell=SpellChecker()
while True:
    word=str(input("enter the choice "))
    if word in spell:
        print("The spelling is correct")
    else:
        k=spell.correction(word)
        print(k,"Is the correct spelling:")
        continue
