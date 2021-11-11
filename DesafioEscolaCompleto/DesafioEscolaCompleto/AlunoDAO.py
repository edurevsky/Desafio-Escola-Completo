from lib.File import *
import json


arquivo = File("DesafioEscolaCompleto/BancoDeDados/alunos.csv")


class AlunoDAO(object):
    def salvar(pessoa):
        Appender(arquivo).append(pessoa.__str__(), False)


    def listar():
        Reader(arquivo).ler()

