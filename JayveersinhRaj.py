'''
Name: Jayveersinh Raj
Group : BS-DS-01
Birthdate: 28.09.2001
day = 28
month = September (09)
year = 2001
use the following to run "python3 JayveersinhRaj.py"
'''

# Imports 
from hashlib import new
import random
import os
import glob
import sys
import math

# QTDesigner imports
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import * 



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




# The class for the first window and its functionalities
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

        # Creation of New game button, and on click calls the option_window function                                 
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

        # On Quit button click call the close function to close the app
        self.button_quit.clicked.connect(self.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    # RetranslateUi function to give names, and labels to our window, and its buttons
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







# Option serving window (2nd Window)
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
        

    # RetranslateUi function to give names, and labels to our window, and its buttons           
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
        
        # Checking the play mode is selected
        if self.radioButton_smart.isChecked():  
            self.play_mode = 1  
            checked_mode = True
           
        if self.radioButton_random.isChecked():  
            self.play_mode = 2  
            checked_mode = True
            
        if self.radioButton_advisor.isChecked():  
            self.play_mode = 3  
            checked_mode = True
            
        
        # Checking the position mode is selected  
        if self.radioButton_user_random.isChecked():  
            self.position = 1  
            checked_position = True
            
        if self.radioButton_user_specified.isChecked():  
            self.position = 2  
            checked_position = True
            
        # If one option from both are selected, Proceed, and close the window by opening 3rd
        if(checked_mode and checked_position):
          # Load the main game window
            self.window = QtWidgets.QWidget()
            self_ui = Ui_Form3()
            self_ui.setupUi(self.window, play_mode = self.play_mode, pos_mode = self.position)
            self.window.show()
            prev_win.close()

        # If one option of from both is not selected, give an alert message telling them to choose           
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

        self.textBrowser_bot_position = QtWidgets.QTextBrowser(Form3)
        self.textBrowser_bot_position.setGeometry(QtCore.QRect(490, 80, 141, 31))
        self.textBrowser_bot_position.setStyleSheet("QTextBrowser {\n"
                                       "    border-radius : 25px;\n"
                                       "}")
        self.textBrowser_bot_position.setObjectName("textBrowser_bot_position")
        
        self.textBrowser_bot_move = QtWidgets.QTextBrowser(Form3)
        self.textBrowser_bot_move.setGeometry(QtCore.QRect(190, 80, 141, 31))
        self.textBrowser_bot_move.setStyleSheet("QTextBrowser {\n"
                                         "    border-radius : 25px;\n"
                                         "}")
        self.textBrowser_bot_move.setObjectName("textBrowser_bot_move")


        # TextBrowser for Bot pos_mode when pos_mode mode == 1
        if(pos_mode == 1):
          self.textB = QtWidgets.QTextBrowser(Form3)
          self.textB .setGeometry(QtCore.QRect(190, 40, 142, 31))
          self.textB .setStyleSheet("QTextBrowser {\n"
                                         "    border-radius : 25px;\n"
                                         "}")
          user_random_position = self.spawn_spolier()
          self.textB.setText(str(user_random_position))

          self.label_bot_spawn = QtWidgets.QLabel(Form3)
          self.label_bot_spawn.setGeometry(QtCore.QRect(350, 40, 179, 21))
          self.label_bot_spawn.setObjectName("Duplicator_Spawn")
          self.textB_bot_pos = QtWidgets.QTextBrowser(Form3)
          self.textB_bot_pos.setGeometry(QtCore.QRect(530, 40, 142, 31))
          self.textB_bot_pos.setStyleSheet("QTextBrowser {\n"
                                         "    border-radius : 25px;\n"
                                         "}")
          init_bot_position = self.spawn_spawn_Duplicator()
          self.textB_bot_pos.setText(str(init_bot_position))

          # Hide the start button if Random mode is selected
          self.button_start.hide()


        # If position mode is user defined then display the Bot spawn in a specific way
        if(pos_mode == 2):
          self.label_bot_spawn = QtWidgets.QLabel(Form3)
          self.label_bot_spawn.setGeometry(QtCore.QRect(470, 40, 179, 21))
          self.label_bot_spawn.setObjectName("Duplicator_Spawn")
          self.textB_bot_pos = QtWidgets.QTextBrowser(Form3)
          self.textB_bot_pos.setGeometry(QtCore.QRect(620, 40, 142, 31))
          self.textB_bot_pos.setStyleSheet("QTextBrowser {\n"
                                         "    border-radius : 25px;\n"
                                         "}")
         
          self.lineEdit_user_pos = QtWidgets.QLineEdit(Form3)
          self.lineEdit_user_pos.setGeometry(QtCore.QRect(190, 40, 142, 25))
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

        # Initally play status is set to Ready
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

        # Keep the clear button hidden until, play logs are visible
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

        # Open logs file only shows up when the game ends, so hidden for now
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
            self.textB_bot_pos.setText(str(bot_spawn))
            self.play(bot_spawn, int(user_random_position), str(self.play_m))




    # RetranslateUi function to give names, and labels to our window, and its buttons
    def retranslateUi(self, Form3):
        _translate = QtCore.QCoreApplication.translate
        Form3.setWindowTitle(_translate("Form3", "Spoiler-Duplicator Game"))
        self.label_pos_user.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:9pt;\">Position:</span></p></body></html>"))
        self.label_bot_spawn.setText(_translate("Form3", "<html><head/><body><p><span style=\" font-size:9pt;\">Duplicator Position :</span></p></body></html>"))
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



  
##########################   Below are the functionalities on Button clicks ##########################




    # Function to exit if quit/bye button is clicked
    def close_app(self):
        sys.exit(0)




    # Check move of the player when 'Make' button is pressed
    def check_move(self, mode, pos_mode):
        alert = QtWidgets.QWidget()

        # Update play status
        self.status_play.setText("Play in progress")

        # Validates the move made by the user (in Random position mode), and checks if its the first move
        if(pos_mode == 1 and self.textB_user_move_result.toPlainText() == ''):
          if(self.lineEdit_user_move.text() != '' and not (self.lineEdit_user_move.text().strip().isdigit())):
             QMessageBox.about(alert, "Not Integer Error", "Please enter positive integer values ")

          elif(self.lineEdit_user_move.text() == ''):

             QMessageBox.about(alert, "No Input", "Please enter positive integer values ")
          
          # If the move is the valid move, calls the function user_move to make the move
          else:
             self.user_move(int(self.textBrowser_bot_position.toPlainText()), int(self.textB.toPlainText()), mode)


        # If the move is not the first move
        elif(pos_mode == 1 and self.textB_user_move_result.toPlainText() != ''):
          if(self.lineEdit_user_move.text() != '' and not (self.lineEdit_user_move.text().strip().isdigit())):
             QMessageBox.about(alert, "Not Integer Error", "Please enter positive integer values ")

          elif(self.lineEdit_user_move.text() == ''):
             QMessageBox.about(alert, "No Input", "Please enter positive integer values ")

          # When the move is a valid move make the move by calling the user_move function   
          else:
             self.user_move(int(self.textBrowser_bot_position.toPlainText()), int(self.textB_user_move_result.toPlainText()), mode)
          

        # Validates the move made by the user (in User-defined position mode), and checks if its the first move
        if(pos_mode == 2 and self.lineEdit_user_pos.text() == ''):
           QMessageBox.about(alert, "No Intial position defined", "Please enter the initial position")

        elif(pos_mode == 2 and self.textB_user_move_result.toPlainText() == ''):
  
          if(self.lineEdit_user_move.text() != '' and not (self.lineEdit_user_move.text().strip().isdigit())):
             QMessageBox.about(alert, "Not Integer Error", "Please enter positive integer values ")

          elif(self.lineEdit_user_move.text() == ''):
             QMessageBox.about(alert, "No Input", "Please enter positive integer values ")

          # When the move is a valid move make the move by calling the user_move function   
          else:
             self.user_move(int(self.textBrowser_bot_position.toPlainText()), int(self.lineEdit_user_pos.text()), mode)

        
        # If the move is not the first move
        elif(pos_mode == 2 and self.lineEdit_user_pos.text() != ''):
          if(self.lineEdit_user_move.text() != '' and not (self.lineEdit_user_move.text().strip().isdigit())):
             QMessageBox.about(alert, "Not Integer Error", "Please enter positive integer values ")

          elif(self.lineEdit_user_move.text() == ''):
             QMessageBox.about(alert, "No Input", "Please enter positive integer values ")

          # When the move is a valid move make the move by calling the user_move function      
          else:
             self.user_move(int(self.textBrowser_bot_position.toPlainText()), int(self.textB_user_move_result.toPlainText()), mode)

          
  

    # On clicking start after the input (User-defined position mode)
    def start_button(self):
      alert = QtWidgets.QWidget()
      
      # Validates the user input position, and changes the graphics
      if(self.lineEdit_user_pos.text().strip().isdigit()):
        if(int(self.lineEdit_user_pos.text()) > 0 and int(self.lineEdit_user_pos.text()) < (day+month+year)+1):
            
            # On valid integer position, then append it to the dictionary
            log["You"].append(int(self.lineEdit_user_pos.text()))

            # Hide the start button, and move the Duplicator spawn label and text browser to left
            self.button_start.hide()
            self.label_bot_spawn.move(350, 40)
            self.textB_bot_pos.move(510, 40)

            # Spawn the bot
            bot_spawn = self.spawn_spawn_Duplicator()
            self.textB_bot_pos.setText(str(bot_spawn))
            
            # Disable the input position from user to disable the alteration
            self.lineEdit_user_pos.setReadOnly(True)

            # Set the Play status to "Play in progress"
            self.status_play.setText("Play in progress")

            # The Duplicator makes it move depending on the mode by calling the play function
            self.play(bot_spawn, self.lineEdit_user_pos.text(), str(self.play_m))
          
        # Alert on wrong range of input  
        else:
           QMessageBox.about(alert, "Input Error", "Please enter a valid position between 1 and 2038")
 
      # Alert if the input is not a positive integer
      else:
          QMessageBox.about(alert, "Not Integer Error", "Please enter positive integer values ")




    # Function to start a New Game      
    def new_game(self, prev_win):
       global log

       # Clear the logs, and make it empty if new game is called from amid
       log.clear()
       log = {'Bot': [],
              'You': [],
              'Bot_moves': [],
              'Your_moves' : []
              }

       # Closing the game window and calling the second window with options to choose mode
       self.window = QtWidgets.QWidget()
       self_ui = Ui_form2()
       self_ui.setupUi(self.window)
       self.window.show()
       prev_win.close()




    # Function to display logs when the button is pressed
    def play_logs(self):
       
       # The formatted display of the logs
       self.textBrowser_display_logs.setText(f"Bot positions: {str(log['Bot'])}\nBot moves:"
                                  f"{str(log['Bot_moves'])}"
                                  f"\n\nYour positions: {str(log['You'])}\nYour moves:"
                                  f"{str(log['Your_moves'])}")

       # Making the Clear button appear when the logs are displayed
       self.Clear.show()

       # Letting the program know that logs are visible now, so to display the clear button
       self.logs = True




    # Function to hide/clear the logs screen
    def clear_logs(self):
       
       # Clearing the logs visible text browser on Clicking clear button
       self.textBrowser_display_logs.setText("")

       # Hiding the button again and wait for the player if he choose to display logs again
       self.Clear.hide()

       # Letting the program know that logs are not visible anymore
       self.logs = False




    '''-------------------------------- File handling functions --------------------------------'''




    # Function to open/print logs file content to the console when open logs button is clicked
    def open_logs_file(self):

      # Checking all files
      list_of_files = glob.glob('./Game_logs/*.txt') # * means all if need specific format then *.txt

      # Getting the latest one
      latest_file = max(list_of_files, key=os.path.getctime)

      # Opening the latest one on the console in reading mode
      f = open(latest_file, "r")
      print(f.read())

      # Closing it once it is read
      f.close()

      # Hiding the open logs button, since we do not need it anymore
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

      # Displays the open logs button in the end of the game when file is ready
      self.open_logs.show()




    '''----------------------------- Game Playing Functionalities -----------------------------'''




    # Function that spawns the spawn_Duplicator (Bot)
    def spawn_spawn_Duplicator(self):
        # Spawning of Duplicator (Bot) at a valid Random position
        init_position = random.randint(0, day+month+year)

        # Appending that position to the logs dictionary
        log["Bot"].append(init_position)

        # Return that position
        return init_position
    

    
    
    # Function that spawns a spawn_Duplicator (user) based on his/her choice. Satisfies 2.
    def spawn_spolier(self):

        # Spawing the player at a valid random position if random position mode is selected
        init_position = random.randint(0, day+month+year)

        # Appending that position to the logs dictionary
        log["You"].append(init_position)

        # Return that position
        return str(init_position)
    
  


    # The function to validate, and make user given move
    def user_move(self, prev_pos_bot, prev_pos_user, mod):
        alert = QtWidgets.QWidget()
        move = self.lineEdit_user_move.text()
        prev_pos_user = int(prev_pos_user)

        # Will validate the move again and send to the play to evaluate and or allow the bot to play
        move = int(move)
        if(int(move) > 0 and int(move) <= (day + month)  and (int(move) + prev_pos_user) <= (day + month + year)):
          
          # Display the new valid position to the textBrowser
          self.textB_user_move_result.setText(str(int(move) + prev_pos_user))

          # Displaying the Position textbrowser with the new position if position mode is random
          if(self.pos == 1):
              self.textB.setText(str(int(move) + prev_pos_user))

          # Displaying the Position textbrowser with the new position if position mode is user defined
          if(self.pos == 2):
              self.lineEdit_user_pos.setText(str(int(move) + prev_pos_user))

          # Append the valid moves to the logs
          log["You"].append(int(move) + prev_pos_user) 
          log["Your_moves"].append(int(move))
        
          # Call to the play function after appending the valid move and position to logs
          self.play(prev_pos_bot = prev_pos_bot, prev_pos_user = (int(move) + prev_pos_user), mod = mod)

        # Else alert the user that making that move is not possible
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

         # Update play status to say that Duplicator won
         self.status_play.setText("Duplicator(Bot) wins")

         # If logs are visible than update them real time
         if(self.logs == True):
           self.textBrowser_display_logs.setText(f"Bot positions: {str(log['Bot'])}\nBot moves:"
                                                 f"{str(log['Bot_moves'])}"
                                                 f"\n\nYour positions: {str(log['You'])}\nYour moves:"
                                                 f"{str(log['Your_moves'])}")
         
         # Appends the file with a statment saying the result of the game is Duplicator win
         self.log_file("Duplicator(Bot) wins")

         # Alerts the user about the result of the game
         QMessageBox.about(alert, "The Duplicator wins", "The Duplicator (Bot) wins, Better luck next time..!!")

         # Disables the making of move at the end of the game
         self.lineEdit_user_move.setDisabled(True)

         # Hides the make button
         self.button_make_move.hide()
         return

    
      # If the user spawns on the goal (day + month + year) in my case (28 + 9+ 2001) = 2038, they win
      elif(prev_pos_user == (day + month + year)):

        # Update play status to say that Spolier (user) won
        self.status_play.setText("Spolier(You) win")

        # Appends the file with a statment saying the result of the game is Duplicator win
        self.log_file("Spolier(You) win")

        # If logs are visible than update them real time
        if(self.logs == True):
           self.textBrowser_display_logs.setText(f"Bot positions: {str(log['Bot'])}\nBot moves:"
                                                 f"{str(log['Bot_moves'])}"
                                                 f"\n\nYour positions: {str(log['You'])}\nYour moves:"
                                                 f"{str(log['Your_moves'])}")
        
        # Alerts the user about the result of the game
        QMessageBox.about(alert, "The Spoiler", "You (Spoiler) win...!!! Congratulations")

        # Disables the making of move at the end of the game
        self.lineEdit_user_move.setDisabled(True)

        # Hides the make button
        self.button_make_move.hide()
        return
     


      # The smart moves by the spoiler (bot) if player chooses smart as the play mode. Satisfies 3.1
      if(str(mod) == "1"):
    
        # Smart strategy of the bot to always make the maximum profiting move as long as it is valid
        if(prev_pos_bot <= (day + month + year) - (day + month)):
          move = (day + month)
          new_pos = prev_pos_bot + move
          
          # Appending the dictionary with the move and position
          log["Bot"].append(new_pos)
          log["Bot_moves"].append(move)

           # Checking if logs are visible, if they are than update them real time
          if(self.logs == True):
            self.textBrowser_display_logs.setText(f"Bot positions: {str(log['Bot'])}\nBot moves:"
                                                  f"{str(log['Bot_moves'])}"
                                                  f"\n\nYour positions: {str(log['You'])}\nYour moves:"
                                                  f"{str(log['Your_moves'])}")

          # Updating the Duplicator(bot) result position and move text browsers
          self.textBrowser_bot_move.setText(str(move))
          self.textBrowser_bot_position.setText(str(new_pos))

          # Updating the Duplicator pos. textbrowser
          self.textB_bot_pos.setText(str(new_pos))
         
    
        # If goal can be achieved within the (day + month + year), reach the goal
        elif(prev_pos_bot > (day + month + year) - (day + month)):
          move = ((day + month + year) - prev_pos_bot)
          new_pos = prev_pos_bot + move

          # Updating the Duplicator(bot) position and move text browsers
          self.textBrowser_bot_move.setText(str(move))
          self.textBrowser_bot_position.setText(str(new_pos))

          # Updating the Duplicator pos. textbrowser
          self.textB_bot_pos.setText(str(new_pos))

          # Appending the move and position to the dictionary
          log["Bot"].append(new_pos)
          log["Bot_moves"].append(move)

          # Updating the play status to print the result
          self.status_play.setText("Duplicator(Bot) wins")
          
          # Append the result to the log file
          self.log_file("Duplicator(Bot) wins")

          # Alert the user about the game result
          QMessageBox.about(alert, "Duplicator wins", "The Duplicator (Bot) wins, Better luck next time..!!")

          # Disable the move input, and hide the make button
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

          # Updating the Duplicator(bot) position and move text browsers
          self.textBrowser_bot_position.setText(str(new_pos))
          self.textBrowser_bot_move.setText(str(move))

          # Updating the Duplicator pos. textbrowser
          self.textB_bot_pos.setText(str(new_pos))

          # Append the move and position to the logs dictionary
          log["Bot"].append(new_pos)
          log["Bot_moves"].append(move)

          # If logs are visible then update them real time
          if(self.logs == True):
            self.textBrowser_display_logs.setText(f"Bot positions: {str(log['Bot'])}\nBot moves:"
                                                  f"{str(log['Bot_moves'])}"
                                                  f"\n\nYour positions: {str(log['You'])}\nYour moves:"
                                                  f"{str(log['Your_moves'])}")
          
          # Update the play status to show the result of the game
          self.status_play.setText("Duplicator(Bot) wins")

          # Appending the game result to the log file
          self.log_file("Duplicator(Bot) wins")
 
          # Alert the user about the game result
          QMessageBox.about(alert, "Duplicator wins", "The Duplicator (Bot) wins, Better luck next time..!!")

          # Disable the make move input at the end of the game, and hide the make button
          self.lineEdit_user_move.setDisabled(True)
          self.button_make_move.hide()
          return

        # If not the winning move by the bot
        else:

          # Append the logs dictionary with move and position
          log["Bot"].append(new_pos)
          log["Bot_moves"].append(move)

          # If logs are visible then update them real time
          if(self.logs == True):
            self.textBrowser_display_logs.setText(f"Bot positions: {str(log['Bot'])}\nBot moves:"
                                                  f"{str(log['Bot_moves'])}"
                                                  f"\n\nYour positions: {str(log['You'])}\nYour moves:"
                                                  f"{str(log['Your_moves'])}")
                                  
          # Updating the Duplicator(bot) position and move text browsers                                            
          self.textBrowser_bot_move.setText(str(move))
          self.textBrowser_bot_position.setText(str(new_pos))

          # Updating the Duplicator pos. textbrowser
          self.textB_bot_pos.setText(str(new_pos))
          return
    
    
    
      # The smart moves by the spoiler (bot) if player chooses advisor as the play mode. Satisifies 3.3
      if(str(mod) == "3"):
    
        # Smart strategy of the bot to always make the maximum profiting move
        if(prev_pos_bot <= (day + month + year) - (day + month)):
          move = (day + month)
          new_pos = prev_pos_bot + move

          # Append the logs dictionary with move and position
          log["Bot"].append(new_pos)
          log["Bot_moves"].append(move)

          # Updating the Duplicator(bot) position and move text browsers                                            
          self.textBrowser_bot_position.setText(str(new_pos))
          self.textBrowser_bot_move.setText(str(move))

          # Updating the Duplicator pos. textbrowser
          self.textB_bot_pos.setText(str(new_pos))

          # If logs are visible update them real time
          if(self.logs == True):
            self.textBrowser_display_logs.setText(f"Bot positions: {str(log['Bot'])}\nBot moves:"
                                                  f"{str(log['Bot_moves'])}"
                                                  f"\n\nYour positions: {str(log['You'])}\nYour moves:"
                                                  f"{str(log['Your_moves'])}")
          

          
          # The advices of existing winning strategies
          # These i_bot and i_user are using the theorum calculated to see where they could reach using max moves
          i_bot = int(new_pos + (int(round((day + month + year) - new_pos) / (day + month)) * (day + month)))
          i_user = int(round((day + month + year) - prev_pos_user) / (day + month)) * (day + month) + prev_pos_user

          # If user is more than max move ahead, he has a strategy to win
          if(prev_pos_user >= new_pos + (day + month)):
               print("I am here")
               print(prev_pos_user >= new_pos + (day + month))

             # Update the advice textbrowser to show there exists no winning strategy for the user
               self.textAdvice.setText("There exist a winning startegy for you")

          # If a bot cannot reach goal without changing moves from its position, when they are closer than day + month moves
          # There exists winning strategy for the user
          elif(new_pos <= prev_pos_user + (day + month) and (i_user == (day + month + year) or i_bot < (day + month + year))):
                
               print(f"I bot : {i_bot}") 
               print(f"I user: {i_user}")
               # Update the advice textbrowser to show there exists no winning strategy for the user
               self.textAdvice.setText("There exist a winning startegy for you")
          
          # If the above conditions does not meet, user has no winning strategy
          else:

             # Update the advice textbrowser to show there exists winning strategy for the user
             self.textAdvice.setText("Unfortunately, there is no winning strategy for you..!! :{")
    


        # If goal can be achieved within the (day + month + year), reach the goal
        elif(prev_pos_bot > (day + month + year) - (day + month)):
          move = ((day + month + year) - prev_pos_bot)
          new_pos = prev_pos_bot + move

          # Updating the Duplicator(bot) position and move text browsers
          self.textBrowser_bot_move.setText(str(move))
          self.textBrowser_bot_position.setText(str(new_pos))

          # Updating the Duplicator pos. textbrowser
          self.textB_bot_pos.setText(str(new_pos))

          # Appending the logs dictionary with the move and position
          log["Bot"].append(new_pos)
          log["Bot_moves"].append(move)

          # If the logs are visible update them real time
          if(self.logs == True):
            self.textBrowser_display_logs.setText(f"Bot positions: {str(log['Bot'])}\nBot moves:"
                                                  f"{str(log['Bot_moves'])}"
                                                  f"\n\nYour positions: {str(log['You'])}\nYour moves:"
                                                  f"{str(log['Your_moves'])}")

          # Update the play status text broswer to show the result of the game that bot wins
          self.status_play.setText("Duplicator(Bot) wins")

          # Append the logs file with the result of the game
          self.log_file("Duplicator(Bot) wins")

          # Alert the user about the game results
          QMessageBox.about(alert, "Duplicator wins", "The Duplicator (Bot) wins, Better luck next time..!!")

          # Disable the move input field on the end of the game, and hide the make button
          self.lineEdit_user_move.setDisabled(True)
          self.button_make_move.hide()
          return


# The driver code that runs and sets up initial conditions, and starts the play       
if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  Form = QtWidgets.QWidget()
  ui = Ui_Form()
  ui.setupUi(Form)
  Form.show()
  sys.exit(app.exec_())