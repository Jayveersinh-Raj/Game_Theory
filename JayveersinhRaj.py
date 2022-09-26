'''
Name: Jayveersinh Raj
Group : BS-DS-01
Birthdate: 28/09/2001
day = 28
month = September (09)
year = 2001

use the following to run "python3 JayveersinhRaj.py"
'''

import random
from turtle import position
from typing import no_type_check

# My birth date information
day = 28
month = 9
year = 2001


# Logs dictionary to store the moves. Satisfies 4.
log = {'Bot': [],
       'You': [],
       'Bot_moves': [],
       'Your_moves' : []
       }


import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import * 

#QTDesigner imports
from PyQt5 import QtCore, QtGui, QtWidgets
import time
from functools import partial

# GUI main window using QT5
'''
class Game(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
      # Title
       self.setWindowTitle("Spolier-Duplicator Game")
       self.setGeometry(500, 100, 1000, 800) # Geometry

       # Label
       self.label = QLabel(self)
       self.label.setText("Welcome to the Spoiler-Duplicator FPG")

       # Font and position
       self.label.setAutoFillBackground(True)
       color  = QtGui.QColor(95,158,160)
       alpha  = 100
       values = "{r}, {g}, {b}, {a}".format(r = color.red(),
                                    g = color.green(),
                                    b = color.blue(),
                                    a = alpha
                                    )
       self.label.setStyleSheet("QLabel { background-color: rgba("+values+"); }")
       self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
       self.setCentralWidget(self.label)
       self.label.setFont(QFont('Times', 10))
   
       # Buttons
       # New Button
       self.b_new = QPushButton(self)
       self.b_new.setText("New")
       self.b_new.move(440, 500)
       self.b_new.resize(100, 50)
   
       # Bye Button
       b_bye = QPushButton(win)
       b_bye.setText("New")
       b_bye.move(440, 500)
       b_new.resize(100, 50)
       
def window():
    app = QApplication(sys.argv)
    win = Game()
      
    
    win.show()
    sys.exit(app.exec_())
'''

