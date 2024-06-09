#Exercício 1
class Cadastro:
    def __init__(self, nome, idade, saldo, statusCadastro):
        self._nome = nome
        self._idade = idade
        self._saldo = saldo
        self._statusCadastro = statusCadastro

# Exemplo de uso
cadastro = Cadastro("João", 20, 100.0, True)
print(cadastro._nome, cadastro._idade, cadastro._saldo, cadastro._statusCadastro)

#Exercício 2
class Cadastro:
    def __init__(self, nome, idade, saldo, statusCadastro):
        self._nome = None
        self._idade = None
        self._saldo = None
        self._statusCadastro = None

        self.set_nome(nome)
        self.set_idade(idade)
        self.set_saldo(saldo)
        self.set_statusCadastro(statusCadastro)

    def set_nome(self, nome):
        if nome is not None and nome != "":
            self._nome = nome
        else:
            print("Erro: Nome não pode ser vazio.")

    def set_idade(self, idade):
        if idade > 18:
            self._idade = idade
        else:
            print("Erro: Idade deve ser maior de 18 anos.")

    def set_saldo(self, saldo):
        if saldo >= 0:
            self._saldo = saldo
        else:
            print("Erro: Saldo não pode ser negativo.")

    def set_statusCadastro(self, statusCadastro):
        if statusCadastro is True:
            self._statusCadastro = statusCadastro
        else:
            print("Erro: statusCadastro deve ser Verdadeiro.")

    def get_nome(self):
        return self._nome

    def get_idade(self):
        return self._idade

    def get_saldo(self):
        return self._saldo

    def get_statusCadastro(self):
        return self._statusCadastro


#Exercício 3
class Cadastro:
    def __init__(self, nome, idade, saldo, statusCadastro):
        self._nome = None
        self._idade = None
        self._saldo = None
        self._statusCadastro = None

        self.set_nome(nome)
        self.set_idade(idade)
        self.set_saldo(saldo)
        self.set_statusCadastro(statusCadastro)

    def set_nome(self, nome):
        if nome is not None and nome != "":
            self._nome = nome
            print("Cadastro de nome feito com sucesso.")
        else:
            print("Erro: Nome não pode ser vazio.")

    def set_idade(self, idade):
        if idade > 18:
            self._idade = idade
            print("Cadastro de idade feito com sucesso.")
        else:
            print("Erro: Idade deve ser maior de 18 anos.")

    def set_saldo(self, saldo):
        if saldo >= 0:
            self._saldo = saldo
            print("Cadastro de saldo feito com sucesso.")
        else:
            print("Erro: Saldo não pode ser negativo.")

    def set_statusCadastro(self, statusCadastro):
        if statusCadastro is True:
            self._statusCadastro = statusCadastro
            print("Cadastro de status feito com sucesso.")
        else:
            print("Erro: statusCadastro deve ser Verdadeiro.")

    def get_nome(self):
        return self._nome

    def get_idade(self):
        return self._idade

    def get_saldo(self):
        return self._saldo

    def get_statusCadastro(self):
        return self._statusCadastro

# Exemplo de uso
cadastro = Cadastro("João", 20, 100.0, True)
cadastro.set_nome("")  # Deverá exibir erro
cadastro.set_idade(17)  # Deverá exibir erro
cadastro.set_saldo(-50)  # Deverá exibir erro
cadastro.set_statusCadastro(False)  # Deverá exibir erro


