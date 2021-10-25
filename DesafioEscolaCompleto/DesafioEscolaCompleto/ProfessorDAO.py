class ProfessorDAO(object):
    def salvar(pessoa):
        with open("DesafioEscolaCompleto/BancoDeDados/professores.txt", encoding="UTF-8", mode="a") as arquivo:
            arquivo.write(pessoa.__str__())
            arquivo.write("\n")
            arquivo.flush()
        arquivo.close()


    def listar():
        pass