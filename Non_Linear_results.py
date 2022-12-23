# import the required libraries

from PyQt5.QtWidgets import QApplication, QScrollArea, QVBoxLayout , QLabel ,QMainWindow , QWidget
from PyQt5.QtCore import Qt, QSize
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from PyQt5 import QtCore 

class Result(QMainWindow):

    def __init__(self , learning_rate , threshold , netwon_dict, gradient_dict, parent = None):
        super(Result , self).__init__(parent)

        # get the height and the width of the current screen
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()

        # set the width and the height
        self.setFixedWidth(self.width)
        self.setMinimumHeight(self.height)

        # init variables
        self.learning_rate = learning_rate
        self.threshold = threshold
        self.netwon_dict = netwon_dict
        self.gradient_dict = gradient_dict

        # init the Widget
         # Scroll Area which contains the widgets, set as the centralWidget
        self.scroll = QScrollArea()           
        # Widget that contains the collection of Vertical Box 
        self.widget = QWidget()     
        # creating a Vertical Box layout            
        self.vbox = QVBoxLayout()    


        # Iterate over Each Point
        for point in netwon_dict:

            # get lists
            netwon_list = netwon_dict[point]
            gradient_list = gradient_dict[point]

            # add a new Section
            self.vbox.addWidget(self.addSection(point , netwon_list , gradient_list))


        self.widget.setLayout(self.vbox)
        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)
        
        self.show()





    def addSection(self , point , newton_list , gradient_list):
        
        # creating a Vertical Box layout
        layout = QVBoxLayout()

        #   Container Widget
        widget = QWidget() 
        widget.setLayout(layout)
        widget.setFixedWidth(self.width)
        widget.setFixedHeight(700)


        #   Scroll Area Properties
        # scroll = QScrollArea()
        # scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # scroll.setWidgetResizable(True)
        # scroll.setWidget(widget)


        #   Scroll Area Layer add
        # scroll_layout = QVBoxLayout(self)
        # scroll_layout.addWidget(scroll)
        # self.setLayout(scroll_layout) 


        # Create a text
        label = QLabel("")

        # add text to the label
        label.setText(f' <h3 style="color: black"> Point {point} with learning rate {self.learning_rate} and threshold {self.threshold} </h3> <br> ')

        # add the label to the layput
        layout.addWidget(label)

        # a figure instance to plot on
        figure = plt.figure()

        # 'figure' instance as a parameter to __init__
        canvas = FigureCanvas(figure)

        # it takes the Canvas widget and a parent
        toolbar = NavigationToolbar(canvas, self)

        # adding tool bar to the layout
        layout.addWidget(toolbar)

        # adding canvas to the layout
        layout.addWidget(canvas)

        # center the text in the middle of the screen
        label.setAlignment(QtCore.Qt.AlignCenter)

        # plot the image
        # create an axis
        ax = figure.add_subplot(111)

        # plot data
        ax.plot(newton_list, label = 'Netwon-Raphson')
        ax.plot(gradient_list, label = 'Gradient Descent')

        ax.legend()



        return widget

