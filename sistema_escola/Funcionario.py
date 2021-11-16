from PessoaFisica import PessoaFisica
from datetime import datetime


class Funcionario(PessoaFisica):

    def __init__(self, nome, cpf, rg, dataNascimento, salario, cargo, horarioTrabalho):
        super().__init__(nome, cpf, rg, dataNascimento)
        self.__salario = salario
        self.__cargo = cargo
        self.__horarioTrabalho = horarioTrabalho

    
    @property
    def getSalario(self):
        return self.__salario


    @property
    def getCargo(self):
        return self.__cargo

    
    @property
    def getHorario(self):
        return self.__horarioTrabalho


    def acessarEscola(self, codigo) -> bool:
        if self.getCpf == codigo:
            print(f'Bom trabalho {self.getNome}!')
            return True
        return False

    
    def registrarPonto(self):
        horario = datetime.now()
        print(f'Funcionário {self.getNome} bateu o ponto em: {horario}')

    
    def __str__(self) -> str:
        string = f'{self.getNome},{self.getCpf},{self.getRg},{self.getNascimento},{self.getSalario},{self.getCargo},{self.getHorario}\n'
        return string


    def toJson(self) -> dict:
        estrutura = {
            "nome": self.getNome,
            "cpf": self.getCpf,
            "rg": self.getRg,
            "dataNascimento": self.getNascimento,
            "salario": self.getSalario,
            "cargo": self.getCargo,
            "horarioTrabalho": self.getHorario
        }
        return estrutura
