from abc import ABC, abstractmethod

# Classe Abstrata / Interface
class Veiculo(ABC):
    def __init__(self, modelo):
        self.modelo = modelo

    @abstractmethod
    def acelerar(self):
        pass

# Subclasses
class Carro(Veiculo):
    def acelerar(self):
        print(f"O carro {self.modelo} está acelerando rapidamente na pista!")

class Moto(Veiculo):
    def acelerar(self):
        print(f"A moto {self.modelo} dispara velozmente entre os veículos!")

class Caminhao(Veiculo):
    def acelerar(self):
        print(f"O caminhão {self.modelo} ganha força e acelera pesadamente!")

# Desafio de aprofundamento (Bônus)
class CarroEletrico(Veiculo):
    def acelerar(self):
        print(f"O carro elétrico {self.modelo} acelera silenciosamente e com eficiência!")

# Execução Polimórfica (Simulação de Corrida)
def main():
    pista_de_corrida = [
        Carro("Fusca"),
        Moto("Honda CG"),
        Caminhao("Volvo FH"),
        CarroEletrico("Tesla Model 3")  # bônus
    ]

    for veiculo in pista_de_corrida:
        veiculo.acelerar()

if __name__ == "__main__":
    main()
