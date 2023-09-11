
class Cadastro:
    def __init__(self, usuario= None , senha = None) -> None:
        self.error = ''
        self.usuario = usuario
        self.senha = senha

    @property
    def usuario(self):
        return self.__usuario
    
    @usuario.setter
    def usuario(self, usuario):
        if usuario != None and len(usuario) != 0:
            self.__usuario = usuario
        else:
            self.error = 'Fornecer o usuário é obrigatório.'

    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        if senha ==0:
            self.error = 'Fornecer a senha é obrigatório.'
        else:
            self.__senha = senha

    def __str__(self) -> str:
        return f'Usuário: {self.usuario} Senha: {self.senha}'

var_cad = Cadastro('Usuario', 10)
print(var_cad)