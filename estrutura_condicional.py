print("\n\tEXEMPLOS")
# saldo = 600.0

# saque = float(input("Digite o Valor para Saque.: "))

# USANDO IF SIMPLES
# if saldo >= saque:
#    print("saque altorizado com sucesso!\n retire seu dinheiro")
# if saldo < saque:
#    print("Erro! saque não altorizado")

# USANDO DESVIO PADRÃO
# if saldo >= saque:
#    print("saque altorizado\nretire seu dinheiro")
# else:  # desvio quando só há duas opçoes
#    print("saque não altorizado")

# MAIS DE UM DESVIO
#print("\n******************************")
#print("[ 1 ]--> Depositar")
#print("[ 2 ]--> Sacar")
#print("[ 3 ]--> Extrato")
#print("******************************")
#opcao = int(input("Escolha um Opção.: "))
#if opcao == 1:
#    valor_depositado = float(input("Digite o Valor para Depositar "))
# ...
#elif opcao == 2:
#    valor_sacadp = float(input("Digite o Valor para Sacar "))
# ...
#elif opcao == 3:
#    print("Exibindo Extrato bancário...")
# ...
#else:
#    print("Opção Inválida")


#IFS ANINHADOS
saldo = 1200.0
cheque_especial = 500.0
print("\n******************************")
print("[ 1 ]--> CONTA NORMAL")
print("[ 2 ]--> CONTA UNIVERSITÁRIA")
#print("[ 3 ]--> Extrato")
print("******************************")
opcao = int(input("Escolha o tipo de Conta.: "))
if opcao == 1:
    print("Você Escolheu Conta Normal")
    saque =float(input("Digite o Valor do Saque.: "))
    if saldo >= saque:
        print("saque altorizado pelo banco")
    elif saque <=(saldo + cheque_especial):
        print("Saque altorizado pelo banco com uso do Cheque Especial")
    else:
        print("SALDO INSUFICIENTE!")    
elif opcao == 2:
    print("Você Escolheu Conta Universitária")
    saque =float(input("Digite o Valor do Saque.: "))
    if saldo >= saque:
        print("Saque altorizado pelo banco")
    else:
        print("SALDO INSUFICIENTE!")
else:
    print("Opção Inválida")        

