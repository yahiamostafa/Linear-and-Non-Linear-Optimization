"""
Author : Yahia Mostafa
Date : 21/12/2022
"""

# import the requied libraries
from sympy import *
import numpy as np
from Non_Linear_results import Result


class Non_Linear_Optimization:

    def __init__(self , number_of_variables , learning_rate , input_fn , threshold , test_points) -> None:

        # declare the variables's vector
        self.variables_vector = []

        # Init variables
        self.number_of_variables = int(number_of_variables)
        self.learning_rate = float(learning_rate)
        self.threshold = float(threshold)
        self.test_points = test_points

        # create user's variables
        for i in range(1 , self.number_of_variables + 1):
            self.variables_vector.append(Symbol(f"x{i}"))

        # Convert the function from string into a real-function
        self.fn = sympify(input_fn, evaluate=False)

        # calculate the gradient
        gradient = [self.fn.diff(x) for x in self.variables_vector]

        # calculate hessian
        hessian = [[self.fn.diff(x).diff(y) for x in self.variables_vector ] for y in self.variables_vector]

        # split the test points
        points_dataset = self.test_points.split(",")

        # create a dict with the point as a key and the convergence list as a value for the two methods 
        newton_dict = {}
        gradient_dict = {}


        # iterate over each point in the points_dataset
        for point in points_dataset:
            
            current_point = list(map(int , point.strip().split(' ')))

            # init the list of convergence for both methods
            self.newton_list = []
            self.gradient_list = []
            
            # Apply both algorithms
            self.gradient_descent(current_point , gradient)
            self.newton_raphson(current_point , gradient , hessian)

            # add the convergence list to the dict
            newton_dict[point] = self.newton_list
            gradient_dict[point] = self.gradient_list

        # Go to the Result Class
        self.result = Result(self.learning_rate , self.threshold , newton_dict , gradient_dict)
        self.result.show()
        self.hide()



    # Gradient Descent Method to get the the optimum points
    def gradient_descent(self , old_point, gradient , learning_rate = 0.01):

        # make a dict to sub variables with their corresponding values from start_vector
        dict = list(zip(self.variables_vector , old_point))

        # get the value of the gradient
        gradient_value = [x.subs(dict) for x in gradient]

        # get the new point 
        new_point = np.array(old_point) - learning_rate * np.array(gradient_value)

        # calculate the distance between the old point and the new point
        dist = np.sum(np.square(old_point - new_point))

        # add the dist to the convergence list
        self.gradient_list.append(dist)

        # if the distance is less than 10 ^ -3 We will stop
        if (dist <= 1e-7):
            return
        
        # else iterare again with the new point
        self.gradient_descent(new_point , gradient)


    # Netwon-Raphson Method to get the the optimum points

    def newton_raphson(self , old_point , gradient , hessian):
        
        # make a dict to sub variables with their corresponding values from start_vector
        dict = list(zip(self.variables_vector , old_point))

        # get the value of the gradient
        gradient_value = [x.subs(dict) for x in gradient]

        # get the values of the Hessian Matrix
        hessian_value = np.matrix([[x.subs(dict) for x in hessian_row ] for hessian_row in hessian]).astype('float64')

        
        # calculte the hessian inverse
        hessian_inverse = np.linalg.inv(hessian_value)

        # get the new point 
        new_point = np.array(old_point) -  np.dot(np.array(hessian_inverse) , np.array(gradient_value))

        # calculate the distance between the old point and the new point
        dist = np.sum(np.square(old_point - new_point))

        # add the dist to the convergence list
        self.newton_list.append(dist)

        # if the distance is less than 10 ^ -3 We will stop
        if (dist <= 1e-7):
            return
        
        # else iterare again with the new point
        self.newton_raphson(new_point , gradient , hessian)




        




