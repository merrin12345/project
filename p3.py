dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

'''Output

     area    capital       country  population
0   8.516   Brasilia        Brazil      200.40
1  17.100     Moscow        Russia      143.50
2   3.286  New Dehli         India     1252.00
3   9.597    Beijing         China     1357.00
4   1.221   Pretoria  South Africa       52.98'''

#to change the index
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# Print out brics with new index values
print(brics)
'''Output

       area    capital       country  population
    BR   8.516   Brasilia        Brazil      200.40
    RU  17.100     Moscow        Russia      143.50
    IN   3.286  New Dehli         India     1252.00
    CH   9.597    Beijing         China     1357.00
    SA   1.221   Pretoria  South Africa       52.98
'''