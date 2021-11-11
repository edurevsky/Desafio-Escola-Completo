from Aluno import Aluno
from Funcionario import Funcionario
from Professor import Professor

from AlunoDAO import AlunoDAO
from FuncionarioDAO import FuncionarioDAO
from ProfessorDAO import ProfessorDAO

import csv

# Class "Escola" deve agir como uma lista
class Escola(object):
    
    def __init__(self):
        self.__nome = ("\033[36m--- Escola Estadual Programadores do Futuro ---")
        self.pessoas = []

    def nomeEscola(self):
        return self.__nome

    def adicionarPessoa(self, pessoa):
        self.pessoas.append(pessoa)

    def solicitaAcesso(self, codigoAcesso):
        i = 0
        while i < len(self.pessoas):
            for pessoa in self.pessoas:
                pessoa.acessarEscola(codigoAcesso)
                i += 1

    # Listagem
    def listarAlunos(self):
        AlunoDAO.listar()

    def listarProfessores(self):
        ProfessorDAO.listar()
    
    def listarFuncionarios(self):
        FuncionarioDAO.listar()

    def carregarPessoas(self):
        self.carregarAlu()
        self.carregarFunc()
        self.carregarProf()
        print(self.pessoas)

    def carregarAlu(self):
        # Append alunos na lista
        with open("DesafioEscolaCompleto/BancoDeDados/alunos.csv") as alunos:
            reader = csv.reader(alunos)
            
            for linha in reader:
                nome, cpf, rg, dataNascimento, cgm, turma, turno = linha

                aluno = Aluno(nome, cpf, rg, dataNascimento, cgm, turma, turno)
                self.pessoas.append(aluno)

    def carregarFunc(self):
        # Append funcionarios na lista
        with open("DesafioEscolaCompleto/BancoDeDados/funcionarios.csv") as funcionarios:
            reader = csv.reader(funcionarios)

            for linha in reader:
                nome, cpf, rg, dataNascimento, salario, cargo, horarioTrabalho = linha

                funcionario = Funcionario(nome, cpf, rg, dataNascimento, salario, cargo, horarioTrabalho)
                self.pessoas.append(funcionario)

    def carregarProf(self):
        # Append professores na lista
        with open("DesafioEscolaCompleto/BancoDeDados/professores.csv") as professores:
            reader = csv.reader(professores)

            for linha in reader:
                nome, cpf, rg, dataNascimento, salario, formacao, tipoDeVinculo = linha

                professor = Professor(nome, cpf, rg, dataNascimento, salario, formacao, tipoDeVinculo)
                self.pessoas.append(professor)

    # Métodos da listagem
    def __getitem__(self, pessoa):
        print(self.pessoas[pessoa])
        return self.pessoas[pessoa]
        

    def __len__(self):
        print("A quantidade de pessoas no registro é: " + str(len(self.pessoas)))
        return len(self.pessoas)
