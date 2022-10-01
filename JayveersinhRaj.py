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
import os
import glob

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
       self.setWindowTitle("Spolier-spawn_spolierlicator Game")
       self.setGeometry(500, 100, 1000, 800) # Geometry
       # Label
       self.label_pos_user = QLabel(self)
       self.label.setText("Welcome to the Spoiler-spawn_spolierlicator FPG")
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
        self.button_new_game = QtWidgets.QPushButton(Form, clicked = lambda : self.option_window())
        self.button_new_game.setGeometry(QtCore.QRect(290, 290, 170, 51))
        self.button_new_game.setObjectName("button_new_game")
        self.button_new_game.setStyleSheet("QPushButton {\n"
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
        self.button_new_game.clicked.connect(Form.close)

        self.button_quit = QtWidgets.QPushButton(Form)
        self.button_quit.setGeometry(QtCore.QRect(290, 370, 170, 51))
        self.button_quit.setStyleSheet("QPushButton {\n"
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
                                        
        self.button_quit.setObjectName("button_quit")
        self.button_quit.clicked.connect(self.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Spoiler-Duplicator Game"))
        self.label.setText(_translate("Spoiler-Duplicator Game", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700; font-style:italic; color:#5F9EA0;\">Welcome to the Game</span></p></body></html>"))
        self.button_new_game.setText(_translate("Form", "New Game"))
        self.button_quit.setText(_translate("Form", "Bye (Quit)"))

 
    
    # Function open options serving page/window 
    def option_window(self):
       self.window = QtWidgets.QWidget()
       self_ui = Ui_form2()
       self_ui.setupUi(self.window)
       self.window.show()



    # Function to close the app if quit/bye button is clicked
    def close(self):
        sys.exit(0)



# Option serving window/page (2nd Window)
class Ui_form2(object):
    # The modes, initially 0, then gets a value when user selects the values
    play_mode = 0
    position = 0 

    def setupUi(self, form2):
        form2.setObjectName("form2")
        form2.resize(761, 674)
        self.verticalLayoutWidget = QtWidgets.QWidget(form2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(290, 160, 131, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.radioButton_smart = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_smart.setObjectName("radioButton_smart")
        self.verticalLayout.addWidget(self.radioButton_smart)

        self.radioButton_random = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_random.setObjectName("radioButton_Random")
        self.verticalLayout.addWidget(self.radioButton_random)

        self.radioButton_advisor = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_advisor.setObjectName("radioButton_Advisor")
        self.verticalLayout.addWidget(self.radioButton_advisor)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(form2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(290, 380, 142, 151))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.radioButton_user_random = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_user_random.setObjectName("radioButton_user_random")
        self.verticalLayout_2.addWidget(self.radioButton_user_random)

        self.radioButton_user_specified = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_user_specified.setObjectName("radioButton_user_specified")
        self.verticalLayout_2.addWidget(self.radioButton_user_specified)

        self.label_position_mode = QtWidgets.QLabel(form2)
        self.label_position_mode.setGeometry(QtCore.QRect(290, 320, 280, 91))
        self.label_position_mode.setObjectName("label_position_mode")

        self.label_play_mode = QtWidgets.QLabel(form2)
        self.label_play_mode.setGeometry(QtCore.QRect(290, 110, 150, 62))
        self.label_play_mode.setObjectName("label")


        # Proceed Button to call start_game function to call the 3rd (main) game page/window
        self.proceed = QtWidgets.QPushButton(form2, clicked = lambda : self.start_game(prev_win = form2))

        self.proceed.setGeometry(QtCore.QRect(290, 590, 170, 51))
        self.proceed.setObjectName("button_make_move")
        self.proceed.setStyleSheet("QPushButton {\n"
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
        self.radioButton_smart.setText(_translate("form2", "Smart"))
        self.radioButton_random.setText(_translate("form2", "Random"))
        self.radioButton_advisor.setText(_translate("form2", "Advisor"))
        self.radioButton_user_random.setText(_translate("form2", "Random"))
        self.radioButton_user_specified.setText(_translate("form2", "User-Specified"))
        self.label_position_mode.setText(_translate("Spoiler-Duplicator Game", "<html><head/><body><p><span style=\" font-size:10pt; color:#4682B4;\">Select Initial Position Mode</span></p></body></html>"))
        self.label_play_mode.setText(_translate("Spoiler-Duplicator Game", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#4682B4;\">Select Play Mode</span></p></body></html>"))
        self.proceed.setText(_translate("form2", "Proceed"))
       



    # The function that accepts and sends the selected options to the main game window
    # It also makes sure that options for the both position and bot is selected
    def start_game(self, prev_win):
        checked_mode = False
        checked_position = False
        form2 = QtWidgets.QWidget()
        if self.radioButton_smart.isChecked():  
            self.play_mode = 1  
            checked_mode = True
           
  
        if self.radioButton_random.isChecked():  
            self.play_mode = 2  
            checked_mode = True
            
  
        if self.radioButton_advisor.isChecked():  
            self.play_mode = 3  
            checked_mode = True
            
          
        if self.radioButton_user_random.isChecked():  
            self.position = 1  
            checked_position = True
            
  
        if self.radioButton_user_specified.isChecked():  
            self.position = 2  
            checked_position = True
            
        
        if(checked_mode and checked_position):
          # Load the main game window
            self.window = QtWidgets.QWidget()
            self_ui = Ui_Form3()
            self_ui.setupUi(self.window, play_mode = self.play_mode, pos_mode = self.position)
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
    def setupUi(self, Form3, play_mode, pos_mode):
        self.play_m  = play_mode
        self.pos = pos_mode
        Form3.setObjectName("Form3")
        Form3.resize(765, 652)

        
        self.label_pos_user = QtWidgets.QLabel(Form3)
        self.label_pos_user.setGeometry(QtCore.QRect(30, 40, 130, 21))
        self.label_pos_user.setObjectName("label_pos_user")

        self.button_start = QtWidgets.QPushButton(Form3, clicked = lambda: self.start_button())
        self.button_start.setGeometry(QtCore.QRect(360, 40, 89, 25))
        self.button_start.setObjectName("button_start")
        self.button_start.setStyleSheet("QPushButton {\n"
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

        self.label_duplicator_move = QtWidgets.QLabel(Form3)
        self.label_duplicator_move.setGeometry(QtCore.QRect(30, 85, 191, 21))
        self.label_duplicator_move.setObjectName("label_duplicator_move")

        self.label_duplicator_result = QtWidgets.QLabel(Form3)
        self.label_duplicator_result.setGeometry(QtCore.QRect(340, 80, 181, 21))
        self.label_duplicator_result.setObjectName("label_duplicator_result")

        self.label_user_move = QtWidgets.QLabel(Form3)
        self.label_user_move.setGeometry(QtCore.QRect(30, 140, 131, 21))
        self.label_user_move.setObjectName("label_user_move")

        self.textBrowser_bot_spawn = QtWidgets.QTextBrowser(Form3)
        self.textBrowser_bot_spawn.setGeometry(QtCore.QRect(490, 80, 141, 31))
        self.textBrowser_bot_spawn.setStyleSheet("QTextBrowser {\n"
                                       "    border-radius : 25px;\n"
                                       "}")
        self.textBrowser_bot_spawn.setObjectName("textBrowser_bot_spawn")
        
        self.textBrowser_user_pos = QtWidgets.QTextBrowser(Form3)
        self.textBrowser_user_pos.setGeometry(QtCore.QRect(190, 80, 141, 31))
        self.textBrowser_user_pos.setStyleSheet("QTextBrowser {\n"
                                         "    border-radius : 25px;\n"
                                         "}")
        self.textBrowser_user_pos.setObjectName("textBrowser_user_pos")

        # TextBrowser for Bot pos_mode when pos_mode mode == 1
        if(pos_mode == 1):
          self.textB = QtWidgets.QTextBrowser(Form3)
          self.textB .setGeometry(QtCore.QRect(190, 40, 142, 31))
          self.textB .setStyleSheet("QTextBrowser {\n"
                                         "    border-radius : 25px;\n"
                                         "}")
          user_random_position = self.spawn_spolier(option = self.pos)
          self.textB.setText(str(user_random_position))

          self.label_bot_spawn = QtWidgets.QLabel(Form3)
          self.label_bot_spawn.setGeometry(QtCore.QRect(350, 40, 179, 21))
          self.label_bot_spawn.setObjectName("Duplicator_Spawn")
          self.textB_spawn = QtWidgets.QTextBrowser(Form3)
          self.textB_spawn.setGeometry(QtCore.QRect(530, 40, 142, 31))
          self.textB_spawn.setStyleSheet("QTextBrowser {\n"
                                         "    border-radius : 25px;\n"
                                         "}")
          init_bot_position = self.spawn_spawn_spolierlicator()
          self.textB_spawn.setText(str(init_bot_position))

          
          self.button_start.hide()

        # If position mode is user defined then display the Bot spawn in a specific way
        if(pos_mode == 2):
          self.label_bot_spawn = QtWidgets.QLabel(Form3)
          self.label_bot_spawn.setGeometry(QtCore.QRect(470, 40, 179, 21))
          self.label_bot_spawn.setObjectName("Duplicator_Spawn")
          self.textB_spawn = QtWidgets.QTextBrowser(Form3)
          self.textB_spawn.setGeometry(QtCore.QRect(620, 40, 142, 31))
          self.textB_spawn.setStyleSheet("QTextBrowser {\n"
                                         "    border-radius : 25px;\n"
                                         "}")
         
          self.lineEdit_user_pos = QtWidgets.QLineEdit(Form3)
          self.lineEdit_user_pos.setGeometry(QtCore.QRect(190, 40, 142, 25))
          # Move to be changed on conditions
          self.lineEdit_user_pos.setPlaceholderText("Enter your position")
          self.lineEdit_user_pos.setObjectName("lineEdit_user_pos")

        
        
        self.lineEdit_user_move = QtWidgets.QLineEdit(Form3)
        self.lineEdit_user_move.setGeometry(QtCore.QRect(190, 140, 142, 25))
        self.lineEdit_user_move.setPlaceholderText("Enter your move")
        self.lineEdit_user_move.setObjectName("lineEdit_user_move")

        self.button_make_move = QtWidgets.QPushButton(Form3, clicked = lambda : self.check_move(self.play_m, self.pos))
        self.button_make_move.setGeometry(QtCore.QRect(360, 140, 89, 25))
        self.button_make_move.setObjectName("button_make_move")
        self.button_make_move.setStyleSheet("QPushButton {\n"
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
        self.textB_user_move_result = QtWidgets.QTextBrowser(Form3)
        self.textB_user_move_result.setGeometry(QtCore.QRect(590, 140, 141, 31))
        self.textB_user_move_result.setStyleSheet("QTextBrowser {\n"
"    border-radius : 25px;\n"
"}")
        self.textB_user_move_result.setObjectName("textB_user_move_result")
        
        self.label_user_result = QtWidgets.QLabel(Form3)
        self.label_user_result.setGeometry(QtCore.QRect(460, 140, 131, 21))
        self.label_user_result.setObjectName("label_user_result")
        
        self.label_play_status = QtWidgets.QLabel(Form3)
        self.label_play_status.setGeometry(QtCore.QRect(30, 200, 131, 21))
        self.label_play_status.setObjectName("play_status")
        self.status_play = QtWidgets.QTextBrowser(Form3)
        self.status_play.setGeometry(QtCore.QRect(190, 190, 160, 31))
        self.status_play.setStyleSheet("QTextBrowser {\n"
                                         "    border-radius : 25px;\n"
                                        "}")
        self.status_play.setObjectName("status_play")

        self.status_play.setText("Ready")

        self.button_player_logs = QtWidgets.QPushButton(Form3, clicked = lambda : self.play_logs())
        self.button_player_logs.setGeometry(QtCore.QRect(30, 270, 89, 25))
        self.button_player_logs.setObjectName("button_player_logs")
        self.button_player_logs.setStyleSheet("QPushButton {\n"
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
        self.textBrowser_display_logs = QtWidgets.QTextBrowser(Form3)
        self.textBrowser_display_logs.setGeometry(QtCore.QRect(30, 310, 701, 251))
        self.textBrowser_display_logs.setObjectName("textBrowser_display_logs")

        self.button_quit = QtWidgets.QPushButton(Form3, clicked = lambda : self.close_app())
        self.button_quit.setGeometry(QtCore.QRect(150, 590, 89, 25))
        self.button_quit.setObjectName("button_quit")
        self.button_quit.setStyleSheet("QPushButton {\n"
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

        self.button_new_game = QtWidgets.QPushButton(Form3, clicked = lambda : self.new_game(Form3))
        self.button_new_game.setGeometry(QtCore.QRect(30, 590, 89, 25))
        self.button_new_game.setObjectName("button_new_game")
        self.button_new_game.setStyleSheet("QPushButton {\n"
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
        self.Clear.setObjectName("button_player_logs")
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

        self.open_logs = QtWidgets.QPushButton(Form3, clicked = lambda: self.open_logs_file())
        self.open_logs.setGeometry(QtCore.QRect(230, 270, 139, 25))
        self.open_logs.setObjectName("open_logs_file")
        self.open_logs.setStyleSheet("QPushButton {\n"
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

        # It only shows up when the game ends
        self.open_logs.hide()

        # Existance of the the advise field when avisor mode is selected
        if (int(play_mode) == 3) :
          self.label_advisor = QtWidgets.QLabel(Form3)
          self.label_advisor.setGeometry(QtCore.QRect(380, 190, 131, 21))
          self.label_advisor.setObjectName("label_7")
          
          self.textAdvice = QtWidgets.QTextBrowser(Form3)
          self.textAdvice.setGeometry(QtCore.QRect(450, 190, 335, 41))
          self.textAdvice.setStyleSheet("QTextBrowser {\n"
                                           "    border-radius : 25px;\n"
                                           "}")
      
        self.retranslateUi(Form3)
        QtCore.QMetaObject.connectSlotsByName(Form3)
        
        # If Random is the position mode then calls play function for the bot to play its turn when window opens
        if(pos_mode == 1):
            bot_spawn = init_bot_position
            self.textB_spawn.setText(str(bot_spawn))
            self.play(bot_spawn, int(user_random_position), str(self.play_m))

    def retranslateUi(self, Form3):
        _translate = QtCore.QCoreApplication.translate
        Form3.setWindowTitle(_translate("Form3", "Spoiler-Duplicator Game"))
        self.label_pos_user.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:9pt;\">You spawn at :</span></p></body></html>"))
        self.label_bot_spawn.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:9pt;\">Duplicator spawn :</span></p></body></html>"))
        self.button_start.setText(_translate("Form3", "Start"))
        self.label_duplicator_move.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:9pt;\">Duplicator move is :</span></p></body></html>"))
        self.label_duplicator_result.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:9pt;\">, it results in :</span></p></body></html>"))
        self.label_user_move.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:9pt;\">Your move is :</span></p></body></html>"))
        self.button_make_move.setText(_translate("Form3", "Make"))
        self.label_user_result.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:9pt;\">, it results in :</span></p></body></html>"))
        self.label_play_status.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:9pt;\">Play Status :</span></p></body></html>"))
        self.button_player_logs.setText(_translate("Form3", "Player Logs"))
        self.button_quit.setText(_translate("Form3", "Bye (Quit)"))
        self.button_new_game.setText(_translate("Form3", "New Game"))
        self.Clear.setText(_translate("Form3", "Clear"))
        self.open_logs.setText(_translate("Form3", "Open logs file"))
        
        # If Advisor is the play mode then Advisor label and text box should appear
        if (int(self.play_m) == 3) :
          self.label_advisor.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:9pt;\"> Advice :</span></p></body></html>"))



  
