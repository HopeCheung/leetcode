import random
import time
 
 
def random_matrix_genetor(vex_num=10):
    '''
    随机图顶点矩阵生成器
    输入：顶点个数，即矩阵维数
    '''
    data_matrix=[]
    for i in range(vex_num):
        one_list=[]
        for j in range(vex_num):
            one_list.append(random.randint(1, 100))
        data_matrix.append(one_list)
    return data_matrix

def floyd(data_matrix):
    dist_matrix=[]
    path_matrix=[]
    vex_num=len(data_matrix)
    
    for h in range(vex_num):
        one_list=['N']*vex_num
        path_matrix.append(one_list)
        dist_matrix.append(one_list)
        
    for i in range(vex_num):
        for j in range(vex_num):
            dist_matrix=data_matrix
            path_matrix[i][j] = j
            
    for k in range(vex_num):
        for i in range(vex_num):
            for j in range(vex_num):
                if dist_matrix[i][k] == 'N' or dist_matrix[k][j] == 'N':
                    temp = 'N'
                else:
                    temp = dist_matrix[i][k]+ dist_matrix[k][j]
                if dist_matrix[i][j] > temp:
                    dist_matrix[i][j] = temp
                    pateh_matrix[i][j] = path_matrix[i][k]
    return dist_matrix, path_matrix


