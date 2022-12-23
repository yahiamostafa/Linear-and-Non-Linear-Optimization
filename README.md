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

### Hand Analysis Solution

1) **Lagrangian function** ==> $L(x_1,x_2,s_1,s_2) = (x_1 - 2 ) ^ 2 + (x_2 - 2) ^ 2 + λ_1(x_1 + x_2 - 2 + s_1^2) + λ_2(x_1^2 - x_2 + s_2^2)$

where **s_1 & s_2** are slack variables.

2) **Kuhn-Tucker Conditions**

$x_1 + x_2 <= 2$

$x_1^2 - x_2 <= 0$ 

$λ_1(x_1 + x_2 - 2 + s_1^2) = 0$

$λ_2(x_1^2 - x_2 + s_2^2)$

$λ_1 >= 0 & λ_2 >= 0$

<svg fill="none" viewBox="0 0 600 300" width="600" height="300" xmlns="http://www.w3.org/2000/svg">
  <foreignObject width="100%" height="100%">
    <div xmlns="http://www.w3.org/1999/xhtml">
      <style>
        @keyframes hi  {
            0% { transform: rotate( 0.0deg) }
           10% { transform: rotate(14.0deg) }
           20% { transform: rotate(-8.0deg) }
           30% { transform: rotate(14.0deg) }
           40% { transform: rotate(-4.0deg) }
           50% { transform: rotate(10.0deg) }
           60% { transform: rotate( 0.0deg) }
          100% { transform: rotate( 0.0deg) }
        }

        @keyframes gradient {
          0% {
            background-position: 0% 50%;
          }
          50% {
            background-position: 100% 50%;
          }
          100% {
            background-position: 0% 50%;
          }
        }

        .container {
          --color-main: #5452ee;
          --color-primary: #e73c7e;
          --color-secondary: #23a6d5;
          --color-tertiary: #ffff;

          background: linear-gradient(-45deg, var(--color-main), var(--color-primary), var(--color-secondary), var(--color-tertiary));
          background-size: 400% 400%;
          animation: gradient 15s ease infinite;

          width: 100%;
          height: 300px;

          display: flex;
          justify-content: center;
          align-items: center;
          color: white;

          font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
        }

        .hi {
          animation: hi 1.5s linear -0.5s infinite;
          display: inline-block;
          transform-origin: 70% 70%;
        }

        @media (prefers-color-scheme: light) {
          .container {
            --color-main: #F15BB5;
            --color-primary: #24b0ef;
            --color-secondary: #4526f6;
            --color-tertiary: #f6f645;
          }
        }

        @media (prefers-reduced-motion) {
          .container {
            animation: none;
          }

          .hi {
            animation: none;
          }
        }
      </style>

      <div class="container">
        <h1>Hi there, my name is Nikola <div class="hi">👋</div></h1>
      </div>
    </div>
  </foreignObject>
</svgg
