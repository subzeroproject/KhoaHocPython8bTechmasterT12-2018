from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class LoginScreen:	
	def __init__(self,):
		super().__init__()	
		self.initUI()

	def initUI(self):
		self.window = QWidget()	
		self.window.resize(300,200)		
		self.window.setWindowTitle('Login Screen')

		self.layout = QVBoxLayout()
		self.layout.setSpacing(10)		

		self.hbox = QHBoxLayout()
		self.hbox.setAlignment(Qt.AlignCenter)		
		self.label_logo = QLabel()		
		self.label_logo.resize(50, 50)
		pixmap = QPixmap('logo.png')
		pixmap = pixmap.scaledToWidth(64)
		self.label_logo.setPixmap(pixmap)
		self.hbox.addWidget(self.label_logo)

		self.txtEmail = QLineEdit()			
		self.txtEmail.setPlaceholderText('Enter email')
		

		self.txtPassword = QLineEdit()
		self.txtPassword.setPlaceholderText('Enter password')
		self.txtPassword.setEchoMode(QLineEdit.Password)

		self.buttonLogin = QPushButton('Login')
		self.buttonLogin.clicked.connect(self.on_login_clicked)
		# self.buttonLogin.setFixedSize(QSize(100, 30))

		self.layout.setAlignment(Qt.AlignCenter)			
		self.layout.addLayout(self.hbox)		
		self.layout.addWidget(self.txtEmail)
		self.layout.addWidget(self.txtPassword)
		self.layout.addWidget(self.buttonLogin)

		self.layout.addStretch(1)
		self.window.setLayout(self.layout)
		self.window.show()
	
	def on_login_clicked(self):
		alert = QMessageBox()
		alert.setText('You clicked Login!')
		alert.exec_()
	
	def to_string(self):
		pass