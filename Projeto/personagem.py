class Personagem:  # Classe Mãe
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel

    def set_vida(self, nova_vida):
        self.__vida = nova_vida

    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()} \nVida: {self.get_vida()} \nNível: {self.get_nivel()}"

    def atacar(self, alvo):
        dano = self.__nivel * 2
        alvo.set_vida(alvo.get_vida() - dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")
