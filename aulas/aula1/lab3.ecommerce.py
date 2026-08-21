class Produto:
   def __init__(self, nome, preco):
       self.nome = nome
       self.preco = preco

   def aplicar_desconto(self, porcentagem):
       desconto = self.preco * (porcentagem / 100)
       self.preco -= desconto
       print(f"Desconto de {porcentagem}% aplicado em {self.nome}!")

class Livro(Produto):
   def __init__(self, nome, preco, autor):
       super().__init__(nome, preco)
       self.autor = autor

class Eletronico(Produto):
   def __init__(self, nome, preco, voltagem):
       super().__init__(nome, preco)
       self.voltagem = voltagem

 