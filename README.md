
# Batalha dos Destinos 🎮 

Um jogo simples baseado em texto, criado em Python, onde o jogador controla um herói em uma batalha contra um inimigo. O jogo utiliza classes e herança para modelar os personagens e suas interações.


📋 Descrição do Jogo
No jogo Batalha dos Destinos:

 . O herói possui habilidades especiais e é controlado pelo usuário.
 . O inimigo é o adversário e possui características próprias.
 . O jogador deve escolher entre um ataque normal ou especial e enfrentar o inimigo em um sistema de turnos.
 . O vencedor é definido quando a vida de um dos personagens chega a zero.

🚀 Funcionalidades
 . Classe Mãe Personagem: Base para Heroi e Inimigo.
 . Ataques Normais e Especiais:
 . O ataque normal causa dano baseado no nível do personagem.
 . O ataque especial causa dano adicional ao inimigo.
 . Sistema de Turnos: O herói e o inimigo se alternam nos ataques.
 . Detalhes dos Personagens: Exibição em tempo real de atributos como vida, nível e habilidades.


📁 Estrutura do Projeto

meu_jogo/

│
├── main.py        # Arquivo principal para iniciar o jogo
├── personagem.py  # Classe mãe Personagem
├── heroi.py       # Classe Heroi (controlado pelo usuário)
├── inimigo.py     # Classe Inimigo (adversário)
└── jogo.py        # Classe Jogo que orquestra a batalha

🛠️ Pré-requisitos
 . Python 3.x instalado na máquina.
 . Instalação do Python
 . Caso não tenha o Python instalado, faça o download em:
        https://www.python.org/

▶️ Como Executar o Jogo

1 .Clone este repositório ou baixe os arquivos.

git clone https://github.com/seu-usuario/batalha-dos-destinos.git

2 .Acesse a pasta do jogo:

   cd batalha-dos-destinos

3 .Execute o arquivo principal:
   python main.py

🎮 Como Jogar

Ao iniciar a batalha, os detalhes do Herói e do Inimigo serão exibidos.

    Escolha entre:
    .1 para Ataque Normal
    .2 para Ataque Especial

O inimigo também atacará automaticamente no final do turno.

O jogo termina quando a vida de um dos personagens chegar a zero.

✨ Exemplo de Saída

Iniciando batalha!

Detalhes dos Personagens:
Nome: Super Star 
Vida: 100 
Nível: 5
Habilidade: Super Bola

Nome: Fresno 
Vida: 50 
Nível: 3
Tipo: Rastejante

Pressione Enter para atacar...
Escolha (1 - Ataque Normal, 2 - Ataque Especial): 1
Super Star atacou Fresno e causou 10 de dano!
Fresno atacou Super Star e causou 6 de dano!

...

Super Star venceu a batalha!


🧑‍💻 Tecnologias Utilizadas
    .Python 3: Linguagem principal para o desenvolvimento do jogo.
    .Programação Orientada a Objetos (POO): Uso de classes, herança e métodos.