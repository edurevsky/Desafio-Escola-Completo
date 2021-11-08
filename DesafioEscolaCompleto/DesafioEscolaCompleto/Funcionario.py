from PessoaFisica import PessoaFisica

class Funcionario(PessoaFisica):
    def __init__(self, nome, cpf, rg, dataNascimento, salario, cargo, horarioTrabalho):
        super().__init__(nome, cpf, rg, dataNascimento)
        self.__salario = salario
        self.__cargo = cargo
        self.__horarioTrabalho = horarioTrabalho


    @property
    def salario(self):
        return self.__salario

    
    @property
    def cargo(self):
        return self.__cargo


    @property
    def horarioDeTrabalho(self):
        return self.__horarioTrabalho


    def acessarEscola(self, codigo):

        # Fazer condição com cpf e exibir mensagem
        if codigo == self.cpf:
            print(f"Bom trabalho {self.nome}!")
            return True
        else:
            return False


    def registrarPonto(self):
        pass


    def __str__(self) -> str:
        return f"{self.nome},{self.cpf},{self.rg},{self.dataNascimento},{self.salario},{self.cargo},{self.horarioDeTrabalho}"

### TESTES ###

# teste1 = Funcionario("Joao", "123", "123", "123", 123, "123", "123")
# print(teste1)
# teste2 = Funcionario("Pedro", "124", "124", "124", 124, "124", "124")

# # Vou precisar disso depois
# lista = [teste1, teste2]

# for funcionario in lista:
#     funcionario.acessarEscola("124")

# teste1.acessarEscola("123")
