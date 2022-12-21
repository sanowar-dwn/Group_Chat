import matplotlib.pyplot as plt
import numpy as np

user_input = input('enter')
break_input = user_input.split(" ")

brands_list = np.array(["bmw", "pepsi"])
occurence = np.array([0, 0])

zipped_array = dict(zip(brands_list, occurence))

for i in zipped_array:
    for j in break_input:
        for i in break_input:
            counter = 0
            counter += 1
            print(counter)
            zipped_array[i]+counter
            print(zipped_array)
        else:
            pass

# plt.bar(brands_list, occurence)
# plt.show()