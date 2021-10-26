from abc import ABCMeta, abstractmethod

class PessoaFisica(ABCMeta):
    def __init__(self, nome, cpf, rg, dataNascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__rg = rg
        self.__dataNascimento = dataNascimento

    
    @property
    def nome(self):
        return self.__nome


    @property
    def cpf(self):
        return self.__cpf


    @property
    def rg(self):
        return self.__rg


    @property
    def dataNascimento(self):
        return self.__dataNascimento


    @abstractmethod
    def acessarEscola(self):
        pass


    def __str__(self) -> str:
        pass

