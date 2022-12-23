clc
clear all
close all

% create the optimization variables
x1 = optimvar('x1');
x2 = optimvar('x2');

% declare your function
f = (x1 - 2) ^ 2 + (x2 - 2) ^ 2 ;

% create an optimization problem
problem = optimproblem('Objective',f);

% add constrains
first_constraint = x1 ^ 2 - x2 <= 0;
second_constraint = x1 + x2 <= 2;

% add the constrains to the problem
problem.Constraints.constr = first_constraint;
problem.Constraints.constr2 = second_constraint;

% initail point
x0.x1 = 3;
x0.x2 = 3;

[sol,fval] = solve(problem,x0);
