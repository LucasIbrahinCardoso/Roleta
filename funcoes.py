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



