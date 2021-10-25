from PessoaFisica import PessoaFisica

class Professor(PessoaFisica):
    def __init__(self, nome, cpf, rg, dataNascimento, salario, formacao, tipoDeVinculo):
        super().__init__(nome, cpf, rg, dataNascimento)
        self.salario = salario
        self.formacao = formacao
        self.tipoDeVinculo = tipoDeVinculo


    def acessarEscola(self, cpf):

        # Fazer condição com cpf e exibir mensagem
        if cpf == self.cpf:
            print(f"Boa aula professor(a) {self.nome}!")
        return super().acessarEscola()


    def lecionarAula(self):
        pass


    def __str__(self) -> str:
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nRG: {self.rg}\nData de Nascimento: {self.dataNascimento}\n\
Salário: {self.salario}\nFormação: {self.formacao}\nTipo de Vínculo: {self.tipoDeVinculo}\n"

### TESTES ###
    
teste1 = Professor("Antonio", "123", "123", "123", 123, "123", "123")
teste2 = Professor("Jonas", "124", "123", "123", 123, "123", "123")

teste1.acessarEscola("123")

print(teste1)