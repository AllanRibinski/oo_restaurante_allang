class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f"Carro: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}"

# Criando uma instância da classe Carro
carro1 = Carro('Ferrari', 'Vermelho', 2008)
print(carro1)





# Classe Restaurante
class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.endereco = None
        self.capacidade = 0

    def __str__(self):
        return f"Restaurante: {self.nome}, Categoria: {self.categoria}, Ativo: {self.ativo}, Endereço: {self.endereco}, Capacidade: {self.capacidade}"

restaurante1 = Restaurante('Bombaxa', 'Gourmet')
restaurante1.endereco = 'Av Paulista, 152'
restaurante1.capacidade = 300
print(restaurante1)

# Criando uma instância da classe Restaurante utilizando o construtor
restaurante2 = Restaurante('Bon LaVida', 'Francesa')
print(restaurante2)





# Classe Cliente
class Cliente:
    def __init__(self, nome, email, telefone, endereco):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def __str__(self):
        return f"Cliente: {self.nome}, Email: {self.email}, Telefone: {self.telefone}, Endereço: {self.endereco}"

# Instanciando 3 objetos da classe Cliente e atribuindo valores aos seus atributos
cliente1 = Cliente('Miguel Carvalho', 'MiguelCarvalho@example.com', '1224-7678', 'Rua A, 130')
cliente2 = Cliente('Joana Ferrerira', 'JoanaFerrerira@example.com', '9704-4321', 'Rua D, 210')
cliente3 = Cliente('Carlos Alberto', 'CarlosAlberto@example.com', '3302-3344', 'Rua E, 174')

print(cliente1)
print(cliente2)
print(cliente3)