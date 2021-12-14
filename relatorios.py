import pickle
from pprint import pprint

def listar_usuarios(tipo = 0, genero = '', ordenar = ''):
    try:
        arquivo = open('usuarios.txt', 'rb')
    except:
        return False, 'Arquivo com usuarios não existe'

    usuarios = pickle.load(arquivo)
    arquivo.close()

    if not usuarios:
        return False, 'Não existem usuarios cadastrados'
    elif not tipo and not genero and not ordenar:
        return True, usuarios
    
    usuarios_filtrados = []
    if tipo:
        usuarios_filtrados = [usuario for usuario in usuarios if usuario['tipo'] == tipo]
    if genero:
        if not usuarios_filtrados:
            usuarios_filtrados = [usuario for usuario in usuarios if usuario['genero'] == genero.upper()]
        else:
            usuarios_filtrados = [usuario for usuario in usuarios if usuario['genero'] == genero]
    if ordenar:
        if not tipo and not genero:
            if ordenar == 1: 
                usuarios_filtrados = sorted(usuarios, key = lambda k: k['nome'])
            else:
                usuarios_filtrados = sorted(usuarios, key = lambda k: k['nome'])
        else:
            if ordenar == 1:
                usuarios_filtrados = sorted(usuarios_filtrados, key=lambda k: k['nome'])
            else:
                usuarios_filtrados = sorted(usuarios_filtrados, key=lambda k: k['data_nascimento'])
    if not usuarios_filtrados:
        return False, 'Nenhum identificado'
    return True, usuarios_filtrados