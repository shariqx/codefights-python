import pyodbc
import numpy as np

if __name__ == '__main__':
    cnxn = pyodbc.connect(driver='{SQL Server Native Client 11.0}',
                      host='pssql', database='sasaas',
                      user='sasaas', password='111111')
    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM AUTOPLANTASK')
    norm_list = list()
    for row in cursor:
        norm_list.append(row[10])
    # print(norm_list)
    np_arr = np.array(norm_list)
    mean_val = np_arr.mean()
    median_val = np.median(np_arr)
    print("Average planned duration of tasks " +  str(mean_val))
    print("Median planned duration of tasks " +  str(median_val))
    cnxn.close()