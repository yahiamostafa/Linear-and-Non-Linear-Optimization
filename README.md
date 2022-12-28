# Linear-and-Non-Linear-Optimization

First if you want to run this project, You have to install the requierd libraries

run this command 
``` pip3 install -r requierments.txt ```

### Unconstrained Non Linear Optimization
Which is a type of problems where the objective function is non-linear and it doesn't have any constrains 

Taking $f(x_1,x_2) = (x_1 - 2 ) ^ 2 + (x_2 - 2) ^ 2$ which is a function in two variables **x_1 , x_2**.

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

![image](https://user-images.githubusercontent.com/61708947/209345026-868be38b-8226-49ba-896d-86f26b8bea5a.png)

![image](https://user-images.githubusercontent.com/61708947/209345072-a0c20584-bc17-4c70-b3b0-2d036b88df3a.png)

The benefits of this application are that there is no limit to the number of variables or iterations, but of course you've got to make sure that your requirements are suitable for your hardware.

**N.B The HESSIAN MATRIX CAN'T BE SINGULAR. **

---
What if we added two constraints, making the problem **Non-Linear Contrained**?

$x_1 + x_2 <= 2$

$x_1^2 - x_2 <= 0$ 

![image](https://user-images.githubusercontent.com/61708947/209392209-312b2c6e-9bba-4943-bf98-fa209fde211a.png)


### Hand Analysis Solution

1) **Lagrangian function** ==> $L(x_1,x_2,s_1,s_2,λ_1,λ_2) = (x_1 - 2 ) ^ 2 + (x_2 - 2) ^ 2 + λ_1(x_1 + x_2 - 2 + s_1^2) + λ_2(x_1^2 - x_2 + s_2^2)$

where **s_1 & s_2** are slack variables.

2) **Kuhn-Tucker Conditions**

$▽f + Σ λ_i ▽g_i = 0$

$x_1 + x_2 <= 2$

$x_1^2 - x_2 <= 0$ 

**$λ_1(x_1 + x_2 - 2) = 0$**

**$λ_2(x_1^2 - x_2) = 0$**

$x_1 + x_2 <= 2$

$x_1^2 - x_2 <= 0$ 

$λ_1 >= 0 , λ_2 >= 0$

$▽f = (2x_1 - 4, 2x_2 - 4)$ ==> 1

$▽g_1 = (1,1)$ ==> 2

$▽g_2 = (2x_1,-1)$ ==> 3

so from 1 2 and 3

**$2x_1 - 4 + λ_1 + λ_2 * 2x_1 = 0$**

**$2x_2 - 4 + λ_1 - λ_2 = 0$**

now we are having 4 equations in 4 unknows solving them simultaneously

we have $x_2 = 2$ 

After solving the above equations, you will get some points. For a point to be accepted, it must satisfy all condolences.


### MATLAB

We can use **MATLAB** to get the optimal point

using [This Script](constrained_non_linear_optimization.m) 

The optimal point is **(0.994 , 1.0006)**. which satsifies all the KKT conditions.

