""" convert a vector of raw scores "[1 0 2]" turn them into a probability distrubution, output values that are all positive and sum to 1, such that they are interpretable as probabilties, formula for the 9th element is softmax(z) to i = e^zi / sum from j to e^zj
"""
"""
'input : "z" a 1d NumPy array of logits 
output : "array that is all positive and sums to 1 : [0.2 , 0.05, 0.05, 0.7]'

CODE :
return e to the z minus max(z) divided by sum from lower limit j e^z - max(z)
"""

import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        return np.round(np.exp((z - np.max(z)))/(sum(np.exp(z - np.max(z)))),4)
