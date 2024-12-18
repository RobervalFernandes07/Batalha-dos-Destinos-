from heroi import Heroi
from inimigo import Inimigo

class Jogo:
    """Classe orquestradora do jogo"""
    def __init__(self):
        self.heroi = Heroi(nome="Super Star", vida=100, nivel=5, habilidade="Super Bola")
        self.inimigo = Inimigo(nome="Fresno", vida=50, nivel=3, tipo="Rastejante")

    def iniciar_batalha(self):
        """Gerencia a batalha em turnos"""
        print("Iniciando batalha!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos Personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para atacar...")
            escolha = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial): ")

            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            elif escolha == "2":
                print(f"{self.heroi.get_nome()} usou {self.heroi.get_habilidade()} e deu dano extra!")
                self.heroi.atacar(self.inimigo)
                self.inimigo.set_vida(self.inimigo.get_vida() - 5)  # Dano extra

            # Inimigo ataca de volta
            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)

        # Verificar quem venceu
        if self.heroi.get_vida() > 0:
            print(f"\n{self.heroi.get_nome()} venceu a batalha!")
        else:
            print(f"\n{self.inimigo.get_nome()} venceu a batalha!")
