from 新酷音輸入法.詞庫整理 import 整理詞庫

def 整理字表():
    對照表 = {}
    for 逝 in open('/home/ihc/桌面/1020801/新酷音詞庫/對應表'):
        if 逝.strip() == '':
            continue
#        print(逝.strip().split())
        鍵, 音 = 逝.strip().split()
        對照表[鍵] = 音
    字表 = set()
    for 逝 in open('/home/ihc/桌面/1020801/新酷音詞庫/phone'):
        if 逝.strip() == '':
            continue
#        print(逝.strip().split())
        鍵盤, 字 = 逝.strip().split()
        注音 = ''
        for 鍵 in 鍵盤:
            注音 += 對照表[鍵]
        字表.add((字, 注音))
    return 字表

if __name__ == "__main__":
    接表 = list(整理字表())
    接表.extend(整理詞庫())
    合表 = set(接表)
#    print(len(合表))
    輸出 = open('/home/ihc/桌面/1020801/新酷音詞庫/all', 'w')
    for 字, 注音 in 合表:
        print(字, 注音, file=輸出)
        
