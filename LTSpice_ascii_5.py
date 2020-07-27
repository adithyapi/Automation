# -------------------------------------------------------------------------------
# Name:        LTSpice_ascii_5.py
# Purpose:     Process LTSpice output files(.raw) and align data for usage in a spread-
#              sheet tool such as Excel, or Calc.
#
# Author:      Adithya Pai (adithyapaip96@gmail.com)
#
# Created:     26-04-2020
# Licence:     Commertial
# Version:     0.1  Transforming the procedure into a callable one in order
#              to call them from a higher level script.
# -------------------------------------------------------------------------------

import time
start=time.perf_counter()
import pandas as pd
import re
import os
import numpy as np


filne = 'SS.raw'
alt_data='alt_data.txt'
ascii_data='acii_data.txt'




#File Manipulation Starts Here**************************************************
with open(filne, 'r+') as f:
    for line in f:
        if line.startswith("Flags: "):
            var=(next(f))
            print(var)
            var_temp=var.split()
            temp=var_temp[2]
            No_of_var=int(temp)
            print(No_of_var)
            mat=pd.DataFrame(index=range(1),columns=range(No_of_var))
            print(mat)
            count=0
            var_simp= No_of_var-1
            break

             
            # StopIteration if the last line is also a match.
f.close()

with open(filne, 'r+') as f:
    for line in f:
        if line.startswith("Variables:"):
           for No_of_var in range(No_of_var,0,-1):
            name=(next(f))
            print(name)
            name_temp=name.split()
            print(name_temp[1])
            mat.iloc[0, mat.columns.get_loc(count)]=name_temp[1]
            count=count+1
    print(mat)

f.close()
"""
with open(filne,'r+') as fin, open(alt_data,'w+') as fout:
    for line in fin:
     if line.startswith("Values:"):
        for line in fin:
          fout.write(line[:-1] + '          ' + next(fin))
"""
i=1   
file_list=[]          
with open(filne,'r+') as fin, open(alt_data,'w+') as fout:
 for line in fin:
    if line.startswith("Values:"):
       print("Got_Value")
       for line in fin:
            file_list.append(line.strip())
            if i <= var_simp :
                i=i+1
            else:
             str1 = '    '.join(file_list)
             fout.write(str1)
             fout.write("\n")
             file_list.clear()
             i=1


data = pd.read_csv(alt_data,sep='\t',index_col=0) 

data.drop(data.columns[0], axis=1,inplace=True)

data.to_csv(ascii_data, sep='\t',index=False)

data = pd.read_fwf(ascii_data,sep='\t')

#print(data.shape)

#print(data)

data.columns = mat.iloc[0].tolist()

data.to_csv(ascii_data, sep='\t',index=False)

#File Manipulation Ends Here**********************************************


end=time.perf_counter()
Performance=end-start
print(Performance)