##########################   Below are the functionalities on Button clicks  ################################




    # Function to exit if quit/bye button is clicked
    def close_app(self):
        sys.exit(0)




    # Check move of the player when 'Make' button is pressed
    def check_move(self, mode, pos_mode):
        alert = QtWidgets.QWidget()

        # Update play status
        self.status_play.setText("Play in progress")

        # Validates the move made by the user (in Random mode), and checks if its the first move
        if(pos_mode == 1 and self.textB_user_move_result.toPlainText() == ''):
          if(self.lineEdit_user_move.text() != '' and not (self.lineEdit_user_move.text().strip().isdigit())):
             QMessageBox.about(alert, "Not Integer Error", "Please enter positive integer values ")

          elif(self.lineEdit_user_move.text() == ''):

             QMessageBox.about(alert, "No Input", "Please enter positive integer values ")
          
          else:
             self.user_move(int(self.textBrowser_bot_spawn.toPlainText()), int(self.textB.toPlainText()), mode)


        elif(pos_mode == 1 and self.textB_user_move_result.toPlainText() != ''):
          if(self.lineEdit_user_move.text() != '' and not (self.lineEdit_user_move.text().strip().isdigit())):
             QMessageBox.about(alert, "Not Integer Error", "Please enter positive integer values ")
          elif(self.lineEdit_user_move.text() == ''):
             QMessageBox.about(alert, "No Input", "Please enter positive integer values ")
          else:
             self.user_move(int(self.textBrowser_bot_spawn.toPlainText()), int(self.textB_user_move_result.toPlainText()), mode)
          

        if(pos_mode == 2 and self.lineEdit_user_pos.text() == ''):
           QMessageBox.about(alert, "Not Intial position defined", "Please enter the initial position")

        elif(pos_mode == 2 and self.textB_user_move_result.toPlainText() == ''):
  
          if(self.lineEdit_user_move.text() != '' and not (self.lineEdit_user_move.text().strip().isdigit())):
             QMessageBox.about(alert, "Not Integer Error", "Please enter positive integer values ")
          elif(self.lineEdit_user_move.text() == ''):
             QMessageBox.about(alert, "No Input", "Please enter positive integer values ")
          else:
             self.user_move(int(self.textBrowser_bot_spawn.toPlainText()), int(self.lineEdit_user_pos.text()), mode)

        
        elif(pos_mode == 2 and self.lineEdit_user_pos.text() != ''):
          if(self.lineEdit_user_move.text() != '' and not (self.lineEdit_user_move.text().strip().isdigit())):
             QMessageBox.about(alert, "Not Integer Error", "Please enter positive integer values ")
          elif(self.lineEdit_user_move.text() == ''):
             QMessageBox.about(alert, "No Input", "Please enter positive integer values ")
          else:
             self.user_move(int(self.textBrowser_bot_spawn.toPlainText()), int(self.textB_user_move_result.toPlainText()), mode)

          
  

    # On clicking start after the input
    def start_button(self):
      alert = QtWidgets.QWidget()
      
      if(self.lineEdit_user_pos.text().strip().isdigit()):
        if(int(self.lineEdit_user_pos.text()) > 0 and int(self.lineEdit_user_pos.text()) < (day+month+year)+1):
            log["You"].append(int(self.lineEdit_user_pos.text()))
            self.button_start.hide()
            self.label_bot_spawn.move(350, 40)
            self.textB_spawn.move(510, 40)

            bot_spawn = self.spawn_spawn_spolierlicator()
            self.textB_spawn.setText(str(bot_spawn))

            self.lineEdit_user_pos.setReadOnly(True)
            self.status_play.setText("Play in progress")
            self.play(bot_spawn, self.lineEdit_user_pos.text(), str(self.play_m))
          
        else:
           QMessageBox.about(alert, "Input Error", "Please enter a valid position between 1 and 2038")

      else:
          QMessageBox.about(alert, "Not Integer Error", "Please enter positive integer values ")




    # Function to start a New Game      
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



    # Function to display logs when the button is pressed
    def play_logs(self):
       self.textBrowser_display_logs.setText(f"Bot positions: {str(log['Bot'])}\nBot moves:"
                                  f"{str(log['Bot_moves'])}"
                                  f"\n\nYour positions: {str(log['You'])}\nYour moves:"
                                  f"{str(log['Your_moves'])}")
       self.Clear.show()
       self.logs = True



    # Function to hide/clear the logs screen
    def clear_logs(self):
       self.textBrowser_display_logs.setText("")
       self.Clear.hide()
       self.logs = False
       



    # Function to open/print logs file content to the console
    def open_logs_file(self):
      list_of_files = glob.glob('./Game_logs/*.txt') # * means all if need specific format then *.csv
      latest_file = max(list_of_files, key=os.path.getctime)
      f = open(latest_file, "r")
      print(f.read())
      f.close()
      self.open_logs.hide()
    
            

    # Function to create logs file inside a folder called Game_logs
    def log_file(self, result):
      # Make a directory if does not exists
      if not os.path.isdir("Game_logs"):
        os.mkdir("Game_logs")
      
      # Starts with 1 and make the file for game 1
      count = 1
      filename = "Logs_Game" + "(" + str(count) + ").txt"
      
      # Check if a logs file exists to name it, so can create files for number of game
      while(os.path.exists('./Game_logs/'+ filename)):
         count = count + 1
         filename = "Logs_Game" + "(" + str(count) + ").txt"

      # When file name with game number found, writes the logs with result inside of it
      filename = "./Game_logs/Logs_Game" + "(" + str(count) + ")"
      f = open(filename + ".txt","w+")
      f.write(f"Bot positions: {str(log['Bot'])}\nBot moves:"
                                f"{str(log['Bot_moves'])}"
                                f"\n\nYour positions: {str(log['You'])}\nYour moves:"
                                f"{str(log['Your_moves'])} \n\n"
                                f"Result of the game: {result}")
      f.close()
      self.open_logs.show()


    '''-------------------------------------- Functionalities ------------------------------------------'''



    # Function that spawns the spawn_spolierlicator (Bot)
    def spawn_spawn_spolierlicator(self):
        init_position = random.randint(0, day+month+year)
        log["Bot"].append(init_position)
        return init_position
    
    
    
    # Function that spawns a spawn_spolierlicator (user) based on his/her choice. Satisfies 2.
    def spawn_spolier(self, option):
        init_position = random.randint(0, day+month+year)
        log["You"].append(init_position)
        return str(init_position)
    
  

    # The function to validate, and make user given move
    def user_move(self, prev_pos_bot, prev_pos_user, mod):
        alert = QtWidgets.QWidget()
        move = self.lineEdit_user_move.text()
        prev_pos_user = int(prev_pos_user)

        # Will validate the move and send to the play to evaluate and or allow the bot to play
        move = int(move)
        if(int(move) > 0 and int(move) <= (day + month)  and (int(move) + prev_pos_user) <= (day + month + year)):
          
          # Display the new valid position to the textBrowser
          self.textB_user_move_result.setText(str(int(move) + prev_pos_user))

          # Append the valid moves to the logs
          log["You"].append(int(move) + prev_pos_user) 
          log["Your_moves"].append(int(move))
        
          # Call to the play function after appending the valid move and position to logs
          self.play(prev_pos_bot = prev_pos_bot, prev_pos_user = (int(move) + prev_pos_user), mod = mod)

        else: 
         QMessageBox.about(alert, "Out of range", "Please enter positive integer value between 1 and 37, should not exceed 2038")
         return
        
              
    
    # Uses Backward induction to make it's play
    # The function that actually Duplicator (Bot) and gives chance to the user to play next
    def play(self, prev_pos_bot, prev_pos_user, mod):
      alert = QtWidgets.QWidget()
      prev_pos_user = int(prev_pos_user)
     
      # If bot spawns on the goal (day + month + year) in my case (28 + 9+ 2001) = 2038, it wins
      if(prev_pos_bot == (day + month + year)):
         self.status_play.setText("Duplicator(Bot) wins")

         self.textBrowser_display_logs.setText(f"Bot positions: {str(log['Bot'])}\nBot moves:"
                                  f"{str(log['Bot_moves'])}"
                                  f"\n\nYour positions: {str(log['You'])}\nYour moves:"
                                  f"{str(log['Your_moves'])}")

         self.log_file("Duplicator(Bot) wins")

         QMessageBox.about(alert, "The Duplicator wins", "The Duplicator (Bot) wins, Better luck next time..!!")
         self.lineEdit_user_move.setDisabled(True)
         self.button_make_move.hide()
         return

    
      # If the user spawns on the goal (day + month + year) in my case (28 + 9+ 2001) = 2038, they win
      elif(prev_pos_user == (day + month + year)):
        self.status_play.setText("Spolier(You) win")
        self.log_file("Spolier(You) win")

        self.textBrowser_display_logs.setText(f"Bot positions: {str(log['Bot'])}\nBot moves:"
                                  f"{str(log['Bot_moves'])}"
                                  f"\n\nYour positions: {str(log['You'])}\nYour moves:"
                                  f"{str(log['Your_moves'])}")

        QMessageBox.about(alert, "The Spoiler", "You (Spoiler) win...!!! Congratulations")
        self.lineEdit_user_move.setDisabled(True)
        self.button_make_move.hide()
        return
     


      # The smart moves by the spoiler (bot) if player chooses smart as the play mode. Satisfies 3.1
      if(str(mod) == "1"):
    
        # Smart strategy of the bot to always make the maximum profiting move
        if(prev_pos_bot <= (day + month + year) - (day + month)):
          move = (day + month)
          new_pos = prev_pos_bot + move
          
          log["Bot"].append(new_pos)
          log["Bot_moves"].append(move)

          if(self.logs == True):
            self.textBrowser_display_logs.setText(f"Bot positions: {str(log['Bot'])}\nBot moves:"
                                  f"{str(log['Bot_moves'])}"
                                  f"\n\nYour positions: {str(log['You'])}\nYour moves:"
                                  f"{str(log['Your_moves'])}")

          self.textBrowser_user_pos.setText(str(move))
          self.textBrowser_bot_spawn.setText(str(new_pos))
         # self.made_move(prev_pos_bot = move, prev_pos_user = prev_pos_user, mod = mod)
    
        # If goal can be achieved within the (day + month + year), reach the goal
        elif(prev_pos_bot > (day + month + year) - (day + month)):
          move = ((day + month + year) - prev_pos_bot)
          new_pos = prev_pos_bot + move
          self.textBrowser_user_pos.setText(str(move))
          self.textBrowser_bot_spawn.setText(str(new_pos))
          log["Bot"].append(new_pos)
          log["Bot_moves"].append(move)
          self.status_play.setText("Duplicator(Bot) wins")
          
          self.log_file("Duplicator(Bot) wins")

          QMessageBox.about(alert, "Duplicator wins", "The Duplicator (Bot) wins, Better luck next time..!!")
          self.lineEdit_user_move.setDisabled(True)
          self.button_make_move.hide()
          return
          
    
    
      # The random moves by the spoiler (bot) if player chooses random as the play mode. Satisifies 3.2
      if(str(mod) == "2"):
        not_correct = True
    
        # Should not exceed 2038
        while(not_correct):
         move = random.randint(1, (day + month))
         new_pos = prev_pos_bot + move
         if(new_pos <= 2038):
          not_correct = False
  
        # If Spoiler(bot) is on 2038, play should terminate
        if(new_pos == 2038):
          self.textBrowser_bot_spawn.setText(str(new_pos))
          self.textBrowser_user_pos.setText(str(move))
          log["Bot"].append(new_pos)
          log["Bot_moves"].append(move)

          if(self.logs == True):
            self.textBrowser_display_logs.setText(f"Bot positions: {str(log['Bot'])}\nBot moves:"
                                  f"{str(log['Bot_moves'])}"
                                  f"\n\nYour positions: {str(log['You'])}\nYour moves:"
                                  f"{str(log['Your_moves'])}")
          
          self.status_play.setText("Duplicator(Bot) wins")

          self.log_file("Duplicator(Bot) wins")

          QMessageBox.about(alert, "Duplicator wins", "The Duplicator (Bot) wins, Better luck next time..!!")
          self.lineEdit_user_move.setDisabled(True)
          self.button_make_move.hide()
          return

        else:
          log["Bot"].append(new_pos)
          log["Bot_moves"].append(move)

          if(self.logs == True):
            self.textBrowser_display_logs.setText(f"Bot positions: {str(log['Bot'])}\nBot moves:"
                                  f"{str(log['Bot_moves'])}"
                                  f"\n\nYour positions: {str(log['You'])}\nYour moves:"
                                  f"{str(log['Your_moves'])}")
                                  
          self.textBrowser_user_pos.setText(str(move))
          self.textBrowser_bot_spawn.setText(str(new_pos))
          return
    
    
      # The smart moves by the spoiler (bot) if player chooses advisor as the play mode. Satisifies 3.3
      if(str(mod) == "3"):
    
        # Smart strategy of the bot to always make the maximum profiting move
        if(prev_pos_bot <= (day + month + year) - (day + month)):
          move = (day + month)
          new_pos = prev_pos_bot + move
          log["Bot"].append(new_pos)
          log["Bot_moves"].append(move)
          self.textBrowser_bot_spawn.setText(str(new_pos))
          self.textBrowser_user_pos.setText(str(move))

          if(self.logs == True):
            self.textBrowser_display_logs.setText(f"Bot positions: {str(log['Bot'])}\nBot moves:"
                                  f"{str(log['Bot_moves'])}"
                                  f"\n\nYour positions: {str(log['You'])}\nYour moves:"
                                  f"{str(log['Your_moves'])}")
          
          
          # The advices of existing winning strategies
          if(prev_pos_user <= new_pos and prev_pos_user <= new_pos + (day + month)):
            self.textAdvice.setText("Unfortunately, there is no winning strategy for you..!! :{")
          
          else:
            self.textAdvice.setText("There exist a winning startegy for you")
         # play(move, u_move, mod)
    
        # If goal can be achieved within the (day + month + year), reach the goal
        elif(prev_pos_bot > (day + month + year) - (day + month)):
          move = ((day + month + year) - prev_pos_bot)
          new_pos = prev_pos_bot + move
          self.textBrowser_user_pos.setText(str(move))
          self.textBrowser_bot_spawn.setText(str(new_pos))
          log["Bot"].append(new_pos)
          log["Bot_moves"].append(move)

          if(self.logs == True):
            self.textBrowser_display_logs.setText(f"Bot positions: {str(log['Bot'])}\nBot moves:"
                                  f"{str(log['Bot_moves'])}"
                                  f"\n\nYour positions: {str(log['You'])}\nYour moves:"
                                  f"{str(log['Your_moves'])}")

          self.status_play.setText("Duplicator(Bot) wins")

          self.log_file("Duplicator(Bot) wins")

          QMessageBox.about(alert, "Duplicator wins", "The Duplicator (Bot) wins, Better luck next time..!!")
          self.lineEdit_user_move.setDisabled(True)
          self.button_make_move.hide()
          return


# e driver code that runs and sets up initial conditions, and starts the play       
if __name__ == "__main__":

 # The main driver
  import sys
  app = QtWidgets.QApplication(sys.argv)
  Form = QtWidgets.QWidget()
  ui = Ui_Form()
  ui.setupUi(Form)
  Form.show()
  sys.exit(app.exec_())