from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QRadioButton, QWidget, QPushButton, QButtonGroup

class RadioButtonExample(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(layout)
        self.setCentralWidget(self.central_widget)

        self.button_group = QButtonGroup()

        self.radio_button_sim = QRadioButton("Sim")
        self.radio_button_nao = QRadioButton("Não")

        layout.addWidget(self.radio_button_sim)
        layout.addWidget(self.radio_button_nao)

        self.button_group.addButton(self.radio_button_sim)
        self.button_group.addButton(self.radio_button_nao)

        self.clear_button = QPushButton("Limpar seleção")
        self.clear_button.clicked.connect(self.clear_radio_buttons)
        layout.addWidget(self.clear_button)

    def clear_radio_buttons(self):
        self.button_group.setExclusive(False)
        for button in self.button_group.buttons():
            button.setChecked(False)
        self.button_group.setExclusive(True)

app = QApplication([])
window = RadioButtonExample()
window.show()
app.exec()
