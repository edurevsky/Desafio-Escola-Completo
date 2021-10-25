class FuncionarioDAO(object):
    def salvar(pessoa):
        with open("DesafioEscolaCompleto/BancoDeDados/funcionarios.txt", encoding="UTF-8", mode="a") as arquivo:
            arquivo.write(pessoa.__str__())
            arquivo.write("\n")
            arquivo.flush()
        arquivo.close()


    def listar():
        pass