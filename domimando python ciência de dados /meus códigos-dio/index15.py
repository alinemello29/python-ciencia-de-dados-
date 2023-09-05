#Interpolação de variáveis

nome = "aline melo"
idade = 26
profissao = "programador"
linguagem = "python"
saldo = 7.000

dados = {"nome": "aline melo", "idade": 26}

print("nome: %s Idade: %d" % (nome, idade))

print("nome: {} Idade: {}".format(nome, idade))

print("nome: {1} Idade: {0}".format(idade, nome))
print("nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

print("nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
print("nome: {nome} Idade: {idade}".format(**dados))

print(f"nome: {nome} Idade: {idade}")
print(f"nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")