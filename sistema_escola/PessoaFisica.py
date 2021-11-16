from abc import ABCMeta, abstractmethod


class PessoaFisica(metaclass=ABCMeta):

    def __init__(self, nome, cpf, rg, dataNascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__rg = rg
        self.__dataNascimento = dataNascimento


    @property
    def getNome(self):
        return self.__nome


    @property
    def getCpf(self):
        return self.__cpf


    @property
    def getRg(self):
        return self.__rg


    @property
    def getNascimento(self):
        return self.__dataNascimento


    @abstractmethod
    def acessarEscola(self) -> bool:
        pass


    @abstractmethod
    def __str__(self) -> str:
        pass


    @abstractmethod
    def toJson(self) -> dict:
        pass
