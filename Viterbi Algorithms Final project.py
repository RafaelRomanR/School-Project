#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
"""
Rafael A. Roman-Rodriguez
CSC 314 introduction to Bioinformatics 
Viterbi Algorithm Final Project 

"""
# coins probability store in a dictionary with transitions probability
fair = {'start': math.log2(0.50),
        'head': math.log2(0.50),
        'tail': math.log2(0.50),
        'FF': math.log2(0.90),
        'BF': math.log2(0.10)}

bias = {'start': math.log2(0.50),
        'head': math.log2(0.80),
        'tail': math.log2(0.20),
        'BB': math.log2(0.90),
        'FB': math.log2(0.10)}

# emissions store in a dictionary
fair_emissions = {
     'H': fair['head'],
     'T': fair['tail']
}

bias_emissions = {
    'H': bias['head'],
    'T': bias['tail']
}

# store the observation
observation = input('Enter the observation state by H (head) or T (tail) e.g. HTH').upper()

# store the calculation of state
fair_cal = []
bias_cal = []

#store the state
fair_path = []
bias_path = []

#store the optimal path
optimal_path = ''
optimal_state = 0
#keep track of the last state for the traceback
last_state = ''
last_path = ''

#initialize calculation with the starting probalitity
for s in range(1):
        F_start = fair['start'] + fair_emissions[observation[s]]
        fair_cal.append(F_start)
        fair_path.append('SF')
        
        B_start= bias['start'] + bias_emissions[observation[s]]
        bias_cal.append(B_start)
        bias_path.append('SB')

# calculate the probabilities and store the highest one 
for o in range(1,len(observation)):
    
    # equation = previous state probablity calculated + transition to coin probality + coin state probality 
    FF = fair_cal[o-1] + fair['FF'] + fair_emissions[observation[o]]
    BF = bias_cal[o-1] + fair['BF'] + fair_emissions[observation[o]]
    
    # find and store the highest probability fair row 
    if FF > BF:
        fair_cal.append(FF)
        fair_path.append('FF')   
    elif BF > FF:
        fair_cal.append(BF)
        fair_path.append('BF')
        

    # equation = previous state calculated + transition to coin probablity + coin state probality 
    BB = bias_cal[o-1] + bias['BB'] + bias_emissions[observation[o]]
    FB = fair_cal[o-1] + bias['FB'] + bias_emissions[observation[o]]
    
    # find and store the highest probability for bias row
    if BB > FB:
        bias_cal.append(BB)
        bias_path.append('BB') 
    elif FB > BB:
        bias_cal.append(FB)
        bias_path.append('FB')
        

# find the optimal state
if fair_cal[-1] > bias_cal[-1]:
    last_state = fair_path[-1][1] # store the current State of the path 
    last_path = fair_path[-1][0]  # mechanism to switch wether the calculation came from FB or BF  
    optimal_path = last_state     # store the state in the optimal path
    optimal_state = fair_cal[-1]  # store the optimal state 
else:
    last_state = bias_path[-1][1]
    last_path = bias_path[-1][0]
    optimal_path = last_state
    optimal_state = bias_cal[-1]

# traceback to find the optimal path
""" The last path store where the calcualtion came from if the calculation 
    was from FB then it store the F in the last_path and B in the last_state
    now it will look on the Fair calculation list. 
    
    The last_path keep track of where it came from to switch from bias_cal list or fair_cal list
"""
for i in range(len(observation)-1, 0, -1):
    if last_path == 'F':
        last_state = fair_path[i-1][1]
        last_path = fair_path[i-1][0]
        optimal_path = last_state + optimal_path

    else:
        last_state = bias_path[i-1][1]
        last_path = bias_path[i-1][0]
        optimal_path = last_state + optimal_path

print('\nState observation:',observation)
print('Optimal state:', optimal_state)
print('Optimal path:', optimal_path)
print()
print('F', fair_cal)
print(fair_path)
print('B',bias_cal)
print(bias_path)


# In[ ]:




