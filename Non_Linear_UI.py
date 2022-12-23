"""
Author : Yahia Mostafa
Date : 21/12/2022
"""

import sys  
from PyQt5 import QtCore 
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog , QApplication
from Non_Linear_Optimizaton import Non_Linear_Optimization


class Non_Linear(QDialog):
    def __init__(self):
        super().__init__()
        
        # load the UI 
        loadUi('non_linear_interface.ui' , self)

        # Set title to the window
        self.setWindowTitle("Non Linear Optimization")

        # init the UI Elements
        self.initGUI()


    def initGUI(self):


        # Align text to the center
        self.NumberTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.functionTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.pointsTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.lrTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.thresholdTxt.setAlignment(QtCore.Qt.AlignCenter)

        # set onclick listener to the calculate button
        self.calculateBtn.clicked.connect(self.start_non_linear)


    def start_non_linear(self):

        # get Number of variables learing rate , Function and test points
        number_of_variables = self.NumberTxt.text()
        function = self.functionTxt.text()
        test_points = self.pointsTxt.text()
        learning_rate = self.lrTxt.text()
        threshold = self.thresholdTxt.text()


        # start 
        Non_Linear_Optimization(number_of_variables = number_of_variables , learning_rate = learning_rate , input_fn = function , threshold = threshold , test_points = test_points )


app = QApplication(sys.argv)
screen = Non_Linear()
screen.show()
sys.exit(app.exec_())