from PessoaFisica import *

class Aluno(PessoaFisica):
    def __init__(self, nome, cpf, rg, dataNascimento, cgm, turma, turno):
        super().__init__(nome, cpf, rg, dataNascimento)
        self.__cgm = cgm
        self.__turma = turma
        self.__turno = turno
        self.codigoAcesso = self.cgm

    
    @property
    def cgm(self):
        return self.__cgm


    @property
    def turma(self):
        return self.__turma


    @property
    def turno(self):
        return self.__turno
    

    def acessarEscola(self, codigo):

        # Fazer condição com cgm e exibir mensagem
        if codigo == self.codigoAcesso:
            print(f"Boa aula aluno(a) {self.nome}!")
        else:
            return "Acesso negado."
        return super().acessarEscola()


    def assistirAula(self):
        pass


    def __str__(self) -> str:
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nRG: {self.rg}\nData de Nascimento: {self.dataNascimento}\n\
CGM: {self.cgm}\nTurma: {self.turma}\nTurno: {self.turno}\n"

### TESTES ###

# teste1 = Aluno("Lucas", "123", "123", "01/01/01", "001", "123", "123")

# teste2 = Aluno("Luis", "123", "123", "01/01/01", "002", "123", "123")

# lista = [teste1, teste2]

# for aluno in lista:
#     aluno.acessarEscola("002")

# teste1.acessarEscola("123")