# Definição da classe Pessoa
class Pessoa:
    # Método inicializador que cria uma nova instância da classe Pessoa
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo para armazenar o nome da pessoa
        self.idade = idade  # Atributo para armazenar a idade da pessoa

    # Método de classe que cria uma instância de Pessoa a partir de uma data de nascimento
    @classmethod
    def criar_apartir_data(cls, ano, mes, dia, nome):
        """
        Calcula a idade com base no ano de nascimento e cria uma nova instância de Pessoa.
        :param cls: Referência à classe Pessoa.
        :param ano: Ano de nascimento da pessoa.
        :param mes: Mês de nascimento da pessoa (não utilizado no cálculo de idade aqui).
        :param dia: Dia de nascimento da pessoa (não utilizado no cálculo de idade aqui).
        :param nome: Nome da pessoa.
        :return: Uma nova instância da classe Pessoa.
        """
        idade = 2024 - ano  # Estima a idade com base no ano de nascimento
        return cls(nome, idade)  # Retorna uma nova instância da classe Pessoa

    # Método estático para verificar se uma idade indica maioridade
    @staticmethod
    def verificacao_maiorIdade(idade):
        """
        Verifica se a idade é maior ou igual a 18 anos.
        :param idade: Idade a ser verificada.
        :return: True se a idade for maior ou igual a 18, False caso contrário.
        """
        return idade >= 18

# Exemplo de uso do método de classe para criar uma instância de Pessoa
p = Pessoa.criar_apartir_data(1998, 5, 15, "Jonas")  # Cria a pessoa Jonas com base no ano de nascimento
print(p.nome, p.idade)  # Exibe o nome e a idade de Jonas

# Exemplo de uso do método estático para verificar maioridade
print(Pessoa.verificacao_maiorIdade(18))  # Verifica se 18 é considerado maioridade (True)
print(Pessoa.verificacao_maiorIdade(8))  # Verifica se 8 é considerado maioridade (False)
