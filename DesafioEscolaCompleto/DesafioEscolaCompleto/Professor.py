from PessoaFisica import PessoaFisica

class Professor(PessoaFisica):
    def __init__(self, nome, cpf, rg, dataNascimento, salario, formacao, tipoDeVinculo):
        super().__init__(nome, cpf, rg, dataNascimento)
        self.__salario = salario
        self.__formacao = formacao
        self.__tipoDeVinculo = tipoDeVinculo

    
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
        if codigo == self.cpf:
            print(f"Boa aula professor(a) {self.nome}!")
            return True
        else:
            return False


    def lecionarAula(self):
        pass


    def __str__(self) -> str:
        return f"Nome: {self.nome} CPF: {self.cpf} RG: {self.rg} Data de Nascimento: {self.dataNascimento}\
 Salário: {self.salario} Formação: {self.formacao} Tipo de Vínculo: {self.tipoDeVinculo}"

### TESTES ###
    
# teste1 = Professor("Antonio", "123", "123", "123", "123", "123", "123")
# print(teste1)
# teste2 = Professor("Jonas", "124", "123", "123", 123, "123", "123")

# teste1.acessarEscola("123")

# print(teste1)