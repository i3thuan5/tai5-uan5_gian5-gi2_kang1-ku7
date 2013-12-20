import os
import xlrd
from 資料庫.資料庫連線 import 資料庫連線

class 表格檔案匯入資料庫:
    def __init__(self):
        檔案所在='twblg_data_20131213'
        資料庫名='教育部臺灣閩南語常用詞辭典'
        清資料庫指令 = ('DELETE FROM "{0}"."{1}" ')
        加資料指令 = ('INSERT INTO "{0}"."{1}" ' +
                'VALUES ({2})')
        for 檔名 in os.listdir(檔案所在):
            if 檔名.endswith('.xls'):
                print(檔名)
                表格檔=xlrd.open_workbook('{0}/{1}'.format(檔案所在,檔名))
                for 表格名 in 表格檔.sheet_names():
                    表格=表格檔.sheet_by_name(表格名)
                    if 表格名=='cuankho':
                        表格名='語音方言差'
                    elif 表格名=='cuankho_p':
                        表格名='詞彙方言差'
                    elif 表格名=='反義詞':
                        表格名='反義詞對應'
                    print(表格名)
                    print(表格.row_values(0))
                    
                    清資料庫=清資料庫指令.format(資料庫名,表格名)
                    資料庫連線.execute(清資料庫)
                    for 第幾逝 in range(1,表格.nrows):
                        print(表格.row_values(第幾逝))
                        資料=[]
                        for 表資料 in 表格.row_values(第幾逝):
                            if isinstance(表資料, float):
                                資料.append(str(int(表資料)))
                            else:
                                資料.append("'{0}'".format(表資料))
                        加資料=加資料指令.format(資料庫名,表格名,','.join(資料))
                        print(加資料)
                        資料庫連線.execute(加資料)
            
if __name__=='__main__':
    表格檔案匯入資料庫()