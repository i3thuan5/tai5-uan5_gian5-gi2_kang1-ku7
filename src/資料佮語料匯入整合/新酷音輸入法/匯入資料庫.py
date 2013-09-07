from 新酷音輸入法.詞庫整理 import 整理詞庫
from 新酷音輸入法.字表整理 import 整理字表
from 言語資料庫.公用資料 import 資料庫連線

資料庫指令 = 資料庫連線.prepare('INSERT INTO "新酷音輸入法"."字詞" ' + 
    '("字","音") ' + 'VALUES ($1,$2) ')

if __name__ == "__main__":
    接表 = list(整理字表())
    接表.extend(整理詞庫())
    合表 = set(接表)
#    print(len(合表))
    for 字, 注音 in 合表:
        資料庫指令(字, 注音)
        
