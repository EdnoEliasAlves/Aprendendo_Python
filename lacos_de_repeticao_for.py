
# texto = input("Digite um Texto... ")
# vogais = "AEIOU"

# for letra in texto:
# if letra.upper() in vogais:
# print(letra, end="")


lista = list(range(10))
# print(lista)


# for numero in range(0, 11):
# print(numero, end=" - ")
print()
print()
print()
fator = int(input("Informe um Número para Tabuada.: "))
for numero in range(0, 11):
    print(f"{fator} X {numero} = {fator * numero}", end="\n")
