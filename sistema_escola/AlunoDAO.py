from __init__ import json, Aluno


class AlunoDAO:

    def salvar(self, aluno: Aluno):
        with open('db/alunos.json', 'r+') as arquivo:
            dados = json.load(arquivo)
            dados.append(aluno.toJson())
            with open('db/alunos.json', 'w') as f:
                json.dump(dados, f, indent=4)


    def listar(self):
        with open('db/alunos.json', 'r') as arquivo:
            dados = json.load(arquivo)
            if len(dados) > 0:
                print('='*19 + ' ALUNOS ' + '='*20)
            for a in dados:
                print('Nome: ' + a['nome'],
                'CPF: '+ a['cpf'], 
                'RG: ' + a['rg'], 
                'Nascimento: ' + a['dataNascimento'], 
                'CGM: ' + a['cgm'], 
                'Turma: ' + a['turma'], 
                'Turno: ' + a['turno'])