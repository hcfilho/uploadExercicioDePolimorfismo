class Pessoa:
    def __init__(self,nome,sobrenome,idade,):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,novo_nome):
        self.__nome = novo_nome

    @property
    def sobrenome(self):
        return self.__sobrenome
    
    @sobrenome.setter
    def sobrenome(self,novo_sobrenome):
        self.__nome = novo_sobrenome

    @property
    def idade(self):
        return self.__idade
    
    @nome.setter
    def idade(self,nova_idade):
        self.__nome = nova_idade

    def retornarIdade(self):
        return self.__idade
        
class Aluno(Pessoa):
    def __init__(self, nome, sobrenome, idade, matricula,curso,mensalidade):
        super().__init__(nome, sobrenome, idade)
        self.__matricula = matricula
        self.__curso = curso
        self.__mensalidade = mensalidade

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, idade,salario,descricao):
        super().__init__(nome, sobrenome, idade)
        self.__salario = salario
        self.__descricao = descricao

    @property
    def salario(self):
        return self.__salario

    def demitir(self):
        print("{}, você está demitido".format(self.nome))
    
    def aumentarSalario(self):
       self.salario *= 0.1

class Materia:
    def __init__(self,nome,duracao):
        self.__nome = nome
        self.__duracao = duracao
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,novo_nome):
        self.__nome = novo_nome

    @property
    def duracao(self):
        return self.__duracao
    
    @duracao.setter
    def duracao(self,nova_duracao):
        self.__duracao = nova_duracao

class Professor(Funcionario):
    def __init__(self, nome, sobrenome, idade, salario, descricao,competencias):
        super().__init__(nome, sobrenome, idade, salario, descricao)
        self.__competencias = competencias
        self.__listaDeMaterias = []
    
    @property
    def materias(self):
        return self.__listaDeMaterias

    def alocarEmMateria(self,materia):
        self.__listaDeMaterias.append(materia)
    

class Coordenador(Funcionario):
    def __init__(self, nome, sobrenome, idade, salario, descricao):
        super().__init__(nome, sobrenome, idade, salario, descricao)

    def aumentarSalario(self):
        self.salario *= 1.20