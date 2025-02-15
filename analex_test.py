import pytest
import subprocess
import shlex
import os, fnmatch

import analex

# Definindo os casos de teste
test_cases = [("", "-k"), ("teste.c", "-k"), ("notexists.cm", "-k")]

# Adicionando os arquivos .cm encontrados na pasta 'tests'
for file in fnmatch.filter(os.listdir('tests'), '*.cm'):
    test_cases.append((file, "-k"))

@pytest.mark.parametrize("input_file, args", test_cases)
def test_execute(input_file, args):
    if input_file != '':
        path_file = 'tests/' + input_file
    else:
        path_file = ""
    
    # Construindo o comando
    cmd = "python analex.py {0} {1}".format(args, path_file)
    process = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Executando o processo e obtendo a saída
    stdout, stderr = process.communicate()

    # Remover o \r da saída gerada e normalizar as quebras de linha
    generated_output = stdout.decode("utf-8").replace('\r', '').strip()

    # Ler a saída esperada do arquivo
    path_file = 'tests/' + input_file
    output_file = open(path_file + ".lex.out", "r")

    # Ler o conteúdo do arquivo de saída esperado e remover espaços extras
    expected_output = output_file.read().strip()

    output_file.close()

    # Imprimir as saídas para depuração
    print("Generated output:")
    print(generated_output)
    print("Expected output:")
    print(expected_output)

    # Comparando a saída gerada com a saída esperada
    assert generated_output == expected_output
