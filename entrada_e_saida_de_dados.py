nome = input("Digite seu Nome.: ")
ano_nascimento = input("Informe seu ano de nascimento.: ")
idade = 2023 - int(ano_nascimento)
print("Olá ", nome.upper(), " Como vai hen", end="...")
print("Sua idade é ", idade, sep="#")
print("O tipo da variável ano_nascimento que contém o valor: ",
      ano_nascimento, " é o seguinte: ", type(ano_nascimento))
