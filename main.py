# Importação da biblioteca
from random import choice

# Criação da super-classe (classe mãe) 
class ObtendoPalavra:
    # Método para obter palavra de forma aleatória
    def escolher_palavra(self):
        with open(r"C:\\Users\\oscar\\Videos\\Temporário\\Projetos\\Projeto 01 - Jogo da Forca\\Jogo-da-Forca-\\Palavras.txt", "r") as arquivo:
            # Escolher palavra de forma aleatória
            palavra = choice(arquivo.read().split(', '))
            return palavra

# Criação da sub-classe (classe filha)
class JogoForca(ObtendoPalavra): # Inserindo como herça da super-classe

    # Metodo de construir bonequinho
    def bonequinho(self, n):
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
        print('')

    # Método principal
    def jogar(self):
        # Variáveis usadas 
        self.chances = 6
        self.letras_erradas = ''

        # status
        self.status = True

        # Mensagem inicial
        print('')
        print('Seja muito bem-vindo(a) ao Jogo da Forca')  
        print('') 

        # Chamando método palavra escolhida
        self.palavra_escolhida = self.escolher_palavra()
        print('Palavra: ','_ ' * len(self.palavra_escolhida))
        self.construcao_palavra = list('_' * len(self.palavra_escolhida))

        # Loop principal
        while self.status:
            # Método de construção da palavra
            def exibir_construcao_palavra(self):
                print('Palavra: ', ' '.join(self.construcao_palavra))
                print('')

            # Método para o usuário digitar uma letra
            def usuario_digitar_letra(self):
            # Loop de tentativas para letra válida
                while True:
                    self.letra_usuario = input('Digite uma letra: ').lower()

                    # Condicional para ver se é uma letra, se a letra não esta nas letras erradas, se a letra não esta nas letras certas
                    if self.letra_usuario.isalpha() and self.letra_usuario not in self.letras_erradas and self.letra_usuario not in self.construcao_palavra:
                        return self.letra_usuario
                    else:
                        print('Por favor digite uma letra válida!')
                        print('')

            # Método principal
            def metodo_principal(self):
                # Condicional para verificar se a letra do usuário está na palavra escolhida
                if self.letra_usuario in self.palavra_escolhida:
                    # Loop de iteração na palavra escolhida
                    for indice , letra in enumerate(self.palavra_escolhida):
                        # Condicional para verificar se letra usuário e a mesma letra da palavra escolhida
                        if self.letra_usuario == letra:
                            self.construcao_palavra[indice] = self.letra_usuario

                    

                # A letra do usuário não está na palavra escolhida
                else:
                    # Chances
                    self.chances = self.chances - 1
                    print(f'Chances restantes: {self.chances}')

                    # Chamando o método do bonequinho 
                    self.bonequinho(n = self.chances)
                    

                    # Letras erradas 
                    self.letras_erradas += self.letra_usuario
                    print(f'Letras erradas: {self.letras_erradas}')

                # Chamando método exibir a construção da palavra 
                exibir_construcao_palavra(self)
                    
            # Método do status do jogo
            def status_jogo(self):
                if self.palavra_escolhida == ''.join(self.construcao_palavra):
                    print('')
                    print('Parabéns. Você acabou de GANHAR o jogo!!')
                    self.status = False
                # Condicional para ver se o usuário perdeu
                elif self.chances == 0:
                    print('')
                    print('Infelizmente. Você PERDEU o jogo\nMas, pode tentar novamente, boa sorte!')
                    print(f'A palavra era: {self.palavra_escolhida}')
                    self.status = False

            # Chamando método usuário digitar uma letra
            usuario_digitar_letra(self)

            # Chamando método principal
            metodo_principal(self)

            # Chamando método status do jogo
            status_jogo(self)           

teste = JogoForca()
teste.jogar()