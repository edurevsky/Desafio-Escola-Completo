from PessoaFisica import PessoaFisica


class Professor(PessoaFisica):

    def __init__(self, nome, cpf, rg, dataNascimento, salario, formacao, tipoDeVinculo):
        super().__init__(nome, cpf, rg, dataNascimento)
        self.__salario = salario
        self.__formacao = formacao
        self.__tipoDeVinculo = tipoDeVinculo

    
    @property
    def getSalario(self):
        return self.__salario

    
    @property
    def getFormacao(self):
        return self.__formacao


    @property
    def getVinculo(self):
        return self.__tipoDeVinculo


    def acessarEscola(self, codigo) -> bool:
        if self.getCpf == codigo:
            print(f'Boa aula professor(a) {self.getNome}!')
            return True
        return False

    
    def lecionarAula(self) -> None:
        print(f'Professor(a) {self.getNome} está lecionando.')

    
    def __str__(self) -> str:
        string = f'{self.getNome},{self.getCpf},{self.getRg},{self.getNascimento},{self.getSalario},{self.getFormacao},{self.getVinculo}\n'
        return string


    def toJson(self) -> dict:
        estrutura = {
            "nome": self.getNome,
            "cpf": self.getCpf,
            "rg": self.getRg,
            "dataNascimento": self.getNascimento,
            "salario": self.getSalario,
            "formacao": self.getFormacao,
            "tipoDeVinculo": self.getVinculo
        }
        return estrutura
