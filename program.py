import numpy as np
import matplotlib.pyplot as plt
import random

def magic_function(a, b, c):
    """Returns something random made from three input numbers
    
    A collection of tiny functions that take three numbers and print or
    display something made from them. The function that is actually 
    used at each call of magic_function() is chosen at random.

    Args:
      a, b, c:
        Three numbers, any type is fine.

    Returns:
      A surprise :)
    """
    
    # List of tiny functions implemented
    options = ['add', 'mult', 'rgb']

    do = random.choice(options)
    
    # Adds the numbers together
    if do == 'add':
        sum = a + b + c
        print(f'Adding {a}, {b} and {c} gives {sum}!')
        return
    
    # Multiplies the numbers together
    if do == 'mult':
        product = a * b * c
        print(f'{a} times {b} times {c} equals {product}!')
        return

    # Scales the numbers to 0--1 range (treating largest as 1) and  
    # treats them as RGB values to display a colour
    if do == 'rgb':
        largest = max(a, b, c)
        a_rgb = a / largest
        b_rgb = b / largest
        c_rgb = c / largest

        img = [[(a_rgb, b_rgb, c_rgb)]]

        plt.imshow(img)
        plt.title('Your numbers turned into a colour :)')
        plt.show()
        return