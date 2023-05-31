import os


opcao = -1
while opcao != 0:
    opcao = int(input(
        "[1]-> Depósito\n[2]-> Saque\n[3]-> Extrato\n[0]-> Sair\n  Digite sua Escolha.: "))
    if opcao == 1:
        print("\x1b[2J\x1b[1;1H")
        print(" * OPÇÃO DEPÓSITO * ")
        break
    # O B S E R V A Ç Ã O:
    ''' Nos Unixes, e talvez em alguns programas de terminal/prompt do Windows, são reconhecidas as "sequências ANSI" - isso é, o próprio terminal reconhece sequências especiais de caracteres que representam comandos tais como limpar a tela, alterar a cor da fonte, posicionar o cursor -etc - São um "brinquedo" bem interessante - e bem mais simples que o módulo curses do Python(do qual falo abaixo). Para apagar a tela em qualquer terminal Linux ou na maior parte dos Unixes (não sei se no Mac OS X funciona direto) - basta imprimir a sequência "\x1b[2J" - (o "\x1b" é o caractére <ESC> o mesmo código que é gerado pela tecla com esse nome). A sequência <ESC>[ inicia várias sequências ANSI. Para ver as sequências exatas suportadas pelo seu terminal, execute o comando infocmp no shell.
 '''
