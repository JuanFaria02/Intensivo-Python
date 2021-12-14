import pickle 
from pprint import pprint

def cadastrar_usuarios(dados = {}):
    if not dados or not dados['nome'] or not dados['cpf'] or not dados['genero'] or not dados['data_nascimento'] or not dados['tipo']:
        return False, 'Digíte todos os dados para realizar o cadastro'

    if len(dados['cpf']) != 11:
        return False, 'Digíte um CPF válido'

    if dados['tipo'] not in ('1', '2'):
        return False, 'Digíte se é Aluno(a) ou professor(a)'

    dados['nome'] = dados['nome'].lower()
    dados['genero'] = dados['genero'].upper()
    dados['tipo'] = int(dados['tipo'])

    if dados['genero'] not in ('M', 'F'):
        return False, 'Gênero inválido (Digíte M para masculino ou F para feminino)!'

    try:
        arquivo = open("usuarios.txt", "rb")
        usuarios = pickle.load(arquivo) #A variavel usuarios vai carregar os dados do arquivo em uma lista
        arquivo.close()
        for user in usuarios:
            if user['cpf'] == dados['cpf']:
                return False, "CPF já cadastrado!"
        dados['matricula'] = usuarios[-1]['matricula'] + 1 #gerador de matriculas

        usuarios.append(dados)
        arquivo = open("usuarios.txt", "wb")
        pickle.dump(usuarios, arquivo)
        arquivo.close()
        return True, dados
    except: #se não houver arquivos
        usuarios = []
        dados['matricula'] = 180001
        usuarios.append(dados) 

        arquivo = open("usuarios.txt", "wb")
        pickle.dump(usuarios, arquivo) #vai adicionar os usuarios no arquivo 
        arquivo.close()
        return True, dados