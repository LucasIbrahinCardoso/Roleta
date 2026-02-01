import funcoes

creation_running = False
battle = False

print("Wellcome to Character Creator!!\n\n")

while True:
    print("What do you want? \n\n 1) To create a new character; \n 2) To make a battle between characters \n?")
    resposta1 = input("(Respond with 1 or 2)\nR: ")
    if resposta1 != '1' and resposta1 != '2':
        print("\n\n    Respond with: 1 or 2\n\n")
    else:
        break
if resposta1 == "1":
    creation_running = True
else:
    battle = True

if creation_running:
    lilname = input("\nType your character name.\nR: ")
    funcoes.txt_persona(lilname)
    funcoes.edit_character(f"{lilname}",f",Potential: {funcoes.potential()}")
    funcoes.edit_character(f"{lilname}", ",Str:Level 3")
