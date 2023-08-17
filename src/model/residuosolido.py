class Residuo_Solido:
    def __init__(self, descricao = None, quant = None, organico = None, 
                 reciclavel = None, limpo_e_livre = None, inflamavel = None, 
                 radioativo = None, origem = None):
        self.error = ''
        self.material = descricao
        self.quantidade = quant
        self.organico = organico
        self.reciclavel = reciclavel
        self.limpo_e_livre = limpo_e_livre
        self.inflamavel = inflamavel
        self.radioativo = radioativo
        self.origem = origem

        
    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, material):
        if material != None and len(material) != 0:
            self.__material = material
        else:
            self.error = 'Fornecer o "Material" é obrigatório.'

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        if quantidade == 0:
            self.error = 'Fornecer a "Quantidade(Kg)" é obrigatória.'
        else:
            self.__quantidade = quantidade
    
    @property
    def organico(self):
        return self.__organico

    @organico.setter
    def organico(self, organico):
        if organico == '':
            self.error = 'A pergunta "Orgânica?" é obrigatória.'
        else:
            self.__organico = organico

    @property
    def reciclavel(self):
        return self.__reciclavel

    @reciclavel.setter
    def reciclavel(self, reciclavel):
        if reciclavel == '':
            self.error = 'A pergunta "Reciclável?" é obrigatória.'
        else:
            self.__reciclavel = reciclavel

    @property
    def limpo_e_livre(self):
        return self.__limpo_e_livre

    @limpo_e_livre.setter
    def limpo_e_livre(self, limpo_e_livre):
        if limpo_e_livre == '':
            self.error = 'A pergunta "Está limpo e livre de contaminação?" é obrigatória.'
        else:
            self.__limpo_e_livre = limpo_e_livre

    @property
    def inflamavel(self):
        return self.__inflamavel

    @inflamavel.setter
    def inflamavel(self, inflamavel):
        if inflamavel == '':
            self.error = 'A pergunta " É inflamavel?" é obrigatória.'
        else:
            self.__inflamavel = inflamavel

    @property
    def radioativo(self):
        return self.__radioativo

    @radioativo.setter
    def radioativo(self, radioativo):
        if radioativo == '':
            self.error = 'A pergunta " É radioativo?" é obrigatória.'
        else:
            self.__radioativo = radioativo

    @property
    def origem(self):
        return self.__origem

    @origem.setter
    def origem(self, origem):
        if origem != None and len(origem) != 0:
            self.__origem = origem
        else:
            self.error = 'Fornecer "Qual a origem do material?" é obrigatório.'

    def __str__(self):
        return f" material: {self.material} \
                 | quantidade: {self.quantidade} \
                 | orgânico: {self.organico}"

#residuo = Residuo_Solido('', 10, False)

