# this is silly 
'''
this is how you make a comment too!
'''
def GiraffeTranslation (random_word):
    translate = ""
    for letter in random_word:
        if letter in "aiueoAIUEO":
            if letter.isupper():
                translate += "G"
            else :
                translate += "g"
        else : 
            translate += letter
    return translate

print(GiraffeTranslation("Ohatever"))
