########################################################
########### Skewed Random Number Generator #############
########################################################
#------------------------------------------------------#
# The function takes in 5 different integers greater than 1.
# Each input is responsible for modulating the probability of 
# getting certain number in a hard-coded range: 
#
# x1 = [1.0. 1.2]; x2 = [1.2, 1.4]; x3 = [1.4, 1.6]; 
# x4 = [1.6, 1.8]; x5 = [1.8, 2.0]. 
#
# For example, if you want to generate a number between 1.2 and 1.4 
# twice as often as other numbers, then input is: 
# [x1, x2, x3, x4, x5] = [1, 2, 1, 1, 1]
# You could easily alter the range by hard-coding if you wish 
# but this is probably sufficient for our purpose.  
#-------------------------------------------------------#
##########################################################

# import numpy module
import numpy as np

# begin function
def skewRandGen (x1, x2, x3, x4, x5):
    # Generate a random number between 0 and 100 
    # with step size of 1
    r = np.arange(0,100,1)
    
    # Define probability interval for 100 numbers. 
    # x1 = 0~19; x2 = 20~39; x3 = 40~59; x4 = 60~79; x5 = 80~100
    x = ( [x1] * 20 + [x2] * 20 
    + [x3] * 20 + [x4] * 20 
    + [x5] * 20 )
    
    # Normalize the probability to 1.0 
    x /= np.sum(x)
    
    # Generate random sample. 
    # Divide by 100 and add 1 so the number is between 1 and 2.
    result = np.random.choice(r, 1, p=x)/100 + 1
    return float(result)

# a test script here
test = skewRandGen(1, 100, 1, 50, 100)
print(f"The result is {test}")

