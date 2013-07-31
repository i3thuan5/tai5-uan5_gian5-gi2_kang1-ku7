'''
Created on 2013/7/31

@author: chhsueh
'''

from html.parser import HTMLParser

class HakkaHTMLParser(HTMLParser):
    剖析結果=[]
    字體內量=0
    表格內=False
    def 剖析客話辭典檔案(self,檔名):
        檔案=open(檔名)
        資料=檔案.read()
        檔案.close()
        return self.剖析客話辭典網頁(資料)
    def 剖析客話辭典網頁(self,資料):
        self.初始化剖析結果()
        self.feed(資料)
        return self.目前剖析結果()
    def 初始化剖析結果(self):
        self.剖析結果=[]
    def 目前剖析結果(self):
        return self.剖析結果
    def handle_starttag(self, tag, attrs):
        if self.字體內量>0 and self.表格內:
            if tag=="td":
                self.剖析結果.append('')
        if tag=="font":
            self.字體內量+=1
        elif tag=="table":
            self.表格內=True
    def handle_endtag(self, tag):
#         if self.字體內量>0 and self.表格內:
#             if tag=="td":
#                 print()
        if tag=="font":
            self.字體內量-=1
        elif tag=="table":
            self.表格內=False
    def handle_data(self, data):
        if self.字體內量>0 and self.表格內:
            if len(self.剖析結果)>0:
                self.剖析結果[-1]+=data.strip()
#                 print('', data.strip(),'',end='',sep='')

class 客語辭典剖析結果處裡(HTMLParser):
    剖析結果=[]
    字體內量=0
    表格內=False
    #['詞目', '【熱天】', '詞性: 名', '各家用字表', '四縣音', 'ngied5tien24', '', '海陸音', 'ngied2tien53', '', '大埔音', 'ngied54tien33', '', '饒平音', 'ngied5tien11', '', '詔安音', 'ngied43teen11', '', '釋義', '夏天。例：熱天个時節，阿姆會摎被骨收起來。（夏天的時候，媽媽會把被子收起來。）', '近義詞', '', '反義詞', '', '文白讀', '', '又\u3000音', '', '多音字', '', '對應華語', '夏天', '圖片', '']
    def 標籤名(self):
        return ['詞目','詞性', '四縣音',  '海陸音', '大埔音', '饒平音',  '詔安音',
                '釋義',  '近義詞',  '反義詞', '文白讀',  '又音',  '多音字','對應華語']
    def 欄位值(self,剖析結果):
        if '詞性' in 剖析結果[2]:
            詞性=剖析結果[2].split(':')[1].strip()
        else:
            詞性=''
        return [剖析結果[1],詞性,剖析結果[5],剖析結果[8],剖析結果[11],剖析結果[14],剖析結果[17],
                剖析結果[20],剖析結果[22],剖析結果[24],剖析結果[26],剖析結果[28],剖析結果[30],剖析結果[32], ]
    def 轉資料庫格式(self,剖析結果):
        return '("'+'","'.join(self.標籤名())+"\") VALUES ('"+"','".join(self.欄位值(剖析結果))+"')"

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)
    def handle_data(self, data):
        print("Encountered some data  :", data)

if __name__ == "__main__":
    parser = MyHTMLParser(strict=False)
    parser = HakkaHTMLParser(strict=False)
    parser.feed('<html><head><title>Test</title></head>'
                '<body><h1>  Parse me!  </h1></body></html>')
    parser.feed('<html><head><title>Test</title></head>'
                '<body><h1>  Parse me!  </h1></body></html>')
    su=open('/home/chhsueh/su.html').read()
#     print(su)
    a=parser.剖析客話辭典網頁(su)
    print(a)
    word=open('/home/chhsueh/word.html').read()
#     print(word)
    a=parser.剖析客話辭典網頁(word)
    print(a)
    
    客語辭典剖析結果=客語辭典剖析結果處裡()
    a=parser.剖析客話辭典檔案('/home/chhsueh/su2.html')
    print(a)
    b=parser.剖析客話辭典檔案('/home/chhsueh/word2.html')
    print(b)
    print(客語辭典剖析結果.標籤名())
    print(客語辭典剖析結果.欄位值( a))
    print(客語辭典剖析結果.轉資料庫格式( a))
    print(客語辭典剖析結果.轉資料庫格式( b))
