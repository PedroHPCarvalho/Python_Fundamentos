# Importa o módulo ABC (Abstract Base Classes) e o decorador @abstractmethod
from abc import ABC, abstractmethod

# Definição de uma classe abstrata chamada ControleRemoto
class ControleRemoto(ABC):
    """
    Classe abstrata que define a interface para controles remotos.
    Fornece métodos que precisam ser implementados pelas subclasses.
    """

    # Método abstrato que deve ser implementado pelas subclasses para ligar o dispositivo
    @abstractmethod
    def ligar(self):
        """
        Método abstrato para ligar o dispositivo.
        Deve ser implementado em qualquer classe que herde de ControleRemoto.
        """
        pass

    # Método abstrato que deve ser implementado pelas subclasses para desligar o dispositivo
    @abstractmethod
    def desligar(self):
        """
        Método abstrato para desligar o dispositivo.
        Deve ser implementado em qualquer classe que herde de ControleRemoto.
        """
        pass

# Subclasse de ControleRemoto que implementa os métodos abstratos para uma TV
class ControleTV(ControleRemoto):
    """
    Controle remoto específico para uma TV.
    Implementa os métodos para ligar e desligar a TV.
    """

    # Implementação do método ligar para a TV
    def ligar(self):
        return print("Ligar TV...")  # Mensagem simulando o ato de ligar a TV

    # Implementação do método desligar para a TV
    def desligar(self):
        return print("Desligar TV...")  # Mensagem simulando o ato de desligar a TV

# Subclasse de ControleRemoto que implementa os métodos abstratos para um ar-condicionado
class ControleArCondicionado(ControleRemoto):
    """
    Controle remoto específico para um ar-condicionado.
    Implementa os métodos para ligar e desligar o ar-condicionado.
    """

    # Implementação do método ligar para o ar-condicionado
    def ligar(self):
        return print("Ligar ArCondicionado...")  # Mensagem simulando o ato de ligar o ar-condicionado

    # Implementação do método desligar para o ar-condicionado
    def desligar(self):
        return print("Desligar ArCondicionado...")  # Mensagem simulando o ato de desligar o ar-condicionado

# Exemplo de uso da classe ControleTV
cTV = ControleTV()  # Criação de uma instância de ControleTV
cTV.ligar()  # Chama o método ligar da TV
cTV.desligar()  # Chama o método desligar da TV
print()  # Linha em branco para separar as saídas

# Exemplo de uso da classe ControleArCondicionado
cARCD = ControleArCondicionado()  # Criação de uma instância de ControleArCondicionado
cARCD.ligar()  # Chama o método ligar do ar-condicionado
cARCD.desligar()  # Chama o método desligar do ar-condicionado
