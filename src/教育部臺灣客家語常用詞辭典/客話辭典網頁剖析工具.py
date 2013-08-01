'''
Created on 2013/7/31

@author: chhsueh
'''

from html.parser import HTMLParser

class 客話辭典網頁剖析工具(HTMLParser):
    剖析結果=[]
    字體內量=0
    表格內=0
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
        self.字體內量=0
        self.表格內=0
    def 目前剖析結果(self):
        return self.剖析結果
    def handle_starttag(self, tag, attrs):
        if self.字體內量>0 and self.表格內>0:
            if tag=="td":
                self.剖析結果.append('')
        if tag=="font":
            self.字體內量+=1
        elif tag=="table":
            self.表格內+=1
    def handle_endtag(self, tag):
#         if self.字體內量>0 and self.表格內>0:
#             if tag=="td":
#                 print()
        if tag=="font":
            self.字體內量-=1
        elif tag=="table":
            self.表格內-=1
    def handle_data(self, data):
        if self.字體內量>0 and self.表格內>0:
            if len(self.剖析結果)>0:
                self.剖析結果[-1]+=data.strip()
#                 print('', data.strip(),'',end='',sep='')

if __name__ == "__main__":
    網頁剖析工具 = 客話辭典網頁剖析工具(strict=False)
    網頁剖析工具.feed('<html><head><title>Test</title></head>'
                '<body><h1>  Parse me!  </h1></body></html>')
    網頁剖析工具.feed('<html><head><title>Test</title></head>'
                '<body><h1>  Parse me!  </h1></body></html>')
    su=open('/home/chhsueh/su.html').read()
#     print(su)
    a=網頁剖析工具.剖析客話辭典網頁(su)
    print(a)
    word=open('/home/chhsueh/word.html').read()
#     print(word)
    a=網頁剖析工具.剖析客話辭典網頁(word)
    print(a)
    