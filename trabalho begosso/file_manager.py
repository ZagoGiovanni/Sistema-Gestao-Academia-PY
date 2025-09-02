# file_manager.py

import os
import classes

# file_manager.py

def load_data(file_path, data_class):
    data = []
    if not os.path.exists(file_path):
        return data

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                fields = line.strip().split(';')
                
                print(f"Lendo linha: {line.strip()}")
                print(f"Campos encontrados: {fields}") # <--- ADICIONE ESTA LINHA
                
                try:
                    # Converte os campos para os tipos corretos
                    if data_class.__name__ == 'Cidade':
                        record = data_class(int(fields[0]), fields[1], fields[2])
                    # ... (o restante do seu código)
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