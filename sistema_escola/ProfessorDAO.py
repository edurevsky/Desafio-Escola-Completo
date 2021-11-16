from __init__ import json, Professor


class ProfessorDAO:

    def salvar(self, professor: Professor):
        with open('db/professores.json', 'r+') as arquivo:
            dados = json.load(arquivo)
            dados.append(professor.toJson())
            with open('db/professores.json', 'w') as f:
                json.dump(dados, f, indent=4)


    def listar(self):
        with open('db/professores.json', 'r') as arquivo:
            dados = json.load(arquivo)
            if len(dados) > 0:
                print('='*17 + ' PROFESSORES ' + '='*17)
            for a in dados:
                print('Nome: ' + a['nome'], 
                'CPF: ' + a['cpf'], 
                'RG: ' + a['rg'], 
                'Nascimento: ' + a['dataNascimento'], 
                'Salário: ' + a['salario'], 
                'Formação: ' + a['formacao'], 
                'Vínculo: ' + a['tipoDeVinculo'])