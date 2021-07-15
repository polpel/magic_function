import numpy as np
import matplotlib.pyplot as plt
import random

def magic_function(a, b, c):
    options = ['add', 'mult', 'rgb']

    do = random.choice(options)

    if do == 'add':
        sum = a + b + c
        print(f'Adding {a}, {b} and {c} gives {sum}!')
        return

    if do == 'mult':
        product = a * b * c
        print(f'{a} times {b} times {c} equals {product}!')
        return

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