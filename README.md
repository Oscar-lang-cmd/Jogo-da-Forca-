# 🕹️ Jogo da Forca em Python

Bem-vindo(a) ao repositório do **Jogo da Forca**, desenvolvido em Python!  
Esse projeto foi criado com o objetivo de praticar conceitos básicos e intermediários da linguagem, evoluindo de uma estrutura baseada em **funções** para uma mais robusta com **classes (POO)**.

---

## 📁 Estrutura do Projeto

O repositório contém duas versões principais do jogo:

### ✅ Versão 1 - Usando Funções

📄 Arquivo: `main.py`

Nesta versão, o código foi escrito de forma procedural, utilizando apenas funções.  
É uma ótima introdução ao funcionamento do jogo e à lógica de programação, com leitura de arquivo, controle de fluxo, validação de entrada e uso de listas para representar a palavra.

**Principais características:**

- Organização do código com funções reutilizáveis  
- Exibição visual do bonequinho da forca  
- Leitura das palavras de um arquivo `.txt`  
- Validação das letras digitadas  
- Controle de erros e mensagens amigáveis ao usuário

---

### 🧠 Versão 2 - Usando Classes (Programação Orientada a Objetos)

📄 Arquivo: `main.py`

Nesta versão, o projeto foi reestruturado utilizando **herança e encapsulamento**.  
A lógica do jogo está organizada em classes, promovendo melhor modularização e reutilização de código.

**Principais características:**

- Uso de **herança** com uma superclasse (`ObtendoPalavra`) responsável por obter a palavra aleatória  
- Subclasse (`JogoForca`) que implementa toda a lógica do jogo  
- Métodos internos para digitar letras, verificar condições de vitória/derrota e construir o bonequinho  
- Separação clara das responsabilidades em métodos diferentes

---

## 📚 Arquivo de Palavras

As palavras do jogo estão armazenadas em um arquivo de texto (`Palavras.txt`), e devem estar separadas por vírgulas.

---

## ✨ Desenvolvido por

**Oscar Donizete**  
Estudante de Python com foco em automação e análise de dados 🌱  
Se quiser bater um papo ou sugerir melhorias, fique à vontade para abrir uma issue ou um pull request!

---
