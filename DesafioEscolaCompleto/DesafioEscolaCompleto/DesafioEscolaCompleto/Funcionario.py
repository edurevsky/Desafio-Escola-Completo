from PessoaFisica import *

class Funcionario(PessoaFisica):
    def __init__(self, nome, cpf, rg, dataNascimento, salario, cargo, horarioTrabalho):
        super().__init__(nome, cpf, rg, dataNascimento)
        self.salario = salario
        self.cargo = cargo
        self.horarioTrabalho = horarioTrabalho
        self.codigoAcesso = self.cpf


    def acessarEscola(self, codigo):

        # Fazer condição com cpf e exibir mensagem
        if codigo == self.codigoAcesso:
            print(f"Bom trabalho {self.nome}!")
        else:
            return "Acesso negado."
        return super().acessarEscola()


    def registrarPonto(self):
        pass


    def __str__(self) -> str:
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nRG: {self.rg}\nData de Nascimento: {self.dataNascimento}\n\
Salário: {self.salario}\nCargo: {self.cargo}\nHorário de Trabalho: {self.horarioTrabalho}\n"

### TESTES ###

# teste1 = Funcionario("Joao", "123", "123", "123", 123, "123", "123")
# teste2 = Funcionario("Pedro", "124", "124", "124", 124, "124", "124")

# # Vou precisar disso depois
# lista = [teste1, teste2]

# for funcionario in lista:
#     funcionario.acessarEscola("124")

# teste1.acessarEscola("123")
