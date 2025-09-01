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
class Professores:
    def __init__(self, codigo, nome, endereco, telefone, codigo_cidade):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.codigo_cidade = codigo_cidade

class Modalidade:
    def __init__(self, codigo, descricao, codigo_professor, valor_aula, limite_alunos, total_alunos):
        self.codigo = codigo
        self.descricao = descricao
        self.codigo_professor = codigo_professor
        self.valor_aula = valor_aula
        self.limite_alunos = limite_alunos
        self.total_alunos = total_alunos

class Matricula:
    def __init__(self, codigo, codigo_aluno, codigo_modalidade, data_matricula, quantidade_aulas):
        self.codigo = codigo
        self.codigo_aluno = codigo_aluno
        self.codigo_modalidade = codigo_modalidade
        self.qtdde_aulas = quantidade_aulas
        