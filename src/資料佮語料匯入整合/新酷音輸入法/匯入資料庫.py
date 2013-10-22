from 資料佮語料匯入整合.新酷音輸入法.字表整理 import 整理字表
from 資料佮語料匯入整合.新酷音輸入法.詞庫整理 import 整理詞庫
from 資料庫.資料庫連線 import 資料庫連線



if __name__ == "__main__":
    資料庫指令 = 資料庫連線.prepare('INSERT INTO "新酷音輸入法"."字詞" ' + 
    '("字","音") ' + 'VALUES ($1,$2) ')
    接表 = list(整理字表())
    接表.extend(整理詞庫())
    合表 = set(接表)
#    print(len(合表))
    for 字, 注音 in 合表:
        資料庫指令(字, 注音)
        
