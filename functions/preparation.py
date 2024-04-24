import numpy as np
import os
import sys

def correct_path(file_name : str):
    txt_path = 'data/'+file_name+'.txt'
    csv_path = 'data/'+file_name+'.csv'
    if os.path.isfile(csv_path) or os.path.isfile(txt_path):
        return True
    else:
        sys.exit('Error: Wrong file name, please try again')

def EIS_txt(file_name : str):
    
    txt_path = 'data/'+file_name+'.txt'
    csv_path = 'data/'+file_name+'.csv'
    
    if os.path.isfile(csv_path):
        print('no need for data prep., csv file already exists')
        return
    
    with open(txt_path, 'r', errors='ignore') as file:    
        lines = file.readlines()
    lines = lines[7:]

    lines = [line.replace('               ', ',') for line in lines]
    lines = [line.replace('  ', '') for line in lines]
    lines.insert(0, "Частота. Гц,Re. Ом,Im. Ом\n")

    with open(txt_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)

    os.rename(txt_path, csv_path)

#Not finished
def DC_txt(file_name : str):
    txt_path = 'data/'+file_name+'.txt'
    csv_path = 'data/'+file_name+'.csv'
    if os.path.isfile(csv_path):
        print('no need for data prep., csv file already exists')
        return
    
    print('a')
    
    
def sort_boundaries(boundaries : list):
    # sort each duple
    sorted_left_right_list = [sorted(elem) for elem in boundaries]
    # sort
    sorted_list = sorted(sorted_left_right_list, key=lambda x: x[0])
    return sorted_list

def data_slicing(Re : list, Im : list, x_left, x_right):
    
    X = np.array(Re)
    Y = np.array(Im)
    indices = (X >= x_left) & (X <= x_right)
    X_sliced = X[indices]
    Y_sliced = Y[indices]
    
    return X_sliced, Y_sliced