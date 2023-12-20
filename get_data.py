import numpy as np

def get_path(day_number):
    
    day_number_str = str(day_number)
    
    return './data/day_' + str(day_number) + '.txt'

def string_as_matrix(data_str):
    
    lines = data_str.splitlines()
    char_list = [[char for char in line] for line in lines]
    
    return np.array(char_list)

def file_as_matrix(day_number):
    
    path = get_path(day_number)
    
    with open(path, 'r') as file:
        
        lines = file.read().splitlines()
        char_list = [[char for char in line] for line in lines]
    
    return np.array(char_list)