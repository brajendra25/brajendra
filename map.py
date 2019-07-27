
exp_list = [1,2,3,4,5,6,7]
data_list = ['A','C','B','E','G','D','F','I']
exp_list.sort(reverse=True)
data_list.sort()


print(exp_list)
print(data_list)

import pandas as pd

path = "E:\\Brajendra\\Big Data\\DataSets\\Fire_Department_Calls_for_Service.csv";


csv = open(path, 'r')
columns = csv.readline().split(",")
for col in columns:
    print(col + " STRING,")