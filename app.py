def ceasar2(text,shift):

    res=""

    for i in range(len(text)):
        character=text[i]

        if text.isupper():
            res+=chr((ord(character)+shift-65 )%26+65)


        if text.islower():
            res+=chr((ord(character)+shift-97 )%26+97)
        
        else:
            return res 
    return res

sifre="ahmet"

print(ceasar2(sifre,3))
    




























