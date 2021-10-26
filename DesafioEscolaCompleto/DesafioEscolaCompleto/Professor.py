from PessoaFisica import *

class Professor(PessoaFisica):
    def __init__(self, nome, cpf, rg, dataNascimento, salario, formacao, tipoDeVinculo):
        super().__init__(nome, cpf, rg, dataNascimento)
        self.__salario = salario
        self.__formacao = formacao
        self.__tipoDeVinculo = tipoDeVinculo
        self.codigoAcesso = self.cpf


    @property
    def salario(self):
        return self.__salario

    
    @property
    def formacao(self):
        return self.__formacao


    @property
    def tipoDeVinculo(self):
        return self.__tipoDeVinculo


    def acessarEscola(self, codigo):

        # Fazer condição com cpf e exibir mensagem
        if codigo == self.codigoAcesso:
            print(f"Boa aula professor(a) {self.nome}!")
        else:
            return "Acesso negado."
        return super().acessarEscola()


    def lecionarAula(self):
        pass


    def __str__(self) -> str:
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nRG: {self.rg}\nData de Nascimento: {self.dataNascimento}\n\
Salário: {self.salario}\nFormação: {self.formacao}\nTipo de Vínculo: {self.tipoDeVinculo}\n"

### TESTES ###
    
# teste1 = Professor("Antonio", "123", "123", "123", 123, "123", "123")
# teste2 = Professor("Jonas", "124", "123", "123", 123, "123", "123")

# teste1.acessarEscola("123")

# print(teste1)