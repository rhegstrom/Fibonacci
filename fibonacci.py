# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 17:53:20 2022

@author: Roger Hegstrom(rhegstrom@avc.edu)

"""


def make_Fibonacci(N):
    """
    Returns N fibonacci numbers

    Parameters
    ----------
    N : integer
        Amount of fibonacci numbers to generate.

    Returns
    -------
    A list of the generated fibonacci numbers.
    """
    nums = [1, 1]
    
    if N == 1: 
        return [1]
    
    for i in range(2, N):
        nextNum = nums[i - 1] + nums[i - 2]
        nums.append(nextNum)
        
    return nums



if __name__ == "__main__":
    print("Generating the first 20 Fibonacci numbers:")
    print(make_Fibonacci(20))
    
    
    