# QTDesigner

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(761, 717)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 190, 331, 71))
        self.label.setObjectName("label")
        self.label.setStyleSheet("QLabel {\n"
                                 "border-radius: 30px; \n"
                                 "background-color : rgb(255,255,255);\n}")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 290, 170, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "    border-radius: 20px;\n"
                                        "    background-color : rgb(102,205,170);\n"
                                        "    color: rgb(255,255,255)\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color : rgb(50,110,255);\n"
                                        "    color: rgb(255,255,255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color : rgb(100,170,255); \n"
                                        "}")
        self.pushButton_2.clicked.connect(self.new_game)
        self.pushButton_2.clicked.connect(Form.close)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 370, 170, 51))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
                                        "    border-radius: 20px;\n"
                                        "    background-color : rgb(102,205,170);\n"
                                        "    color: rgb(255,255,255)\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color : rgb(50,110,255);\n"
                                        "    color: rgb(255,255,255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color : rgb(100,170,255); \n"
                                        "}")
                                        
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Spoiler-Duplicator Game"))
        self.label.setText(_translate("Spoiler-Duplicator Game", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700; font-style:italic; color:#5F9EA0;\">Welcome to the Game</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "New Game"))
        self.pushButton_3.setText(_translate("Form", "Bye (Quit)"))


    def new_game(self):
       self.window = QtWidgets.QWidget()
       self_ui = Ui_form2()
       self_ui.setupUi(self.window)
       self.window.show()


    def close(self):
        sys.exit(0)


# 2nd Window
class Ui_form2(object):
    play_mode = 0
    position = 0
    close = False
    def setupUi(self, form2):
        form2.setObjectName("form2")
        form2.resize(761, 674)
        self.verticalLayoutWidget = QtWidgets.QWidget(form2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(290, 160, 131, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(form2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(290, 380, 142, 151))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_6 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout_2.addWidget(self.radioButton_6)
        self.radioButton_5 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_2.addWidget(self.radioButton_5)
        self.label_2 = QtWidgets.QLabel(form2)
        self.label_2.setGeometry(QtCore.QRect(290, 320, 280, 91))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(form2)
        self.label.setGeometry(QtCore.QRect(290, 110, 150, 62))
        self.label.setObjectName("label")

        # Submit Button
        self.submit = QtWidgets.QPushButton(form2, clicked = lambda : self.start_game(prev_win = form2))

        self.submit.setGeometry(QtCore.QRect(290, 590, 170, 51))
        self.submit.setObjectName("pushButton_2")
        self.submit.setStyleSheet("QPushButton {\n"
                                    "    border-radius: 20px;\n"
                                    "    background-color : rgb(102,205,170);\n"
                                    "    color: rgb(255,255,255)\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    background-color : rgb(50,110,255);\n"
                                    "    color: rgb(255,255,255);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "    background-color : rgb(100,170,255); \n"
                                    "}")

        self.retranslateUi(form2)
        QtCore.QMetaObject.connectSlotsByName(form2)
        

            

    def retranslateUi(self, form2):
        _translate = QtCore.QCoreApplication.translate
        form2.setWindowTitle(_translate("form2", "Spoiler-Duplicator Game"))
        self.radioButton.setText(_translate("form2", "Smart"))
        self.radioButton_2.setText(_translate("form2", "Random"))
        self.radioButton_3.setText(_translate("form2", "Advisor"))
        self.radioButton_6.setText(_translate("form2", "Random"))
        self.radioButton_5.setText(_translate("form2", "User-Specified"))
        self.label_2.setText(_translate("Spoiler-Duplicator Game", "<html><head/><body><p><span style=\" font-size:10pt; color:#4682B4;\">Select Initial Position Mode</span></p></body></html>"))
        self.label.setText(_translate("Spoiler-Duplicator Game", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#4682B4;\">Select Play Mode</span></p></body></html>"))
        self.submit.setText(_translate("form2", "Proceed"))
       


    def start_game(self, prev_win):
        checked_mode = False
        checked_position = False
        form2 = QtWidgets.QWidget()
        if self.radioButton.isChecked():  
            self.play_mode = 1  
            checked_mode = True
            print(self.play_mode)  
  
        if self.radioButton_2.isChecked():  
            self.play_mode = 2  
            checked_mode = True
            print(self.play_mode)  
  
        if self.radioButton_3.isChecked():  
            self.play_mode = 3  
            checked_mode = True
            print(self.play_mode)  
          
        if self.radioButton_6.isChecked():  
            self.position = 1  
            checked_position = True
            print(self.position)  
  
        if self.radioButton_5.isChecked():  
            self.position = 2  
            checked_position = True
            print(self.position)
        
        if(checked_mode and checked_position):
          # Load the main game window
            self.window = QtWidgets.QWidget()
            self_ui = Ui_Form3()
            self_ui.setupUi(self.window, play_mode = self.play_mode, position = self.position)
            self.window.show()
            prev_win.close()
           
        else:
           QMessageBox.about(form2, "Mode not selected", "Please select a play mode, and position mode")
            
           






'''###############################         The Main Game Window          #################################'''





# 3rd window, the game window
class Ui_Form3(object):
    play_m = 0
    pos = 0
    logs = False
    def setupUi(self, Form3, play_mode, position):
        self.play_m  = play_mode
        self.pos = position
        Form3.setObjectName("Form3")
        Form3.resize(765, 652)

        
        self.label = QtWidgets.QLabel(Form3)
        self.label.setGeometry(QtCore.QRect(30, 40, 81, 21))
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(Form3, clicked = lambda: self.start_button())
        self.pushButton.setGeometry(QtCore.QRect(360, 40, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton {\n"
                                        "    border-radius: 20px;\n"
                                        "    background-color : rgb(102,205,170);\n"
                                        "    color: rgb(255,255,255)\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color : rgb(50,110,255);\n"
                                        "    color: rgb(255,255,255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color : rgb(100,170,255); \n"
                                        "}")
        self.label_2 = QtWidgets.QLabel(Form3)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 151, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form3)
        self.label_3.setGeometry(QtCore.QRect(360, 80, 131, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form3)
        self.label_4.setGeometry(QtCore.QRect(30, 140, 131, 21))
        self.label_4.setObjectName("label_4")
        self.textBrowser = QtWidgets.QTextBrowser(Form3)
        self.textBrowser.setGeometry(QtCore.QRect(490, 80, 141, 31))
        self.textBrowser.setStyleSheet("QTextBrowser {\n"
                                       "    border-radius : 25px;\n"
                                       "}")
        self.textBrowser.setObjectName("textBrowser")
        
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form3)
        self.textBrowser_2.setGeometry(QtCore.QRect(190, 80, 141, 31))
        self.textBrowser_2.setStyleSheet("QTextBrowser {\n"
                                         "    border-radius : 25px;\n"
                                         "}")
        self.textBrowser_2.setObjectName("textBrowser_2")

        # TextBrowser for Bot position
        if(position == 1):
          self.textB = QtWidgets.QTextBrowser(Form3)
          self.textB .setGeometry(QtCore.QRect(190, 40, 142, 31))
          self.textB .setStyleSheet("QTextBrowser {\n"
                                         "    border-radius : 25px;\n"
                                         "}")
          user_random_position = self.spawn_duplicator(option = self.pos)
          self.textB.setText(str(user_random_position))

          self.label_sp_spawn = QtWidgets.QLabel(Form3)
          self.label_sp_spawn.setGeometry(QtCore.QRect(370, 40, 129, 21))
          self.label_sp_spawn.setObjectName("Spolier_Spawn")
          self.textB_spawn = QtWidgets.QTextBrowser(Form3)
          self.textB_spawn.setGeometry(QtCore.QRect(497, 40, 142, 31))
          self.textB_spawn.setStyleSheet("QTextBrowser {\n"
                                         "    border-radius : 25px;\n"
                                         "}")
          init_bot_position = self.spawn_spoiler()
          self.textB_spawn.setText(str(init_bot_position))

          
          self.pushButton.hide()

        if(position == 2):
          self.label_sp_spawn = QtWidgets.QLabel(Form3)
          self.label_sp_spawn.setGeometry(QtCore.QRect(470, 40, 129, 21))
          self.label_sp_spawn.setObjectName("Spolier_Spawn")
          self.textB_spawn = QtWidgets.QTextBrowser(Form3)
          self.textB_spawn.setGeometry(QtCore.QRect(597, 40, 142, 31))
          self.textB_spawn.setStyleSheet("QTextBrowser {\n"
                                         "    border-radius : 25px;\n"
                                         "}")
         
          self.lineEdit_3 = QtWidgets.QLineEdit(Form3)
          self.lineEdit_3.setGeometry(QtCore.QRect(190, 40, 142, 25))
          # Move to be changed on conditions
          self.lineEdit_3.setPlaceholderText("Enter your position")
          self.lineEdit_3.setObjectName("lineEdit_3")

        
        
        self.lineEdit_2 = QtWidgets.QLineEdit(Form3)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 140, 142, 25))
        self.lineEdit_2.setPlaceholderText("Enter your move")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton_2 = QtWidgets.QPushButton(Form3, clicked = lambda : self.check_move(self.play_m, self.pos))
        self.pushButton_2.setGeometry(QtCore.QRect(360, 140, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "    border-radius: 20px;\n"
                                        "    background-color : rgb(102,205,170);\n"
                                        "    color: rgb(255,255,255)\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color : rgb(50,110,255);\n"
                                        "    color: rgb(255,255,255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color : rgb(100,170,255); \n"
                                        "}")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Form3)
        self.textBrowser_3.setGeometry(QtCore.QRect(590, 140, 141, 31))
        self.textBrowser_3.setStyleSheet("QTextBrowser {\n"
"    border-radius : 25px;\n"
"}")
        self.textBrowser_3.setObjectName("textBrowser_3")
        
        self.label_5 = QtWidgets.QLabel(Form3)
        self.label_5.setGeometry(QtCore.QRect(460, 140, 131, 21))
        self.label_5.setObjectName("label_5")
        
        self.label_6 = QtWidgets.QLabel(Form3)
        self.label_6.setGeometry(QtCore.QRect(30, 200, 131, 21))
        self.label_6.setObjectName("label_6")
        self.textBrowser_4 = QtWidgets.QTextBrowser(Form3)
        self.textBrowser_4.setGeometry(QtCore.QRect(190, 190, 141, 31))
        self.textBrowser_4.setStyleSheet("QTextBrowser {\n"
"    border-radius : 25px;\n"
"}")
        self.textBrowser_4.setObjectName("textBrowser_4")

        self.pushButton_5 = QtWidgets.QPushButton(Form3, clicked = lambda : self.play_logs())
        self.pushButton_5.setGeometry(QtCore.QRect(30, 270, 89, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet("QPushButton {\n"
                                        "    border-radius: 20px;\n"
                                        "    background-color : rgb(102,205,170);\n"
                                        "    color: rgb(255,255,255)\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color : rgb(50,110,255);\n"
                                        "    color: rgb(255,255,255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color : rgb(100,170,255); \n"
                                        "}")
        self.textBrowser_5 = QtWidgets.QTextBrowser(Form3)
        self.textBrowser_5.setGeometry(QtCore.QRect(30, 310, 701, 251))
        self.textBrowser_5.setObjectName("textBrowser_5")

        self.pushButton_4 = QtWidgets.QPushButton(Form3, clicked = lambda : self.close_app())
        self.pushButton_4.setGeometry(QtCore.QRect(150, 590, 89, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "    border-radius: 20px;\n"
                                        "    background-color : rgb(102,205,170);\n"
                                        "    color: rgb(255,255,255)\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color : rgb(50,110,255);\n"
                                        "    color: rgb(255,255,255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color : rgb(100,170,255); \n"
                                        "}")

        self.pushButton_3 = QtWidgets.QPushButton(Form3, clicked = lambda : self.new_game(Form3))
        self.pushButton_3.setGeometry(QtCore.QRect(30, 590, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("QPushButton {\n"
                                        "    border-radius: 20px;\n"
                                        "    background-color : rgb(102,205,170);\n"
                                        "    color: rgb(255,255,255)\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color : rgb(50,110,255);\n"
                                        "    color: rgb(255,255,255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color : rgb(100,170,255); \n"
                                        "}")

        self.Clear = QtWidgets.QPushButton(Form3, clicked = lambda : self.clear_logs())
        self.Clear.setGeometry(QtCore.QRect(130, 270, 89, 25))
        self.Clear.setObjectName("pushButton_5")
        self.Clear.setStyleSheet("QPushButton {\n"
                                        "    border-radius: 20px;\n"
                                        "    background-color : rgb(102,205,170);\n"
                                        "    color: rgb(255,255,255)\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color : rgb(50,110,255);\n"
                                        "    color: rgb(255,255,255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color : rgb(100,170,255); \n"
                                        "}")
        self.Clear.hide()

        # Existance of the the advise field when avisor mode is selected
        if (int(play_mode) == 3) :
          self.label_7 = QtWidgets.QLabel(Form3)
          self.label_7.setGeometry(QtCore.QRect(380, 190, 131, 21))
          self.label_7.setObjectName("label_7")
          
          self.textAdvice = QtWidgets.QTextBrowser(Form3)
          self.textAdvice.setGeometry(QtCore.QRect(450, 190, 335, 41))
          self.textAdvice.setStyleSheet("QTextBrowser {\n"
                                           "    border-radius : 25px;\n"
                                           "}")
      
        self.retranslateUi(Form3)
        QtCore.QMetaObject.connectSlotsByName(Form3)
        
        if(position == 1):
            bot_spawn = init_bot_position
            self.textB_spawn.setText(str(bot_spawn))
            print(f"Type for user position: {type(user_random_position)}, Value: {user_random_position}")
            self.play(bot_spawn, int(user_random_position), str(self.play_m))

    def retranslateUi(self, Form3):
        _translate = QtCore.QCoreApplication.translate
        Form3.setWindowTitle(_translate("Form3", "Spoiler-Duplicator Game"))
        self.label.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:9pt;\">Position :</span></p></body></html>"))
        self.label_sp_spawn.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:9pt;\">Spolier Spawn :</span></p></body></html>"))
        self.pushButton.setText(_translate("Form3", "Start"))
        self.label_2.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:9pt;\">Spoiler move is :</span></p></body></html>"))
        self.label_3.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:9pt;\">, it results in :</span></p></body></html>"))
        self.label_4.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:9pt;\">Your move is :</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Form3", "Make"))
        self.label_5.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:9pt;\">, it results in :</span></p></body></html>"))
        self.label_6.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:9pt;\">Play Status :</span></p></body></html>"))
        self.pushButton_5.setText(_translate("Form3", "Player Logs"))
        self.pushButton_4.setText(_translate("Form3", "Bye (Quit)"))
        self.pushButton_3.setText(_translate("Form3", "New Game"))
        self.Clear.setText(_translate("Form3", "Clear"))
        

        if (int(self.play_m) == 3) :
          self.label_7.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:9pt;\"> Advice :</span></p></body></html>"))

  


    def close_app(self):
        sys.exit(0)


    # Check move of the player when 'Make' button is pressed
    def check_move(self, mode, pos):
        alert = QtWidgets.QWidget()
        if(pos == 1 and self.textBrowser_3.toPlainText() == ''):
          print("I am here")
          if(self.lineEdit_2.text() != '' and not (self.lineEdit_2.text().strip().isdigit())):
             QMessageBox.about(alert, "Not Integer Error", "Please enter positive integer values ")
          elif(self.lineEdit_2.text() == ''):
             QMessageBox.about(alert, "No Input", "Please enter positive integer values ")
          else:
             self.user_move(int(self.textBrowser.toPlainText()), int(self.textB.toPlainText()), mode)


        elif(pos == 1 and self.textBrowser_3.toPlainText() != ''):
          if(self.lineEdit_2.text() != '' and not (self.lineEdit_2.text().strip().isdigit())):
             QMessageBox.about(alert, "Not Integer Error", "Please enter positive integer values ")
          elif(self.lineEdit_2.text() == ''):
             QMessageBox.about(alert, "No Input", "Please enter positive integer values ")
          else:
             self.user_move(int(self.textBrowser.toPlainText()), int(self.textBrowser_3.toPlainText()), mode)
          

        if(pos == 2 and self.lineEdit_3.text() == ''):
           QMessageBox.about(alert, "Not Intial position defined", "Please enter the initial position")

        elif(pos == 2 and self.textBrowser_3.toPlainText() == ''):
          print("I am here")
          if(self.lineEdit_2.text() != '' and not (self.lineEdit_2.text().strip().isdigit())):
             QMessageBox.about(alert, "Not Integer Error", "Please enter positive integer values ")
          elif(self.lineEdit_2.text() == ''):
             QMessageBox.about(alert, "No Input", "Please enter positive integer values ")
          else:
             self.user_move(int(self.textBrowser.toPlainText()), int(self.lineEdit_3.text()), mode)

        
        elif(pos == 2 and self.lineEdit_3.text() != ''):
          if(self.lineEdit_2.text() != '' and not (self.lineEdit_2.text().strip().isdigit())):
             QMessageBox.about(alert, "Not Integer Error", "Please enter positive integer values ")
          elif(self.lineEdit_2.text() == ''):
             QMessageBox.about(alert, "No Input", "Please enter positive integer values ")
          else:
             print("I am fucking here")
             self.user_move(int(self.textBrowser.toPlainText()), int(self.textBrowser_3.toPlainText()), mode)

          



  

    # On clicking start after the input
    def start_button(self):
      alert = QtWidgets.QWidget()
      
      if(self.lineEdit_3.text().strip().isdigit()):
        if(int(self.lineEdit_3.text()) > 0 and int(self.lineEdit_3.text()) < (day+month+year)+1):
            log["You"].append(int(self.lineEdit_3.text()))
            self.pushButton.hide()
            self.label_sp_spawn.move(370, 40)
            self.textB_spawn.move(497, 40)

            bot_spawn = self.spawn_spoiler()
            self.textB_spawn.setText(str(bot_spawn))
            print("lineEdit3 type: ", type(self.lineEdit_3.text()))

            self.lineEdit_3.setReadOnly(True)
            self.play(bot_spawn, self.lineEdit_3.text(), str(self.play_m))
          
        else:
           QMessageBox.about(alert, "Input Error", "Please enter a valid position between 1 and 2038")

      else:
          QMessageBox.about(alert, "Not Integer Error", "Please enter positive integer values ")
          
    def new_game(self, prev_win):
       global log
       log.clear()
       log = {'Bot': [],
              'You': [],
              'Bot_moves': [],
              'Your_moves' : []
              }
       self.window = QtWidgets.QWidget()
       self_ui = Ui_form2()
       self_ui.setupUi(self.window)
       self.window.show()
       prev_win.close()


    def play_logs(self):
       self.textBrowser_5.setText(f"Bot positions: {str(log['Bot'])}\nBot moves:"
                                  f"{str(log['Bot_moves'])}"
                                  f"\n\nYour positions: {str(log['You'])}\nYour moves:"
                                  f"{str(log['Your_moves'])}")
       self.Clear.show()
       self.logs = True

    def clear_logs(self):
       self.textBrowser_5.setText("")
       self.Clear.hide()
       self.logs = False
       



    '''-------------------------------------- Functionalities ------------------------------------------'''



    # Function that spawns the spolier (Bot)
    def spawn_spoiler(self):
        init_position = random.randint(0, day+month+year)
        log["Bot"].append(init_position)
        return init_position
    
    
    
    # Function that spawns a Duplicator (user) based on his/her choice. Satisfies 2.
    def spawn_duplicator(self, option):
        init_position = random.randint(0, day+month+year)
        log["You"].append(init_position)
        return str(init_position)
    
  

    # The function to validate, and make user given move
    def user_move(self, init_pos_bot, init_pos_user, mod):
        alert = QtWidgets.QWidget()
        move = self.lineEdit_2.text()
        init_pos_user = int(init_pos_user)
        not_correct = True
        print(f"Move: {move}")


        move = int(move)
        if(int(move) > 0 and int(move) <= (day + month)  and (int(move) + init_pos_user) <= (day + month + year)):
          self.textBrowser_3.setText(str(int(move) + init_pos_user))
          log["You"].append(int(move) + init_pos_user) 
          log["Your_moves"].append(int(move))
          not_correct = False
          print("I am here")
          self.play(init_pos_bot = init_pos_bot, init_pos_user = (int(move) + init_pos_user), mod = mod)

        elif((int(move) + init_pos_user) == (day + month + year)):
           print("You win")
           return
        else: 
         QMessageBox.about(alert, "Out of range", "Please enter positive integer value between 1 and 37, should not exceed 2038")
         return
        
              

            

          
         
        
    
    
    # The function that actually plays spolier (Bot) and gives chance to the user to play next
    def play(self, init_pos_bot, init_pos_user, mod):
      alert = QtWidgets.QWidget()
      init_pos_user = int(init_pos_user)
      print(f"i am in the play function: {type(mod)}")
      # If bot spawns on the goal (day + month + year) in my case (28 + 9+ 2001) = 2038, it wins
      if(init_pos_bot == (day + month + year)):
         QMessageBox.about(alert, "Spoiler wins", "The Spoiler (Bot) wins, Better luck next time..!!")
         self.lineEdit_2.setDisabled(True)
         self.pushButton_2.hide()
         return

    
      # If the user spawns on the goal (day + month + year) in my case (28 + 9+ 2001) = 2038, they win
      elif(init_pos_user == (day + month + year)):
        QMessageBox.about(alert, "You win", "The Duplicator (You) win...!!! Congratulations")
        self.lineEdit_2.setDisabled(True)
        self.pushButton_2.hide()
        return
     
      # The smart moves by the spoiler (bot) if player chooses smart as the play mode. Satisfies 3.1
      if(str(mod) == "1"):
    
        # Smart strategy of the bot to always make the maximum profiting move
        if(init_pos_bot <= (day + month + year) - (day + month)):
          move = (day + month)
          new_pos = init_pos_bot + move
          print(f"Move of bot: {move}")
          log["Bot"].append(new_pos)
          log["Bot_moves"].append(move)

          if(self.logs == True):
            self.textBrowser_5.setText(f"Bot positions: {str(log['Bot'])}\nBot moves:"
                                  f"{str(log['Bot_moves'])}"
                                  f"\n\nYour positions: {str(log['You'])}\nYour moves:"
                                  f"{str(log['Your_moves'])}")

          self.textBrowser_2.setText(str(move))
          self.textBrowser.setText(str(new_pos))
         # self.made_move(init_pos_bot = move, init_pos_user = init_pos_user, mod = mod)
    
        # If goal can be achieved within the (day + month + year), reach the goal
        elif(init_pos_bot > (day + month + year) - (day + month)):
          move = ((day + month + year) - init_pos_bot)
          new_pos = init_pos_bot + move
          self.textBrowser_2.setText(str(move))
          self.textBrowser.setText(str(new_pos))
          log["Bot"].append(new_pos)
          log["Bot_moves"].append(move)
          QMessageBox.about(alert, "Spoiler wins", "The Spoiler (Bot) wins, Better luck next time..!!")
          self.lineEdit_2.setDisabled(True)
          self.pushButton_2.hide()
          return
          
    
    
      # The random moves by the spoiler (bot) if player chooses random as the play mode. Satisifies 3.2
      if(str(mod) == "2"):
        not_correct = True
    
        # Should not exceed 2038
        while(not_correct):
         move = random.randint(1, (day + month))
         new_pos = init_pos_bot + move
         if(new_pos <= 2038):
          not_correct = False
  
        # If Spoiler(bot) is on 2038, play should terminate
        if(new_pos == 2038):
          self.textBrowser.setText(str(new_pos))
          self.textBrowser_2.setText(str(move))
          log["Bot"].append(new_pos)
          log["Bot_moves"].append(move)

          if(self.logs == True):
            self.textBrowser_5.setText(f"Bot positions: {str(log['Bot'])}\nBot moves:"
                                  f"{str(log['Bot_moves'])}"
                                  f"\n\nYour positions: {str(log['You'])}\nYour moves:"
                                  f"{str(log['Your_moves'])}")

          QMessageBox.about(alert, "Spoiler wins", "The Spoiler (Bot) wins, Better luck next time..!!")
          self.lineEdit_2.setDisabled(True)
          self.pushButton_2.hide()
          return

        else:
          log["Bot"].append(new_pos)
          log["Bot_moves"].append(move)

          if(self.logs == True):
            self.textBrowser_5.setText(f"Bot positions: {str(log['Bot'])}\nBot moves:"
                                  f"{str(log['Bot_moves'])}"
                                  f"\n\nYour positions: {str(log['You'])}\nYour moves:"
                                  f"{str(log['Your_moves'])}")
                                  
          self.textBrowser_2.setText(str(move))
          self.textBrowser.setText(str(new_pos))
          return
    
    
      # The smart moves by the spoiler (bot) if player chooses advisor as the play mode. Satisifies 3.3
      if(str(mod) == "3"):
    
        # Smart strategy of the bot to always make the maximum profiting move
        if(init_pos_bot <= (day + month + year) - (day + month)):
          move = (day + month)
          new_pos = init_pos_bot + move
          log["Bot"].append(new_pos)
          log["Bot_moves"].append(move)
          self.textBrowser.setText(str(new_pos))
          self.textBrowser_2.setText(str(move))

          if(self.logs == True):
            self.textBrowser_5.setText(f"Bot positions: {str(log['Bot'])}\nBot moves:"
                                  f"{str(log['Bot_moves'])}"
                                  f"\n\nYour positions: {str(log['You'])}\nYour moves:"
                                  f"{str(log['Your_moves'])}")
          
          
          # The advices of existing winning strategies
          if(init_pos_user <= new_pos and init_pos_user <= new_pos + (day + month)):
            self.textAdvice.setText("Unfortunately, there is no winning strategy for you..!! :{")
          
          else:
            self.textAdvice.setText("There exist a winning startegy for you")
         # play(move, u_move, mod)
    
        # If goal can be achieved within the (day + month + year), reach the goal
        elif(init_pos_bot > (day + month + year) - (day + month)):
          move = ((day + month + year) - init_pos_bot)
          new_pos = init_pos_bot + move
          self.textBrowser_2.setText(str(move))
          self.textBrowser.setText(str(new_pos))
          log["Bot"].append(new_pos)
          log["Bot_moves"].append(move)

          if(self.logs == True):
            self.textBrowser_5.setText(f"Bot positions: {str(log['Bot'])}\nBot moves:"
                                  f"{str(log['Bot_moves'])}"
                                  f"\n\nYour positions: {str(log['You'])}\nYour moves:"
                                  f"{str(log['Your_moves'])}")

          QMessageBox.about(alert, "Spoiler wins", "The Spoiler (Bot) wins, Better luck next time..!!")
          self.lineEdit_2.setDisabled(True)
          self.pushButton_2.hide()
          return


# e driver code that runs and sets up initial conditions, and starts the play       
if __name__ == "__main__":
  '''
  option = choice()
  mod = mode()

  init_pos_user = spawn_duplicator(option)
  init_pos_bot = spawn_spoiler()
  print(f"Bot position: {init_pos_bot}\nYour position :{init_pos_user}")
  print(f"The log : {log}")
  play(init_pos_bot, init_pos_user, mod) '''
   # window()

 # The main driver
  import sys
  app = QtWidgets.QApplication(sys.argv)
  Form = QtWidgets.QWidget()
  ui = Ui_Form()
  ui.setupUi(Form)
  Form.show()
  sys.exit(app.exec_())
 
     
