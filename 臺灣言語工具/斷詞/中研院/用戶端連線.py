# -*- coding: utf-8 -*-
from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
import re
import sys
import time


class 用戶端連線:
    檢查結果 = re.compile('<result>(.*)</result>')
    檢查空結果 = re.compile('<result/>')
    分句 = re.compile('<sentence>(.*?)</sentence>')
    回傳狀況 = re.compile('<processstatus code="\d">(.*?)</processstatus>')
    傳去格式 = '''
<?xml version="1.0" ?>
<wordsegmentation version="0.1" charsetcode='{}' >
<option showcategory="1" />
<authentication username="{}" password="{}" />
<text>{}</text>
</wordsegmentation>
'''

    def __init__(self, 主機, 埠, 編碼, 帳號, 密碼):
        self.編碼 = 編碼
        self.主機 = 主機
        self.埠 = 埠
        self.帳號 = 帳號
        self.密碼 = 密碼

    def _語句做了嘛是語句(self, 語句, 等待=3, 一定愛成功=False):
        # 官方功能無記錄原本換逝資訊，所以愛一逐一擺
        結果 = []
        for 一逝 in 語句.split('\n'):
            愛做 = 一逝.strip()
            if 愛做 == '':
                continue
            while True:
                try:
                    逐逝 = self._連線(
                        愛做, 等待, self.編碼, self.主機, self.埠, self.帳號, self.密碼)
                    結果.append(逐逝)
                except Exception as 問題:
                    if 一定愛成功:
                        print('連線失敗，小等閣試……。原因：{0}'.format(問題),
                              file=sys.stderr)
                        time.sleep(10)
                    else:
                        raise
                else:
                    break
        return 結果

    def _連線(self, 語句, 等待, 編碼, 主機, 埠, 帳號, 密碼):
        連線 = socket(
            AF_INET, SOCK_STREAM)
        連線.settimeout(等待)
        try:
            連線.connect((主機, 埠))
        except:
            raise RuntimeError("連線逾時")
        資料 = self.傳去格式.format(編碼, 帳號, 密碼, 語句).encode(編碼)
# 		print('送出', 資料)
        已經送出去 = 0
        while 已經送出去 < len(資料):
            這擺送出去 = 連線.send(資料[已經送出去:])
            if 這擺送出去 == 0:
                raise RuntimeError("連線出問題")
            已經送出去 += 這擺送出去
        全部收著資料 = b''
        走 = True
        while 走:
            這擺收著資料 = 連線.recv(1024)
            if 這擺收著資料 == b'':
                raise RuntimeError("連線出問題")
            全部收著資料 = 全部收著資料 + 這擺收著資料
            if b'</wordsegmentation>' in 全部收著資料:
                走 = False
        連線.close()
        全部收著字串 = 全部收著資料.decode(編碼)
# 		print('收著', 全部收著字串)
        收著結果 = self.檢查結果.search(全部收著字串)
        if 收著結果 is not None:
            逐逝 = self.分句.split(收著結果.group(1))[1::2]
            return 逐逝
        if self.檢查空結果.search(全部收著字串) is not None:
            return []
        狀況 = self.回傳狀況.split(全部收著字串)
        if 狀況 is not None:
            # <processstatus code="1">Service internal error</processstatus>
            # <processstatus code="2">XML format error</processstatus>
            # <processstatus code="3">Authentication failed</processstatus>
            raise RuntimeError(狀況[1])
        raise RuntimeError('回傳的資料有問題！！')
