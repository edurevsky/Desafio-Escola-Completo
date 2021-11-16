from __init__ import *


class Escola:

    def __init__(self):
        self.__nome = '--- Escola Estadual Programadores do Futuro ---'
        self.__lista = []
        self.carregarTodos()


    @property
    def getEscNome(self):
        return self.__nome


    @property
    def getLista(self):
        return self.__lista


    def addLista(self, pessoa):
        self.__lista.append(pessoa)


    def solicitaAcesso(self, codigo):
        achou = 0
        for p in self.__lista:
            if p.acessarEscola(codigo):
                achou = 1
        if achou != 1:
            print('Acesso negado!')




    def __getitem__(self, index):
        return self.__lista[index]


    def __len__(self):
        return len(self.__lista)


    def carregarTodos(self):
        self.carregarAlunos()
        self.carregarFuncionarios()
        self.carregarProfessores()


    def carregarAlunos(self):
        with open('db/alunos.json', 'r') as arquivo:
            dados = json.load(arquivo)
            for aluno in dados:
                a = Aluno(**aluno)
                self.__lista.append(a)


    def carregarProfessores(self):
        with open('db/professores.json', 'r') as arquivo:
            dados = json.load(arquivo)
            for professor in dados:
                p = Professor(**professor)
                self.__lista.append(p)


    def carregarFuncionarios(self):
        with open('db/funcionarios.json', 'r') as arquivo:
            dados = json.load(arquivo)
            for funcionario in dados:
                f = Funcionario(**funcionario)
                self.__lista.append(f)
