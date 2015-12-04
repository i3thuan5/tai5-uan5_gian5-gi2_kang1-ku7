# -*- coding: utf-8 -*-
import os
from subprocess import Popen


from 臺灣言語工具.系統整合.外部程式 import 外部程式


class 摩西服務端():

    def __init__(self,
                 moses模型資料夾路徑,
                 埠='8080',
                 moses資料夾路徑=外部程式.moses預設目錄(),
                 ):
        self.執行程式 = os.path.join(moses資料夾路徑, 'bin', 'mosesserver')
        if not os.path.isfile(self.執行程式):
            raise OSError('{0}程式無存在！！'.format(self.執行程式))
        self.模型路徑 = os.path.join(moses模型資料夾路徑, 'model', 'moses.ini')
        if not os.path.isfile(self.模型路徑):
            raise OSError('{0}模型無存在！！'.format(self.模型路徑))
        self.埠 = 埠
        self.程序 = None

    def 走(self):
        if not self.程序:
            self.程序 = Popen(
                [self.執行程式, '-f', self.模型路徑, '--server-port', str(self.埠)],
            )

    def 狀態(self):
        return self.程序.poll()

    def 等(self):
        return self.程序.wait()

    def 停(self):
        self.程序.terminate()
        self.程序 = None
