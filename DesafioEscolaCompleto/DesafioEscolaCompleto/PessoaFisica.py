from abc import ABCMeta, abstractmethod

class PessoaFisica(object):

    __metaclass__ = ABCMeta
    def __init__(self, nome, cpf, rg, dataNascimento):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.dataNascimento = dataNascimento


    @abstractmethod
    def acessarEscola(self):
        pass


    def __str__(self) -> str:
        pass

