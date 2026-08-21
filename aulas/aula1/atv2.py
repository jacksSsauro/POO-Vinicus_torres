class Carro(Veiculo):
   def __init__(self, marca, modelo, qtd_portas):
       # Chama o construtor da classe mãe
       super().__init__(marca, modelo)
       self.qtd_portas = qtd_portas