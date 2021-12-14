import pickle
from pprint import pprint

'''dados = {
    'nome': 'Prog',
    'codigo': '2001',
    'semestre': '2021.2',
    'professor': '210001',
    'alunos': [2100001, 2100003]
}'''

def cadastro_disciplinas(dados = {}):
    if not dados['nome'] or not dados['codigo'] or not dados['semestre'] or not dados['professor'] or not dados['alunos']:
        return False, 'Preencha todos os campos' 

    try:
        arquivo = open('discplinas.txt', 'rb')
        disciplinas = pickle.load(arquivo)
        arquivo.close()

        disciplinas.append(dados)
        arquivo = open('disciplinas.txt', 'wb')
        pickle.dump(disciplinas, arquivo)
        arquivo.close()
        return True, dados
    except:
        disciplinas = []
        disciplinas.append(dados)
        arquivo = open('disciplinas.txt', 'wb')
        pickle.dump(disciplinas, arquivo)
        arquivo.close()
        return True, dados