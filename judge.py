########################################################
################ Final Judge Coin Flip #################
########################################################
#------------------------------------------------------#
# This function takes in a real number < 1. This number is 
# the success rate determined by the ratio of mission vector and 
# target mission vector. If p > = 1, then you automatically succeed.
# If p < 1, you toss a biased coin which is simulated with binomial 
# distribution. If the coin is head (1), then you succeed in mission, 
# and if the coin is tail (0), you fail the mission. 
#-------------------------------------------------------#
##########################################################

# import numpy module
import numpy as np

def judge(p):
    
    if p >= 1: # you already succeeded
        print('Mission success!!! You get a bonus!')
        print('Your Estimated Success Rate: '+str(p*100) + ' %')
    else : # if not succeeded, flip a biased coin
        x = np.random.binomial(1,p)
        if x == 1 : # heads, you succeed. Luck you if you had low chance!
            print('Mission Success!')
            print('Your Estimated Success Rate: '+str(p*100) + ' %')
            return "success"
        else : # tails, you fail...
            print('Fail...')
            print('Your Estimated Success Rate: '+str(p*100) + ' %')
            return "fail"
# test
fail = 0
suc = 0
for i in range(100):
    if judge(0.3) in "success":
        suc+=1
    else:
        fail+=1

print("suc: " + str(suc))
print("fail: " + str(fail))
print(suc/100)

