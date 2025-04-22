# Bibliotecas
from random import choice

# Mensagem de Boas-Vindas 
print('*' * 41)
print(' ' * 5, 'Bem-vindo(a) ao Jogo da Forca')
print('*' * 41)

# Função escolher palavra
def palavra_escolhida():

    # Caminho do arquivo palavras.txt
    with open(r"C:/Users/oscar/Videos/Temporário/Projetos\Projeto 01 - Jogo da Forca/Jogo-da-Forca-/Palavras.txt", "r") as arquivo:
        # Adicionei as palavras em uma lista
        palavras = arquivo.read().split(', ')

        # Escolhendo de forma aleatória uma palavra
        palavra_selecionada = choice(palavras)
        return palavra_selecionada

    
# Função do desenho do bonequinho da forca
def bonequinho(n):
    desenho = ["""=============
|        |
|        O
|       /|\\
|        |
|       /\\
|
-------------""",
"""=============
|        |
|        O
|       /|\\
|        |
|        \\
|
-------------""",
"""=============
|        |
|        O
|       /|\\
|        |
|     
|
-------------""",
"""=============
|        |
|        O
|       /|\\
|        
|
|
-------------""",
"""=============
|        |
|        O
|       /|
|
|
|
-------------""",
"""=============
|        |
|        O
|        |   
|       
|       
|
-------------""",
]
    print(desenho[n])
    print(" ")
    
# Função principal 
def jogo_forca():

    # Chamar função (palavra_escolhida()) e guardar em uma variável o resultado
    palavra = palavra_escolhida()

    # Mostrando os tracinhos da palavra
    print(len(palavra) * '_ ')
    palavra_lista = list(len(palavra) * '_')

    # Quantidade de chances
    chances = 6

    # Letras erradas
    letras_erradas = ''

    # Função de construção da palavra
    def construcao_palavra():
        print(f'Palavra: {''.join(palavra_lista)}')
        print('')
    
    # Loop externo
    while True:
    
        # Loop de tentativas para letras válidas
        while True:
            letra_usuario = input('Digite uma letra: ').lower()

            # Usuário digitar uma letra válida
            if letra_usuario.isalpha() and (letra_usuario not in ''.join(palavra_lista) and letra_usuario not in letras_erradas):
                break
            else:
                print('Por favor digite uma letra válida!!')
                print('')
        
        # Condicional para ver a letra do usuário esta na palavra escolhida
        if letra_usuario in palavra: 

            # Loop principal para a construção da palavra 
            for indice, letra in enumerate(palavra):

                # Condicional para letra da palavra ser igual a letra do usuário
                if letra_usuario == letra:
                    palavra_lista[indice] = letra_usuario

            # Chamando a função para exibir a palavra em construção
            construcao_palavra()

        # Condicional, se a letra não estive na palavra
        else:
            # Chances 
            chances = chances - 1
            print(f'Chances restantes: {chances}')

            # Chamando função bonequinho e exibir palavra e construção
            bonequinho(n=chances)
            construcao_palavra()

            # Letras erradas
            letras_erradas = letras_erradas + letra_usuario 
            print(f'Letras erradas: {letras_erradas}')

        # Se o usuário perder todas as suas chances 
        if chances == 0:
            print('')
            print(f'Infelizmente, você PERDEU o jogo.\nA palavra era {palavra}\nMas pode tentar novamente. Boa sorte!')
            break

        # Se o usuário completar a palavra 
        elif palavra == ''.join(palavra_lista):
            print('')
            print('Parabéns, você acabou de GANHAR o jogo!')
            break

jogo_forca()