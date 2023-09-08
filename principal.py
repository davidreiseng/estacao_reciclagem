import sys

from gui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QTableWidgetItem, QButtonGroup
from PyQt6 import QtWidgets
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from model.residuosolido import Residuo_Solido
from login.login import Login

class Principal(Ui_MainWindow, QMainWindow):

    def __init__(self, parent = None) -> None:
        super().__init__(parent)

        super().setupUi(self)

        self.lista_residuos = [] #banco falso
        self.frame.hide()#frame na tela da tabela

        self.frame_erro_login.hide()
       
        self.frame_msg_erro.hide()#frame na tela de cadastro

        self.line_edit_login.setFocus()#coloca o foco no line edit de login

        self.push_button_entrar.clicked.connect(self.realizar_login)

        self.pushButton_sair.clicked.connect(self.apresentacao)

        self.pushButton_cadastrar.clicked.connect(self.cadastrar)

        self.push_button_salvar.clicked.connect(self.salvar_dados)

        self.pushButton_limpar.clicked.connect(self.limpar_cadastro)

        self.pushButton_limpar.clicked.connect(self.clear_radio_buttons)

        self.pushButton_home.clicked.connect(self.voltar_login)

        self.pushButton_meus_res.clicked.connect(self.meus_residuos)

        self.pushButton_cad_res.clicked.connect(self.cad_res)

        self.pushButton_voltar.clicked.connect(self.voltar_inicio)

        self.set_label_img(self.label, 'img/eco.png')
        self.set_label_img(self.label_img_logo, 'img/eco2.png')

        self.tratar_groups()

    def voltar_login(self):
        self.stacked_widget.setCurrentWidget(self.page_login)
        self.frame_erro_login.hide()

    def tratar_groups(self):
        self.button_group1 = QButtonGroup()
        self.button_group1.addButton(self.radioButton_1sim)
        self.button_group1.addButton(self.radioButton_1nao)

        self.button_group2 = QButtonGroup()
        self.button_group2.addButton(self.radioButton_2sim)
        self.button_group2.addButton(self.radioButton_2nao)

        self.button_group3 = QButtonGroup()
        self.button_group3.addButton(self.radioButton_3sim)
        self.button_group3.addButton(self.radioButton_3nao)

        self.button_group4 = QButtonGroup()
        self.button_group4.addButton(self.radioButton_4sim)
        self.button_group4.addButton(self.radioButton_4nao)

        self.button_group5 = QButtonGroup()
        self.button_group5.addButton(self.radioButton_5sim)
        self.button_group5.addButton(self.radioButton_5nao)
  
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

            self.stacked_widget.setCurrentWidget(self.page_cad_res)

        else:

            self.label_erro_login.setText('Seu login ou senha estão incorretos!')

            self.frame_erro_login.show()
        if login == 'david' and senha == '54321':

            self.line_edit_login.setText('')

            self.line_edit_senha.setText('')

            self.frame_erro_login.hide()

            self.stacked_widget.setCurrentWidget(self.page_cad_res)

        else:

            self.label_erro_login.setText('Seu login ou senha estão incorretos!')

            self.frame_erro_login.show()
        if login == 'jhully' and senha == '56789':

            self.line_edit_login.setText('')

            self.line_edit_senha.setText('')

            self.frame_erro_login.hide()

            self.stacked_widget.setCurrentWidget(self.page_cad_res)

        else:

            self.label_erro_login.setText('Seu login ou senha estão incorretos!')

            self.frame_erro_login.show()

        if login == 'naylana' and senha == '010203':

            self.line_edit_login.setText('')

            self.line_edit_senha.setText('')

            self.frame_erro_login.hide()

            self.stacked_widget.setCurrentWidget(self.page_cad_res)

        else:

            self.label_erro_login.setText('Seu login ou senha estão incorretos!')

            self.frame_erro_login.show()


        if login == 'caioh235' and senha == 'ch1337':

            self.line_edit_login.setText('')

            self.line_edit_senha.setText('')

            self.frame_erro_login.hide()

            self.stacked_widget.setCurrentWidget(self.page_cad_res)

        else:

            self.label_erro_login.setText('Seu login ou senha estão incorretos!')

            self.frame_erro_login.show()

    def cadastrar(self):
        self.stacked_widget.setCurrentWidget(self.page_cadastro)
    
    def cad_res(self):
        self.stacked_widget.setCurrentWidget(self.page_cadastro)

    def meus_residuos(self):
        self.stacked_widget.setCurrentWidget(self.page_apresentacao)

    def voltar_inicio(self):
        self.stacked_widget.setCurrentWidget(self.page_login)
        self.frame_erro_login.hide()

    def limpar_cadastro(self):
        self.line_edit_material.clear()
        self.line_edit_quantidade.clear()
        self.lineEdit_origem.clear()
    
    def clear_radio_buttons (self):
        self.button_group1.setExclusive(False)
        for button in self.button_group1.buttons():
            button.setChecked(False)
        self.button_group1.setExclusive(True)

        self.button_group2.setExclusive(False)
        for button in self.button_group2.buttons():
            button.setChecked(False)
        self.button_group2.setExclusive(True)

        self.button_group3.setExclusive(False)
        for button in self.button_group3.buttons():
            button.setChecked(False)
        self.button_group3.setExclusive(True)

        self.button_group4.setExclusive(False)
        for button in self.button_group4.buttons():
            button.setChecked(False)
        self.button_group4.setExclusive(True)

        self.button_group5.setExclusive(False)
        for button in self.button_group5.buttons():
            button.setChecked(False)
        self.button_group5.setExclusive(True)

    def apresentacao(self):

        self.stacked_widget.setCurrentWidget(self.page_login)
        self.frame_erro_login.hide()
    
    def recalcular_tam_imagem_2(self, end_imagem: str, w: int = 16, h: int = 16):
            print(f'w:{w}, h:{h}')
            logo_2 = QPixmap(end_imagem)
            logo_2 = logo_2.scaled(w, h,
                                Qt.AspectRatioMode.KeepAspectRatio)
            return logo_2

    def salvar_dados(self):
        material = self.line_edit_material.text()
        quantidade = self.line_edit_quantidade.text()
        if self.radioButton_1sim.isChecked():
            organico= True
        elif self.radioButton_1nao.isChecked():
            organico= False
        else :
            organico = ""

        if self.radioButton_2nao.isChecked():
            reciclavel= True
        elif self.radioButton_2sim.isChecked():
            reciclavel= False
        else :
            reciclavel = ""
       
        if self.radioButton_3sim.isChecked():
            limpo_e_livre = True
        elif self.radioButton_3nao.isChecked():
            limpo_e_livre = False
        else :
            limpo_e_livre  = ""    
    
        if self.radioButton_4sim.isChecked():
            inflamavel = True
        elif self.radioButton_4nao.isChecked():
            inflamavel = False
        else :
            inflamavel  = ""

        if self.radioButton_5sim.isChecked():
            radioativo = True
        elif self.radioButton_5nao.isChecked():
            radioativo = False
        else :
            radioativo  = ""

        origem = self.lineEdit_origem.text()
        
        residuo = Residuo_Solido(material, quantidade, organico, reciclavel, limpo_e_livre, inflamavel, radioativo, origem)
        if residuo.error != '':
            self.label_erro.setText(residuo.error)
            self.frame_msg_erro.show()
        else:
            self.lista_residuos.append(residuo)           
            self.label_erro_2.setText('Cadastrado com sucesso!')
            self.frame.show()
            self.line_edit_material.setFocus()
            self.enviar_dados_tabela()
            self.stacked_widget.setCurrentWidget(self.page_apresentacao)


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
            self.limpar_cadastro()
            self.clear_radio_buttons()
            cont_linhas += 1


if __name__ == '__main__':

    qt = QApplication(sys.argv)

    principal = Principal()

    principal.show()

    qt.exec()

