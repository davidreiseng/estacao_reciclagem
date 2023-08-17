import sys


from gui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QTableWidgetItem
from PyQt6 import QtWidgets
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt

from model.residuosolido import Residuo_Solido

class Principal(Ui_MainWindow, QMainWindow):


    def __init__(self, parent = None) -> None:
        super().__init__(parent)

        super().setupUi(self)

        self.lista_residuos = [] # banco falso
        self.frame.hide()#frame na tela da tabela

        self.frame_erro_login.hide()
       
        self.frame_msg_erro.hide()#frame na tela de cadastro

        self.line_edit_login.setFocus()#coloca o foco no line edit de login

        self.push_button_entrar.clicked.connect(self.realizar_login)

        # self.push_button_salvar.clicked.connect(self.salvar_residuos)

        self.pushButton_sair.clicked.connect(self.apresentacao)

        self.pushButton_cadastrar.clicked.connect(self.cadastrar)

        self.push_button_salvar.clicked.connect(self.salvar_dados)

        #self.set_label_img(self.label_4, 'img/eco.png')
        self.set_label_img(self.label, 'img/eco.png')
        self.set_label_img(self.label_img_logo, 'img/eco2.png')

        
    def set_label_img(self, label: QLabel, end_img: str):
        img = QPixmap(end_img)
        img = img.scaled(label.width(), label.height(), Qt.AspectRatioMode.KeepAspectRatio)
        label.setPixmap(img)
            

        
        

    def realizar_login(self):

        '''Realizar o login do usuário'''

        login = self.line_edit_login.text()#recupera o texto do line edit

        senha = self.line_edit_senha.text()

        if login == 'admin' and senha == '12345':

            self.line_edit_login.setText('')

            self.line_edit_senha.setText('')

            self.frame_erro_login.hide()

            self.stacked_widget.setCurrentWidget(self.page_apresentacao)

        else:

            self.label_erro_login.setText('Seu login ou senha estão incorretos!')

            self.frame_erro_login.show()




    def cadastrar(self):

        #material = self.line_edit_material.text()

        #quantidade = self.line_edit_quantidade.text()

        self.stacked_widget.setCurrentWidget(self.page_cadastro)


    def apresentacao(self):

        self.stacked_widget.setCurrentWidget(self.page_login)

    # def salvar_residuos(self):
    #     if self.line_edit_material.text() == '':
    #         self.frame_msg_erro.show()
    #     else:
    #         #deve salvar os dados do registro sólido
    #         self.stacked_widget.setCurrentWidget(self.page_apresentacao)

    
    def recalcular_tam_imagem_2(self, end_imagem: str, w: int = 16, h: int = 16):
            print(f'w:{w}, h:{h}')
            logo_2 = QPixmap(end_imagem)
            logo_2 = logo.scaled(w, h,
                                Qt.AspectRatioMode.KeepAspectRatio)
            return logo_2

    def salvar_dados(self):
        #hide
        material = self.line_edit_material.text()
        quantidade = self.line_edit_quantidade.text()
        organico = True if self.radioButton_1sim.isChecked() else False
        reciclavel = True if self.radioButton_2sim.isChecked() else False
        limpo_e_livre = True if self.radioButton_3sim.isChecked() else False
        inflamavel = True if self.radioButton_4sim.isChecked() else False
        radioativo = True if self.radioButton_5sim.isChecked() else False
        origem = self.lineEdit_origem.text()
        
        residuo = Residuo_Solido(material, int(quantidade), organico, reciclavel, limpo_e_livre, inflamavel, radioativo, origem)
        if residuo.error != '':
            self.label_erro.setText(residuo.error)
            self.frame_msg_erro.show()
        else:
            self.lista_residuos.append(residuo)           
            # self.frame_msg_erro.show()
            self.label_erro_2.setText('Cadastrado com sucesso!')
            self.frame.show()
            self.line_edit_material.setFocus()
            self.enviar_dados_tabela()
            self.stacked_widget.setCurrentWidget(self.page_apresentacao)

        # if residuo.error != '':
        #    self.label_erro_2.setText(residuo.error)
        #   self.frame.show()

        #else:
        #  self.frame.show()

            

        # print(
        #     f'Material: {material}\n'
        #     f'Quantidade(Kg): {quantidade}\n'
        #     f'Orgânico?: {organico}\n'
        #     f'Reciclável?: {reciclavel}\n'
        #     f'Está limpo e livre de contaminação?: {limpo_e_livre}\n'
        #     f'É inflamável?: {inflamavel}\n'
        #     f'É radioativo?: {radioativo}\n'
        #     f'Qual a origem do material?: {origem}'
        # )

    def enviar_dados_tabela(self):
        cont_linhas = 0
        self.tableWidget.setRowCount(len(self.lista_residuos))
        for ref_obj in self.lista_residuos:
            self.tableWidget.setItem(cont_linhas, 0, QTableWidgetItem(ref_obj.material))
            self.tableWidget.setItem(cont_linhas, 1, QTableWidgetItem(str(ref_obj.quantidade)) )
            self.tableWidget.setItem(cont_linhas, 2, QTableWidgetItem(str('Sim' if ref_obj.organico else 'Não')))
            self.tableWidget.setItem(cont_linhas, 3, QTableWidgetItem(str('Sim' if ref_obj.reciclavel else 'Não')))
            self.tableWidget.setItem(cont_linhas, 4, QTableWidgetItem(str('Sim' if ref_obj.limpo_e_livre else 'Não')))
            self.tableWidget.setItem(cont_linhas, 5, QTableWidgetItem(str('Sim' if ref_obj.inflamavel else 'Não')))
            self.tableWidget.setItem(cont_linhas, 6, QTableWidgetItem(str('Sim' if ref_obj.radioativo else 'Não')))
            self.tableWidget.setItem(cont_linhas, 7, QTableWidgetItem(ref_obj.origem))

            cont_linhas += 1



if __name__ == '__main__':

    qt = QApplication(sys.argv)

    principal = Principal()

    principal.show()

    qt.exec()

