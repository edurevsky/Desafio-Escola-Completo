# Importações
from os import system

from Aluno import Aluno
from AlunoDAO import AlunoDAO

from Professor import Professor
from ProfessorDAO import ProfessorDAO

from Funcionario import Funcionario
from FuncionarioDAO import FuncionarioDAO

from Escola import Escola

from Erros import *

# Inicialização de Objetos

escola = Escola()


# Funções

def registrarAluno():
    system("cls")

    # Informações
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    rg = input("Digite o RG: ")
    dataNascimento = input("Digite a data de nascimento: ")
    cgm = input("Digite o CGM: ")
    turma = input("Digite a turma: ")
    turno = input("Digite o turno: ")

    # Construtor
    aluno = Aluno(nome, cpf, rg, dataNascimento, cgm, turma, turno)
    escola.adicionarPessoa(aluno)
    
    # DAO
    AlunoDAO.salvar(aluno)

    system("cls")
    print("Aluno registrado com sucesso.")


def registrarProfessor():
    system("cls")

    # Informações
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    rg = input("Digite o RG: ")
    dataNascimento = input("Digite a data de nascimento: ")
    salario = input("Informe o salário: ")
    formacao = input("Informe a formação: ")
    tipoDeVinculo = input("Informe o tipo de vínculo: ")

    # Construtor
    professor = Professor(nome, cpf, rg, dataNascimento, salario, formacao, tipoDeVinculo)
    escola.adicionarPessoa(professor)

    # DAO
    ProfessorDAO.salvar(professor)

    system("cls")
    print("Professor registrado com sucesso.")


def registrarFuncionario():
    system("cls")
    
    # Informações
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    rg = input("Digite o RG: ")
    dataNascimento = input("Digite a data de nascimento: ")
    salario = input("Informe o salário: ")
    cargo = input("Digite o cargo: ")
    horarioDeTrabalho = input("Informe o horário de trabalho: ")

    # Construtor
    funcionario = Funcionario(nome, cpf, rg, dataNascimento, salario, cargo, horarioDeTrabalho)
    escola.adicionarPessoa(funcionario)

    # DAO
    FuncionarioDAO.salvar(funcionario)

    system("cls")
    print("Funcionário registrado com sucesso.")


def acsEscola():
    # system("cls")
    cdgAcs = input("Digite o código de acesso: ")
    escola.solicitaAcesso(cdgAcs)

def listarTodos():
    system("cls")
    escola.listarAlunos()
    escola.listarProfessores()
    escola.listarFuncionarios()


# Main

if __name__ == "__main__":

    escola.carregarPessoas()
    while True:
        
        # Interface
        print(escola.nomeEscola())
        print("O que você deseja fazer?")
        print("[1] - Registrar um NOVO ALUNO")
        print("[2] - Registrar um NOVO PROFESSOR")
        print("[3] - Registrar um NOVO FUNCIONÁRIO")
        print("[4] - LISTAR TODOS")
        print("[5] - LISTAR ALUNOS")
        print("[6] - LISTAR PROFESSORES")
        print("[7] - LISTAR FUNCIONÁRIOS")
        print("[8] - ACESSAR ESCOLA")
        print("[9] - SAIR")

        # Condições
        scanner = int(input("Digite o número da sua resposta: "))

        if scanner == 1:
            registrarAluno()

        elif scanner == 2:
            registrarProfessor()

        elif scanner == 3:
            registrarFuncionario()

        elif scanner == 4:
            listarTodos()

        elif scanner == 5:
            escola.listarAlunos()

        elif scanner == 6:
            escola.listarProfessores()

        elif scanner == 7:
            escola.listarFuncionarios()

        elif scanner == 8:
            acsEscola()

        elif scanner == 9:
            exit()

        else:
            raise ComandoNaoExiste("Valor digitado não corresponde a um comando.")
