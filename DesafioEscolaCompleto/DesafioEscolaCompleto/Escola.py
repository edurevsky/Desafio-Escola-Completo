from Aluno import Aluno
from Funcionario import Funcionario
from Professor import Professor

# Class "Escola" deve agir como uma lista
class Escola(object):
    def __init__(self):
        self.__nome = "Escola Estadual Programadores do Futuro"
        self.__pessoas = []


    def adicionarPessoa(self, pessoa):
        self.__pessoas.append(pessoa)


    def __getitem__(self, pessoa):
        print(self.__pessoas[pessoa])
        return self.__pessoas[pessoa]
        

    def __len__(self):
        print("A quantidade de pessoas no registro é: " + str(len(self.__pessoas)))
        return len(self.__pessoas)


### TESTES ###

Eduardo = Aluno("Eduardo", "12345678901", "12345678901", "01/01/01", "12345678", "3ºA", "Manhã")
Joao = Funcionario("João", "12345678902", "12345678902", "02/02/02", 3000.00, "Zelador", "6:30 às 12:30")
Maria = Professor("Maria", "12345678903", "12345678903", "03/03/03", 3000.00, "Mestrado", None)

escola = Escola()

escola.adicionarPessoa(Eduardo)
escola.adicionarPessoa(Joao)
escola.adicionarPessoa(Maria)

escola.__len__()