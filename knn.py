from pandas import *
import tkinter as tk
from tkinter import filedialog
from math import sqrt
from scipy import stats

root = tk.Tk()
file_path = filedialog.askopenfilename()
e = pandas.read_csv(file_path, header = 0)

input_x = int(input("enter x: "))
input_y = int(input("enter y: "))
input_k = int(input("enter k: "))
collect = []

## calculating euclidian distance
col_names = list(e)
j = 0
dict = {}
for i in range(len(e.index)):
    print(i)
    temp = 0
    temp = ((input_x - int(e.iloc[i][j]))**2) + ((input_y - int(e.iloc[i][j+1]))**2)
    temp = sqrt(temp)
    collect.append(temp)
    dict[temp] = e.iloc[i][j+2]
print(collect)
print(dict)
collect.sort()
list2 = collect[0: input_k]
list3 = []
for m in list2:
    list3.append(dict[m])
common = max(set(list3), key=list3.count)
print(list3)
print("your entry belongs to class: " +common)
