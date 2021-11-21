from datetime import datetime
import json


def __newPessoa(nome, idade, cpf) -> dict:
    pessoa = {}
    pessoa['nome'] = nome; pessoa['idade'] = idade; pessoa['cpf'] = cpf
    return pessoa


def _newAluno(nome, idade, cpf, cgm, turma, turno) -> dict:
    aluno = __newPessoa(nome, idade, cpf)
    aluno['cgm'] = cgm; aluno['turma'] = turma; aluno['turno'] = turno; aluno['tipo'] = 'aluno'; aluno['cod'] = cgm
    return aluno


def _newProfessor(nome, idade, cpf, salario, formacao, vinculo) -> dict:
    prof = __newPessoa(nome, idade, cpf)
    prof['salario'] = salario; prof['formacao'] = formacao; prof['vinculo'] = vinculo; prof['tipo'] = 'prof'; prof['cod'] = cpf
    return prof


def _newFuncionario(nome, idade, cpf, salario, cargo, horario) -> dict:
    func = __newPessoa(nome, idade, cpf)
    func['salario'] = salario; func['cargo'] = cargo; func['horario'] = horario; func['tipo'] = 'func'; func['cod'] = cpf
    return func


def escola() -> list:
    pessoas = []
    with open('escola.json', 'r') as f:
        x = json.load(f)
        pessoas.append(x)
    return pessoas


def listarTodos(escola) -> None:
    for p in escola:
        for i in p:
            print(i)


def listarAlunos(escola) -> None:
    print('Alunos registrados: ')
    for x in escola:
        for p in x:
            if p['tipo'] == 'aluno':
                print(p)


def listarProfessores(escola) -> None:
    print('Professores registrados: ')
    for x in escola:
        for p in x:
            if p['tipo'] == 'prof':
                print(p)


def listarFuncionarios(escola) -> None:
    print('Funcionários registrados: ')
    for x in escola:
        for p in x:
            if p['tipo'] == 'func':
                print(p)


def _dictParaArquivo(aluno) -> None:
    with open('escola.json', 'r+') as a:
        dados = json.load(a)
        dados.append(aluno)
        with open('escola.json', 'w') as b:
            json.dump(dados, b, indent=4)


def registarAluno() -> None:
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    cpf = input('Digite o CPF: ')
    cgm = input('Digite o CGM: ')
    turma = input('Digite a turma: ')
    turno = input('Digite o turno: ')

    aluno = _newAluno(nome, idade, cpf, cgm, turma, turno)
    _dictParaArquivo(aluno)


def registrarProfessor() -> None:
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    cpf = input('Digite o CPF: ')
    salario = float(input('Digite o salário: ').replace(",", "."))
    formacao = input('Digite a formação: ')
    vinculo = input('Digite o vínculo: ')

    prof = _newProfessor(nome, idade, cpf, salario, formacao, vinculo)
    _dictParaArquivo(prof)


def registrarFuncionario() -> None:
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    cpf = input('Digite o CPF: ')
    salario = input('Digite o salário: ')
    cargo = input('Digite o cargo: ')
    horario = input('Digite o horário de trabalho: ')

    func = _newFuncionario(nome, idade, cpf, salario, cargo, horario)
    _dictParaArquivo(func)


def _lastLog(pessoa) -> None:
    hora = datetime.now()
    with open('ultimo_registro.txt', 'w+') as f:
        f.write(f'{pessoa["tipo"]} {pessoa["nome"]} - {hora}')
    f.close()


def acessarEscola(esc) -> None:
    cod = str(input('Digite o código de acesso: '))
    achou = 0
    for a in esc:
        for b in a:
            if cod == b['cod'] and b['tipo'] == 'prof':
                achou = 1
                print(f'Boa aula Professor(a) {b["nome"]}!')
                _lastLog(b)
            elif cod == b['cod'] and b['tipo'] == 'aluno':
                achou = 1
                print(f'Boa aula Aluno(a) {b["nome"]}!')
                _lastLog(b)
            elif cod == b['cod'] and b['tipo'] == 'func':
                achou = 1
                print(f'Bom trabalho {b["nome"]}!')
                _lastLog(b)
    if achou == 0:
        e = f'Acesso negado! Código {cod} não está na lista!'
        raise Exception(e)


def comandos():
    print('Escola Tal')
    print('Comandos:')
    print('[1] - Registar Novo Aluno')
    print('[2] - Registar Novo Professor')
    print('[3] - Registar Novo Funcionário')
    print('[4] - Listar Todos')
    print('[5] - Listar Alunos')
    print('[6] - Listar Professores')
    print('[7] - Listar Funcionários')
    print('[8] - Acessar Escola')
    print('[0] - Sair')


if __name__ == '__main__':

    rodando = 1
    while rodando:
        esc = escola()
        try:
            comandos()
            comando = int(input('Digite o comando >> '))

            if comando == 1:
                registarAluno()

            elif comando == 2:
                registrarProfessor()

            elif comando == 3:
                registrarFuncionario()

            elif comando == 4:
                listarTodos(esc)

            elif comando == 5:
                listarAlunos(esc)

            elif comando == 6:
                listarProfessores(esc)

            elif comando == 7:
                listarFuncionarios(esc)

            elif comando == 8:
                acessarEscola(esc)

            elif comando == 0:
                rodando = 0

            else:
                raise ValueError('Comando não existe.')

        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)
