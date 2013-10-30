from subprocess import Popen, PIPE

class 外部程式工具:
    def 專案目錄(self):
        找位置 = Popen(['pwd'], stdout = PIPE)
        for 一逝 in 找位置.stdout:
            程式所在 = 一逝[:-1].decode("utf-8")
        找位置.stdout.close()
        程式所在, 資料夾 = 程式所在.rsplit('/', 1)
        while 資料夾 != 'src' and 資料夾 != '測試':
            程式所在, 資料夾 = 程式所在.rsplit('/', 1)
        return 程式所在