import telnetlib

class 自設剖析工具:
    主機="140.113.207.101"
    連接埠=23222
    def 剖析(self, 愛轉換的字串):
        連線 = telnetlib.Telnet(self.主機,self.連接埠)
        連線.write(愛轉換的字串.encode('big5') )
        結果=連線.read_all().decode('big5')
        連線.close()
        return 結果.replace('\r','').rstrip().split('\n')
        
        
if __name__ == '__main__':
    工具 = 自設剖析工具()
    print(工具.剖析('我想吃飯。我想吃很多飯。'))
