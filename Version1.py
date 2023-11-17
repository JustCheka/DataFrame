import random
import pandas as pd
 
lst = ['robot'] * 10
lst += ['human'] * 10
lst += ['animal'] * 10 
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

unique_elements = list(set(lst))
del data['whoAmI']

for i in range(len(unique_elements)):
    arr = []
    for j in range(len(lst)):
        if (unique_elements[i] == lst[j]):
            arr.append(1)
        else:
            arr.append(0)
    data[f'WhoAmI_{unique_elements[i]}'] = arr
    arr = []

print(data)
