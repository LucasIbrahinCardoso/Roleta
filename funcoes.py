import random

def potential():
    x = random.randint(0, 100)
    if x >= 0 and x <= 18:
        return "Level 1"
    elif x >= 19 and x <= 45:
        return "Level 2"
    elif x >= 46 and x <= 73:
        return "Level 3"
    elif x >= 74 and x <= 89:
        return "Level 4"
    else:
        return "Level 5"




def nivelador(potencial):
    if "1" in potencial:
        valorPotencial = random.randint(1,21)
        x = ((random.randint(21, 27)/100) * valorPotencial + valorPotencial)    
        if x >= (1) and x < (5.092):
                return "Level 1"
        elif x >= (5.092) and x < (11):
            return "Level 2"
        elif x >= (11) and x < (17.5):
            return "Level 3"
        elif x >= (17.5) and x < (22):
            return "Level 4"
        else:
            return "Level 5"

    elif "2" in potencial:
        valorPotencial = random.randint(1,29)
        x = ((random.randint(21, 27)/100) * valorPotencial + valorPotencial)
        if x >= (1) and x < (7.124):
            return "Level 1"
        elif x >= (7.124) and x < (15.625):
            return "Level 2"
        elif x >= (15.625) and x < (25.755):
            return "Level 3"
        elif x >= (25.755) and x < (31.75):
            return "Level 4"
        else:
            return "Level 5"
        
    elif "3" in potencial:
        valorPotencial = random.randint(1,38)
        x = ((random.randint(21, 27)/100) * valorPotencial + valorPotencial)
        if x >= (1) and x < (8.5):
            return "Level 1"
        elif x >= (8.5) and x < (17.91):
            return "Level 2"
        elif x >= (17.91) and x < (28.41):
            return "Level 3"
        elif x >= (28.41) and x < (38.06):
            return "Level 4"
        else:
            return "Level 5"
        
    elif "4" in potencial:
        valorPotencial = random.randint(2,48)
        x = ((random.randint(21, 27)/100) * valorPotencial + valorPotencial)
        if x >= (1) and x < (9.54):
            return "Level 1"
        elif x >= (9.54) and x < (20.54):
            return "Level 2"
        elif x >= (20.54) and x < (32.04):
            return "Level 3"
        elif x >= (32.04) and x < (47.04):
            return "Level 4"
        else:
            return "Level 5"

    elif "5" in potencial:
        valorPotencial = random.randint(3,60)
        x = ((random.randint(21, 27)/100) * valorPotencial + valorPotencial)
        if x >= (1) and x < (10.514):
            return "Level 1"
        elif x >= (10.514) and x < (14.056):
            return "Level 2"
        elif x >= (14.056) and x < (30.39):
            return "Level 3"
        elif x >= (30.39) and x < (18.73):
            return "Level 4"
        else:
            return "Level 5"        
        
         





        
        



def txt_persona(nome):
    with open (f"./Characters/{nome}.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"Nome: {nome}")

def edit_character(nome, txtadded):
    with open (f"./Characters/{nome}.txt", "a", encoding="utf-8") as nome:
        nome.write(txtadded)




#def py_persona(nome):
#    potencial = potential()
#    with open (f"Character.py", "a") as croba:
#        croba.write(
#            "\n" + nome + " = { 'Nome' : '" + nome + "', 'Potencial' : '" + potencial + "' }" 
#        )



