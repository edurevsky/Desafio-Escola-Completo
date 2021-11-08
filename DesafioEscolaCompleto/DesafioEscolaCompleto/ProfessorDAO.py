from lib.File import *

arquivo = File("DesafioEscolaCompleto/BancoDeDados/professores.csv")

class ProfessorDAO(object):
    def salvar(pessoa):
        Appender(arquivo).append(pessoa.__str__(), True)


    def listar():
        Reader(arquivo).ler()