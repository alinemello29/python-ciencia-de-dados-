#Estruturas Condicionais e de Repetição em Python
#Estruturas condicionais

MAIOR_IDADE = 20
IDADE_ESPECIAL = 12

idade = int(input("informe sua idade:"))

if idade >= MAIOR_IDADE:

    print("maior de idade, pode tirar a sua habilitação")

if idade <= MAIOR_IDADE:
    print("maior de idade pode tirar habilitação")
else:
    print("ainda não pode ter habilitação")
    

#segundo exemplo
if idade >= MAIOR_IDADE:
    print("maior de idade, pode tirra a CNH")
elif idade <= IDADE_ESPECIAL:
    print("pode fazer aulas teóricas, mas não pode fazer aulas práticas")
else:
    print("ainda não pode tirar a CNH")

#terceiro exemplo arquivo index12
