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
    potenGuardado = funcoes.potential()
    funcoes.edit_character(f"{lilname}",f",Potential: {potenGuardado},")
    guardador = funcoes.nivelador(potenGuardado)

    funcoes.edit_character(lilname, f"Str: {funcoes.nivelador(potenGuardado)},")
    funcoes.edit_character(lilname, f"BattleIQ: {funcoes.nivelador(potenGuardado)},")
    funcoes.edit_character(lilname, f"Dex: {funcoes.nivelador(potenGuardado)},")
    funcoes.edit_character(lilname, f"Velo: {funcoes.nivelador(potenGuardado)},")
    funcoes.edit_character(lilname, f"Mana: {funcoes.nivelador(potenGuardado)},")
    funcoes.edit_character(lilname, f"Durab: {funcoes.nivelador(potenGuardado)},")
    funcoes.edit_character(lilname, f"Pow: {funcoes.nivelador(potenGuardado)},")
    funcoes.edit_character(lilname, f"PTechnic: {funcoes.nivelador(potenGuardado)},")
    funcoes.edit_character(lilname, f"BTechnic: {funcoes.nivelador(potenGuardado)},")
