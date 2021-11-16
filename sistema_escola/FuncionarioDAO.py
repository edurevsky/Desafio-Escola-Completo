from __init__ import json, Funcionario


class FuncionarioDAO:

    def salvar(self, funcionario: Funcionario):
        with open('db/funcionarios.json', 'r+') as arquivo:
            dados = json.load(arquivo)
            dados.append(funcionario.toJson())
            with open('db/funcionarios.json', 'w') as f:
                json.dump(dados, f, indent=4)


    def listar(self):
        with open('db/funcionarios.json', 'r') as arquivo:
            dados = json.load(arquivo)
            if len(dados) > 0:
                print('='*17 + ' FUNCIONÁRIOS ' + '='*16)
            for a in dados:
                print('Nome: ' + a['nome'], 
                'CPF: ' + a['cpf'], 
                'RG: ' + a['rg'], 
                'Nascimento: ' + a['dataNascimento'], 
                'Salário: ' + a['salario'], 
                'Cargo: ' + a['cargo'], 
                'Horário de Trabalho: ' + a['horarioTrabalho'])    