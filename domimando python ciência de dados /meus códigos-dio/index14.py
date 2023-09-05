#manipulando strings com python conhecendo métodos úteis da classe string
#Conhecendo métodos úteis da classe string
nome = " aline"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  olá mundo!  "

print(texto + ".")
print(texto.strip()+ ".")
print(texto.rstrip()+ ".")
print(texto.lstrip()+ ".")

menu = "python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("-".join(menu))