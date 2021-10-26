class AlunoDAO(object):
    def salvar(pessoa):
        with open("DesafioEscolaCompleto/BancoDeDados/alunos.txt", encoding="UTF-8", mode="a") as arquivo:
            arquivo.write(pessoa.__str__())
            arquivo.write("\n")
            arquivo.flush()
        arquivo.close()


    def listar():
        with open("DesafioEscolaCompleto/BancoDeDados/alunos.txt", encoding="UTF-8", mode="r") as arquivo:
            dados = arquivo.read()
            print(dados)
        arquivo.close()