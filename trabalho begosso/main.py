class Cidade:
    def __init__(self, codigo, descricao, estado):
        self.codigo = codigo
        self.descricao = descricao
        self.estado = estado

class Aluno:
    def __init__(self, codigo, nome, codigo_cidade, data_nascimento, peso, altura):
        self.codigo = codigo
        self.nome = nome
        self.codigo_cidade = codigo_cidade
        self.data_nascimento = data_nascimento
        self.peso = peso
        self.altura = altura