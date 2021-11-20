import json


def __newPessoa(nome, idade, cpf) -> dict:
    pessoa = {}
    pessoa['nome'] = nome; pessoa['idade'] = idade; pessoa['cpf'] = cpf
    return pessoa


def _newAluno(nome, idade, cpf, cgm, turma, turno) -> dict:
    aluno = __newPessoa(nome, idade, cpf)
    aluno['cgm'] = cgm; aluno['turma'] = turma; aluno['turno'] = turno; aluno['tipo'] = 'aluno'
    return aluno


def _newProfessor(nome, idade, cpf, salario, formacao, vinculo) -> dict:
    prof = __newPessoa(nome, idade, cpf)
    prof['salario'] = salario; prof['formacao'] = formacao; prof['vinculo'] = vinculo; prof['tipo'] = 'prof'
    return prof


def _newFuncionario(nome, idade, cpf, salario, cargo, horario) -> dict:
    func = __newPessoa(nome, idade, cpf)
    func['salario'] = salario; func['cargo'] = cargo; func['horario'] = horario; func['tipo'] = 'func'
    return func


def escola() -> list:
    pessoas = []
    with open('escola.json', 'r') as f:
        x = json.load(f)
        pessoas.append(x)
    return pessoas


def addEscola(escola, pessoa) -> None:
    escola.append(pessoa)


def listarTodos(escola) -> None:
    for p in escola:
        for i in p:
            print(f'{i}\n')


def listarAlunos(escola) -> None:
    print('Alunos registrados: ')
    for x in escola:
        for p in x:
            if p['tipo'] == 'aluno':
                print(p)
    print('\n')


def listarProfessores(escola) -> None:
    print('Professores registrados: ')
    for x in escola:
        for p in x:
            if p['tipo'] == 'prof':
                print(p)
    print('\n')


def listarFuncionarios(escola) -> None:
    print('Funcionários registrados: ')
    for x in escola:
        for p in x:
            if p['tipo'] == 'func':
                print(p)
    print('\n')


def _dictParaArquivo(aluno) -> None:
    with open('escola.json', 'r+') as a:
        dados = json.load(a)
        dados.append(aluno)
        with open('escola.json', 'w') as b:
            json.dump(dados, b, indent=4)


def registarAluno(escola) -> None:
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    cpf = input('Digite o CPF: ')
    cgm = input('Digite o CGM: ')
    turma = input('Digite a turma: ')
    turno = input('Digite o turno: ')

    aluno = _newAluno(nome, idade, cpf, cgm, turma, turno)
    _dictParaArquivo(aluno)
    addEscola(escola, aluno)


def registrarProfessor(escola) -> None:
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    cpf = input('Digite o CPF: ')
    salario = float(input('Digite o salário: ').replace(",", "."))
    formacao = input('Digite a formação: ')
    vinculo = input('Digite o vínculo: ')

    prof = _newProfessor(nome, idade, cpf, salario, formacao, vinculo)
    _dictParaArquivo(prof)
    addEscola(escola, prof)


def registrarFuncionario(escola) -> None:
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    cpf = input('Digite o CPF: ')
    salario = input('Digite o salário: ')
    cargo = input('Digite o cargo: ')
    horario = input('Digite o horário de trabalho: ')

    func = _newFuncionario(nome, idade, cpf, salario, cargo, horario)
    _dictParaArquivo(func)
    addEscola(escola, func)


if __name__ == '__main__':

    esc = escola()
    print('Programação Estruturada')
    print('Sistema Escola - V: 0.0.1\n')

    rodando = 1
    while rodando:

        print('Escola Tal')
        print('Comandos:')
        print('[1] - Registar Novo Aluno')
        print('[2] - Registar Novo Professor')
        print('[3] - Registar Novo Funcionário')
        print('[4] - Listar Todos')
        print('[5] - Listar Alunos')
        print('[6] - Listar Professores')
        print('[7] - Listar Funcionários')
        print('[0] - Sair')

        comando = int(input('Digite o comando: '))

        if comando == 1:
            registarAluno(esc)

        elif comando == 2:
            registrarProfessor(esc)

        elif comando == 3:
            registrarFuncionario(esc)

        elif comando == 4:
            listarTodos(esc)

        elif comando == 5:
            listarAlunos(esc)

        elif comando == 6:
            listarProfessores(esc)

        elif comando == 7:
            listarFuncionarios(esc)

        elif comando == 0:
            rodando = 0

        else:
            raise ValueError('Comando não existe.')
