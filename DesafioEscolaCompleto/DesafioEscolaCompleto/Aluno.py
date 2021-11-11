from PessoaFisica import PessoaFisica

class Aluno(PessoaFisica):
    def __init__(self, nome, cpf, rg, dataNascimento, cgm, turma, turno):
        super().__init__(nome, cpf, rg, dataNascimento)
        self.__cgm = cgm
        self.__turma = turma
        self.__turno = turno


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
        if codigo == self.cgm:
            print(f"Boa aula aluno(a) {self.nome}!")
            return True
        else:
            return False


    def assistirAula(self):
        pass


    def __str__(self) -> str:
        return f"{self.nome},{self.cpf},{self.rg},{self.dataNascimento},{self.cgm},{self.turma},{self.turno}"
