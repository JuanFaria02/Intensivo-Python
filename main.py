from pprint import pp, pprint
from usuarios import cadastrar_usuarios
from disciplinas import cadastro_disciplinas
import relatorios 

menu = input('Digite o número que indica qual ação deseja realizar:\n(1) Cadastrar Aluno(a)/Professor(a)\n(2) Cadatrar disciplinas\n(3) Relatórios')
print()
if menu == '1':
    dados = {
        "nome": input('Nome: '),
        "genero": input('Gênero (M para masculino e F para feminino): '),
        "cpf": input('Digíte seu CPF: '),
        "data_nascimento": input('Dia: ') + '/' + input('Mês (Apenas números): ') + '/' + input('Ano: '),
        "tipo": input('1 para alunos / 2 para professores: ')
    }

    cadastro = cadastrar_usuarios(dados) #Cadastro será realizado e o número da matrícula gerado
    
    if cadastro[0]: #Se for o primeiro cadastrado
        print("Usuário cadastrado com sucesso!\n")
        pprint(cadastro[1])
    else:
        print(cadastro[1])

elif menu == '2':
    dados = {
        "nome": input('Nome: '),
        "codigo": input('Código: '),
        "semestre": input('Semestre: '),
        "professor": input('Matrícula do professor: '),
        "alunos": list(map(int, input('Digíte as matrículas dos alunos separadas por um espaço em branco: ').split()))
    }
    
    cadastro = cadastro_disciplinas(dados)

    if cadastro[0]: #Se cadastro retornar verdadeiro
        print('Disciplina cadastrada')
        pprint(cadastro[1]) #Imprimir dados
    else: 
        print(cadastro[1]) #Imprimir quais dados foram inválidos

elif menu == '3':
    menu = input('Digite o número correspondente ação que deseja realizar:\n(1) Listar alunos e professores\n(2) Listar Alunos\n(3) Listar Professores')

    if menu == '1':
        pprint(relatorios.listar_usuarios()[1])
    elif menu == '2':
        pprint(relatorios.listar_usuarios(1)[1])
    elif menu == '3':
        pprint(relatorios.listar_usuarios(2)[1])

 