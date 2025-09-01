# file_manager.py

import os
import classes

def load_data(file_path, data_class):
    data = []
    if not os.path.exists(file_path):
        return data

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                fields = line.strip().split(';')
                if len(fields) > 0:
                    try:
                        # Converte os campos para os tipos corretos
                        # Exemplo para a classe Aluno:
                        if data_class.__name__ == 'Aluno':
                            record = data_class(
                                codigo=int(fields[0]),
                                nome=fields[1],
                                codigo_cidade=int(fields[2]),
                                data_nascimento=fields[3],
                                peso=float(fields[4]),
                                altura=float(fields[5])
                            )
                        # Adicione o mesmo para as outras classes
                        elif data_class.__name__ == 'Cidade':
                            record = data_class(int(fields[0]), fields[1], fields[2])
                        elif data_class.__name__ == 'Professor':
                            record = data_class(int(fields[0]), fields[1], fields[2], fields[3], int(fields[4]))
                        # etc...
                        
                        data.append(record)
                    except (ValueError, IndexError) as e:
                        print(f"Erro ao ler linha: {line.strip()}. Erro: {e}")
    return data

def save_data(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        for record in data:
            # Converte o objeto de volta para uma string de texto
            if isinstance(record, classes.Aluno):
                f.write(f"{record.codigo};{record.nome};{record.codigo_cidade};{record.data_nascimento};{record.peso};{record.altura}\n")
            # Adicione o mesmo para as outras classes
            elif isinstance(record, classes.Cidade):
                f.write(f"{record.codigo};{record.descricao};{record.estado}\n")
            # etc...