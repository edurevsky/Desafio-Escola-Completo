from PessoaFisica import PessoaFisica


class Aluno(PessoaFisica):

    def __init__(self, nome, cpf, rg, dataNascimento, cgm, turma, turno):
        super().__init__(nome, cpf, rg, dataNascimento)
        self.__cgm = cgm
        self.__turma = turma
        self.__turno = turno


    @property
    def getCgm(self):
        return self.__cgm


    @property
    def getTurma(self):
        return self.__turma


    @property
    def getTurno(self):
        return self.__turno


    def acessarEscola(self, codigo) -> bool:
        if self.getCgm == codigo:
            print(f'Boa aula aluno(a) {self.getNome}!')
            return True
        return False


    def assistirAula(self) -> None:
        print(f'{self.getNome} está presente na aula.')


    def __str__(self) -> str:
        string = f'{self.getNome},{self.getCpf},{self.getRg},{self.getNascimento},{self.getCgm},{self.getTurma},{self.getTurno}\n'
        return string


    def toJson(self) -> dict:
        estrutura = {
            "nome": self.getNome,
            "cpf": self.getCpf,
            "rg": self.getRg,
            "dataNascimento": self.getNascimento,
            "cgm": self.getCgm,
            "turma": self.getTurma,
            "turno": self.getTurno
        }
        return estrutura
