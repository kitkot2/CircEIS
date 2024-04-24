import os

def EIS_txt(file_name : str):
    
    with open('data/'+file_name+'.txt', 'r', errors='ignore') as file:    
        lines = file.readlines()
    lines = lines[7:]

    lines = [line.replace('               ', ',') for line in lines]
    lines = [line.replace('  ', '') for line in lines]
    lines.insert(0, "Частота. Гц,Re. Ом,Im. Ом\n")

    with open('data/'+file_name+'.txt', 'w', encoding='utf-8') as file:
            file.writelines(lines)

    os.rename('data/'+file_name+'.txt', 'data/'+file_name+'.csv')



def DC_txt(file_name : str):
    print('a')