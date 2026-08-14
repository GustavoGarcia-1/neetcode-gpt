#inputs : 
    #iterations - how many gradient descent steps to execute. Can be zero (meaning return the initial value unchanged) must be >= 0 ,
        # possible method - iterations == 0
    #learning rate - the step size multiplier alpha that scales each gradient update., strictly between 0 and 1.
        # the bigger the learning rate the more change., closer to zero = less change
    #init - starting point for optimization. Can be any number (including zero)

# Apply the update rule for hte specified number of iterations starting fom init, then retrun the final value of x 
# Use round to output to 5 decimial places

# while iterations != 0 
#   plug inputs into this function "x,new = init aka x,old - learning rate (f'(x)) "
class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        x = init
        f_x = None
        while iterations != 0:
            f_x = 2 * x
            x = x - (learning_rate * f_x)
            iterations = iterations - 1 
        x = round (x, 5)
        return x
        pass
