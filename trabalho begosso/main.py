# main.py
import os

from classes import Aluno, Cidade, Professor, Modalidade, Matricula
from arvore_binaria import BinarySearchTree
from file_manager import load_data, save_data

# Dicionários para armazenar os índices em memória
indices = {
    'cidades': BinarySearchTree(),
    'alunos': BinarySearchTree(),
    'professores': BinarySearchTree(),
    'modalidades': BinarySearchTree(),
    'matriculas': BinarySearchTree()
}

# Dicionários para armazenar os dados em memória (facilita o acesso)
db = {
    'cidades': [],
    'alunos': [],
    'professores': [],
    'modalidades': [],
    'matriculas': []
}

def carregar_dados_e_indices():
    print("Carregando dados e construindo índices...")
    
def carregar_dados_e_indices():
    # ...
    db['cidades'] = load_data('dados/cidades.txt', Cidade)
    for cidade in db['cidades']:
        indices['cidades'].insert(cidade.codigo, cidade)

    print(f"Total de cidades carregadas: {len(db['cidades'])}")
    if indices['cidades'].root:
        print("Árvore de cidades construída com sucesso.")
    else:
        print("Atenção: A árvore de cidades está vazia.")

    db['alunos'] = load_data('dados/alunos.txt', Aluno)
    for aluno in db['alunos']:
        indices['alunos'].insert(aluno.codigo, aluno)

    # Repita o mesmo para professores, modalidades e matrículas
    print("Dados carregados com sucesso!")

def menu_principal():
    while True:
        print("\n--- Sistema de Gestão de Academia ---")
        print("1. Gerenciar Alunos")
        print("2. Gerenciar Professores")
        print("3. Gerenciar Modalidades")
        print("4. Gerenciar Matrículas")
        print("5. Faturamento por Modalidade")
        print("6. Relatório de Matrículas")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_alunos()
        elif opcao == '0':
            print("Saindo do sistema. Dados salvos.")
            # Salvar todos os dados antes de sair
            save_data('dados/cidades.txt', db['cidades'])
            # etc...
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_alunos():
    while True:
        print("\n--- Menu Alunos ---")
        print("1. Incluir Aluno")
        print("2. Consultar Aluno")
        print("3. Excluir Aluno")
        print("4. Listar todos os Alunos")
        print("0. Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            incluir_aluno()
        elif opcao == '2':
            consultar_aluno()
        elif opcao == '0':
            break

# No arquivo main.py

def incluir_aluno():
    """
    Função para incluir um novo aluno no sistema.
    """
    print("\n--- Inclusão de Novo Aluno ---")
    try:
        # 1. Solicitar os dados do novo aluno
        codigo = int(input("Digite o código do aluno: "))
        
        # Opcional: Verificar se o código já existe
        if indices['alunos'].search(codigo) is not None:
            print(f"Erro: O aluno com o código {codigo} já existe.")
            return

        nome = input("Digite o nome do aluno: ")
        
        # 2. Verificar se a cidade informada existe na base de dados
        while True:
            codigo_cidade = int(input("Digite o código da cidade: "))
            cidade = indices['cidades'].search(codigo_cidade)
            if cidade:
                print(f"Cidade encontrada: {cidade.descricao} ({cidade.estado})")
                break
            else:
                print("Erro: Código de cidade não encontrado. Por favor, tente novamente.")

        data_nascimento = input("Digite a data de nascimento (DD-MM-AAAA): ")
        peso = float(input("Digite o peso em kg (ex: 75.5): "))
        altura = float(input("Digite a altura em metros (ex: 1.75): "))

        # 3. Criar um novo objeto Aluno
        novo_aluno = Aluno(
            codigo=codigo,
            nome=nome,
            codigo_cidade=codigo_cidade,
            data_nascimento=data_nascimento,
            peso=peso,
            altura=altura
        )

        # 4. Adicionar o novo aluno ao nosso "banco de dados" em memória (lista)
        db['alunos'].append(novo_aluno)

        # 5. Adicionar o novo aluno ao nosso índice em Árvore Binária
        # Aqui, a chave é o código e o dado é o próprio objeto Aluno
        indices['alunos'].insert(novo_aluno.codigo, novo_aluno)

        # 6. Salvar as alterações no arquivo para persistência
        save_data('dados/alunos.txt', db['alunos'])

        print("\nAluno incluído com sucesso!")

    except ValueError:
        print("\nErro: Entrada inválida. Certifique-se de que o código, peso e altura são números válidos.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")
def consultar_aluno():
    codigo = int(input("Digite o código do aluno: "))
    aluno = indices['alunos'].search(codigo)
    if aluno:
        # Lógica para exibir os dados do aluno e calcular o IMC
        # Busque a cidade do aluno usando o índice de cidades
        cidade = indices['cidades'].search(aluno.codigo_cidade)
        if cidade:
            print(f"Nome do Aluno: {aluno.nome}")
            print(f"Cidade: {cidade.descricao} ({cidade.estado})")
            # Calcule e exiba o IMC
        else:
            print("Cidade não encontrada.")
    else:
        print("Aluno não encontrado.")


if __name__ == "__main__":
    # Garante que a pasta de dados existe
    if not os.path.exists('dados'):
        os.makedirs('dados')
    
    carregar_dados_e_indices()
    menu_principal()