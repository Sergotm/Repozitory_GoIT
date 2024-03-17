import re
new_text = "Little girl, little girl Why are you crying? Inside your restless soul your heart is dying Little one, little one Your soul is purging Of love and razor blades Your blood is surging Runaway From the river to the street And find yourself with your face in the gutter Your a stray for the salvation army There is no place like home When you got no place to go Little girl, little girl Your life is calling The charlatans and saints of your abandon Little one little one The sky is falling The lifeboat of deception is now sailing In the wake all the way No rhyme or reason Your bloodshot eyes Will show your heart of treason Little girl little girl You dirty liar You're just a junkie Preaching to the choir Runaway To your lost tranquility And find yourself with your face in the gutter Your a stray for the dregs of humanity There is no place like home When you got no place to go The traces of blood Always follow you home Like the Mascara tears From your getaway Your walking with blisters And running with shears So unholy. Sister of grace. Runaway From the river to the street And find yourself with your face in the gutter You're a stray for the salvation army There is no place like home When you got no place to go"
dict_words = {}
dict_reverse = {}
re_sub = re.sub(r"[,!\.\?\;()]", " ", new_text)

for el in re_sub.lower().split():
    # if el in dict_words:
    dict_words[el] = 1 + dict_words.get(el, 0)

list(dict_words.items())
# def aa(element):
#     return element[1]

resort = sorted(dict_words.items(), key=lambda el: el[1])

dict_sorted = dict(resort)   
print(dict_sorted)
    
    















# for word, count in dict_words.items():
#     if count in dict_reverse:
#         dict_reverse[count].append(word)
#     else:
#         dict_reverse[count] = [word]

# for key in sorted(dict_reverse):
#     print(key, dict_reverse[key])