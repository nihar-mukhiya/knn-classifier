from pandas import *
import tkinter as tk
from tkinter import filedialog
from datascience import *
import copy

root = tk.Tk()
file_path = filedialog.askopenfilename()
e = pandas.read_csv(file_path, header = 0)
b = Table.read_table(file_path)
number_of_rows = b.num_rows
print(e)
col_names = b.labels
print(col_names)
input1 = int(input("enter the index of column to be selected as class: "))
class_name = col_names[input1]
uniq = e[col_names[input1]].unique()
len_uniq = len(uniq)
class_values = []


for y in range(len_uniq):
    clas1 = b.select(col_names[input1]).where(col_names[input1], uniq[y]).num_rows
    probs = clas1 / number_of_rows
    class_values.append(probs)
print(class_values)

temp = copy.deepcopy(list(col_names))
temp.remove(temp[input1])
print(temp)
dict = dict.fromkeys(uniq, [])

print("enter constraints for each column: ")
collect = []
for i in range(len(temp)):
    #list2 = []
    temp2 = input("for "+temp[i]+": ")
    collect.append(temp2)
    temp3 = b.where(temp[i], collect[i])
    for y in range(len_uniq):
        list2 = []
        temp4 = temp3.where(class_name, uniq[y]).num_rows
        #list2.append(temp4)
    dict[uniq[y]].append(temp4)
print(dict)