class Pessoa:
    def __init__(self,nome,ano_nascimento,documento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento
        self.__documento = documento

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, value):
        self.__documento = value

pessoa_conta = Pessoa("Pedro", 2003, "99312245")
print(pessoa_conta.documento)
pessoa_conta.documento = 234
print(pessoa_conta.documento)
