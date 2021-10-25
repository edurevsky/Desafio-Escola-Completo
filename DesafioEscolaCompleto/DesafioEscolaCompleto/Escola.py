from Aluno import Aluno
from Funcionario import Funcionario
from Professor import Professor

from AlunoDAO import AlunoDAO
from FuncionarioDAO import FuncionarioDAO
from ProfessorDAO import ProfessorDAO

# Class "Escola" deve agir como uma lista
class Escola(object):
    def __init__(self):
        self.__nome = "Escola Estadual Programadores do Futuro"
        self.__pessoas = []


    def adicionarPessoa(self, pessoa):
        self.__pessoas.append(pessoa)


    def solicitaAcesso(self, codigoAcesso):
        for pessoa in self.__pessoas:
            pessoa.acessarEscola(codigoAcesso)
 
        # Adicionar Mensagem de acesso negado ***

    def __getitem__(self, pessoa):
        print(self.__pessoas[pessoa])
        return self.__pessoas[pessoa]
        

    def __len__(self):
        print("A quantidade de pessoas no registro é: " + str(len(self.__pessoas)))
        return len(self.__pessoas)


### TESTES ###

Eduardo = Aluno("Eduardo", "12345678901", "12345678901", "01/01/01", "12345678", "3ºA", "Manhã")
Pedro = Aluno("Pedro", "12345678900", "12345678900", "00/00/00", "123345670", "", "")
Joao = Funcionario("João", "12345678902", "12345678902", "02/02/02", 3000.00, "Zelador", "6:30 às 12:30")
Maria = Professor("Maria", "12345678903", "12345678903", "03/03/03", 3000.00, "Mestrado", None)

escola = Escola()

escola.adicionarPessoa(Eduardo)
escola.adicionarPessoa(Joao)
escola.adicionarPessoa(Maria)

escola.solicitaAcesso("12345678")

AlunoDAO.salvar(Eduardo)
AlunoDAO.salvar(Pedro)

FuncionarioDAO.salvar(Joao)
ProfessorDAO.salvar(Maria)

escola.__len__()