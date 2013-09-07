'''
Created on 2013/7/31

@author: chhsueh
'''

def 整理詞庫():
    詞表 = []
    for 逝 in open('/home/ihc/桌面/1020801/新酷音詞庫/tsi'):
        if 逝.strip() == '':
            continue
#        print(逝.strip().split())
        字,頻率,*注音 = 逝.strip().split()
        頻率.split()
        if len(詞表)>0 and 字==詞表[-1][0] and ' '.join(注音)==詞表[-1][1]:
            pass
        elif len(詞表)>0 and 字==詞表[-1][0] and len(字)>1:
            if ('一' in 字 or '兒' in 字 or '刻' in 字 or '場' in 字 or
                '廈' in 字 or '帆' in 字 or '個' in 字):
                詞表.pop()
                詞表.append((字, ' '.join(注音)))
            elif '巫' in 字 or '兒' in 字 or '刻' in 字 or '場' in 字:
                pass
            else:
#                print(詞表[-1])
#                print(逝.strip())
                詞表.append((字, ' '.join(注音)))
        else:
            詞表.append((字, ' '.join(注音)))
#    for 字, 注音 in 詞表:
#        print(字, 注音)
    return 詞表
        
if __name__ == "__main__":
    整理詞庫()
    