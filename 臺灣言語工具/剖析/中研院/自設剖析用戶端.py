# -*- coding: utf-8 -*-
import telnetlib


class 自設剖析用戶端:
    主機 = "140.113.207.101"
    埠 = 23222

    def 剖析(self, 愛轉換的字串):
        大五碼字串 = 愛轉換的字串.encode('big5')
        連線 = telnetlib.Telnet(self.主機, self.埠, 0.5)
        連線.write(大五碼字串)
        結果 = 連線.read_all().decode('big5')
        連線.close()
        return 結果.replace('\r', '').rstrip().split('\n')
