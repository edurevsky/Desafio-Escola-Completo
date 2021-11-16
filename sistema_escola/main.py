from __init__ import *


escola = Escola()


def cabecalio():
    print('='*47)
    print(f'{escola.getEscNome}')
    print('='*47)
    print('O que deseja fazer?')
    print('[1] - Registar Novo Aluno')
    print('[2] - Registrar Novo Professor')
    print('[3] - Registrar Novo Funcionário')
    print('[4] - Listar Todos')
    print('[5] - Acessar Escola')
    print('[6] - Listar ALUNOS')
    print('[7] - Listar PROFESSORES')
    print('[8] - Listar FUNCIONÁRIOS')
    print('[9] - Sair')
    print('='*47)


def registarNovoAluno():

    nome = input('Digite o nome do aluno: ')
    cpf = input('Digite o CPF do aluno: ')
    rg = input('Digite o RG do aluno: ')
    dataNascimento = input('Digite a data de nascimento do aluno: ')
    cgm = input('Digite o CGM do aluno: ')
    turma = input('Digite a turma do aluno: ')
    turno = input('Digite o turno do aluno: ')

    aluno = Aluno(nome, cpf, rg, dataNascimento, cgm, turma, turno)
    AlunoDAO().salvar(aluno)
    escola.addLista(aluno)

    print('Aluno Registrado com Sucesso.')


def registrarNovoProfessor():

    nome = input('Digite o nome do professor: ')
    cpf = input('Digite o CPF do professor: ')
    rg = input('Digite o RG do professor: ')
    dataNascimento = input('Digite a data de nascimento do professor: ')
    salario = input('Digite o salário do professor: ')
    formacao = input('Digite a formação do professor: ')
    vinculo = input('Digite o tipo de vínculo do professor: ')

    professor = Professor(nome, cpf, rg, dataNascimento, salario, formacao, vinculo)
    ProfessorDAO().salvar(professor)
    escola.addLista(professor)

    print('Professor Registrado com Sucesso.')


def registrarNovoFuncionario():
    
    nome = input('Digite o nome do funcionário: ')
    cpf = input('Digite o CPF do funcionário: ')
    rg = input('Digite o RG do funcionário: ')
    dataNascimento = input('Digite a data de nascimento do funcionário: ')
    salario = input('Digite o salário do funcionário: ')
    cargo = input('Digite o cargo do funcionário: ')
    horario = input('Digite o horário de trabalho do funcionário: ')

    funcionario = Funcionario(nome, cpf, rg, dataNascimento, salario, cargo, horario)
    FuncionarioDAO().salvar(funcionario)
    escola.addLista(funcionario)

    print('Funcionário Registrado com Sucesso.')


class ComandoNaoExiste(Exception):
    pass


if __name__ == '__main__':

    rodando = True
    while rodando:

        cabecalio()
        resposta = int(input('Digite o comando: '))

        try:
            if resposta == 1:
                registarNovoAluno()

            elif resposta == 2:
                registrarNovoProfessor()

            elif resposta == 3:
                registrarNovoFuncionario()

            elif resposta == 4:
                AlunoDAO().listar()
                ProfessorDAO().listar()
                FuncionarioDAO().listar()

            elif resposta == 5:
                codigo = input('Digite o código de acesso: ')
                escola.solicitaAcesso(codigo)

            elif resposta == 6:
                AlunoDAO().listar()

            elif resposta == 7:
                ProfessorDAO().listar()

            elif resposta == 8:
                FuncionarioDAO().listar()

            elif resposta == 9:
                quit()

            else:
                raise ComandoNaoExiste

        except ComandoNaoExiste:
            raise ComandoNaoExiste('Comando digitado não existe')
