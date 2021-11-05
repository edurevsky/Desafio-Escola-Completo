from lib.File import *

arquivo = File("DesafioEscolaCompleto/BancoDeDados/funcionarios.txt")

class FuncionarioDAO(object):
    def salvar(pessoa):
        Appender(arquivo).append(pessoa.__str__(), True)


    def listar():
        Reader(arquivo).ler()