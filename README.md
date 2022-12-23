# Linear-and-Non-Linear-Optimization

First if you want to run this project, You have to install the requierd libraries

run this command 
``` pip3 install -r requierments.txt ```

### Unconstrained Non Linear Optimization
Which is a type of problems where the objective function is non-linear and it doesn't have any constrains 

Taking $f(x1,x2) = (x1 - 2 ) ^ 2 + (x2 - 2) ^ 2$ which is a function in two variables **x1 , x2**.

![image](https://user-images.githubusercontent.com/61708947/209340770-ed16ed43-5f35-4bf3-b3c2-ed265a5dc176.png)

Now we need to solve this problem and find the optimal point. You can get it from the graph, which is (2,, 2). But what if the functions can't be graphed because they have more than two variables or the graph is difficult to inspect?

Luckily, there are a neumrical methods to get an aproximate solution:
1) **Gradient-Descent**.
  - **Parameters**
    - Current Point.
    - Gradient. represents the direction of greatest change
    - Learning Rate defines the adjustment in the weights of our network with respect to the loss gradient descent
    - Threshold to indeicate when the program should be stopped. 
2) **Newton-Raphson**.
  - **Parameters**
    - Current Point
    - Gradient.
    - Hessian Matrix of second order mixed partials of a scalar field
    - Learning Rate.

Now Let's solve the problem
![image](https://user-images.githubusercontent.com/61708947/209344205-5cb6617d-b0d2-43e9-b6fd-995fef00cadc.png)
