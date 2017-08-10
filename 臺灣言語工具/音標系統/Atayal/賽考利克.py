import re
from 臺灣言語工具.音標系統.Pangcah.原住民族語言書寫系統秀姑巒阿美語 import 正規表示法

_元音 = {
    'a': 'a', 'i': 'i', 'e': 'e', 'u': 'u', 'o': 'o', '_': 'ə',
}
_滑音 = {'w': 'w', 'y': 'j', }
_輔音 = {
    'p': 'p', 't': 't', 'k': 'k', 'q': 'q',
    "'": 'ʔ',
    'c': 'ts', 'b': 'β',
    's': 's', 'z': 'z', 'x': 'x', 'g': 'ɣ', 'h': 'h',
    'm': 'm', 'n': 'n', 'ng': 'ŋ',
    'r': 'r', 'l': 'l',
}

_國際音標對照表 = {}
_國際音標對照表.update(_元音)
_國際音標對照表.update(_滑音)
_國際音標對照表.update(_輔音)


class 賽考利克:
    國際音標對照表 = _國際音標對照表
    元音 = _元音
    滑音 = _滑音
    輔音 = _輔音
    寫法檢查 = re.compile(r'{}+\Z'.format(正規表示法(國際音標對照表)))
    拆音節檢查 = re.compile(正規表示法(國際音標對照表))
    輔音音值 = set(輔音.values())

    def __init__(self, 音標):
        對應 = self.寫法檢查.match(音標.lower())
        if 對應:
            self.音標 = 音標
        else:
            self.音標 = None

    def 預設音標(self):
        return self.音標

    def 音值(self):
        if self.音標 is None:
            return []
        音素陣列 = self.拆音節檢查.findall(self.音標.lower())
        是音節上尾一个 = []
        有元音矣 = False
        有滑音矣 = False
        有onset矣 = False
        有coda矣 = False
        for 音素 in 音素陣列[::-1]:
            if 音素 in self.輔音:  # 是輔音
                if 有onset矣 and 有元音矣:
                    是音節上尾一个.append(True)
                    有元音矣 = False
                    有滑音矣 = False
                    有onset矣 = False
                    有coda矣 = True
                elif 有元音矣:  # onset
                    是音節上尾一个.append(False)
                    有onset矣 = True
                elif 有coda矣:  # schwa
                    是音節上尾一个.append(True)
                    有元音矣 = False
                    有滑音矣 = False
                    有onset矣 = False
                    有coda矣 = True
                else:  # coda
                    是音節上尾一个.append(False)
                    有onset矣 = False
                    有coda矣 = True
            elif 音素 in self.滑音:  # 是滑音
                if 有滑音矣 and 有元音矣:
                    是音節上尾一个.append(False)
                elif 有元音矣:  # onset
                    是音節上尾一个.append(False)
                    有滑音矣 = True
                else:  # coda
                    是音節上尾一个.append(False)
                    有滑音矣 = True
            else:  # 是元音
                if 有元音矣:
                    是音節上尾一个.append(True)
                    有元音矣 = True
                    有滑音矣 = False
                    有onset矣 = False
                    有coda矣 = False
                else:
                    是音節上尾一个.append(False)
                    有元音矣 = True
        結果 = [[]]
        for 音素, 音節上尾一个 in zip(音素陣列, 是音節上尾一个[::-1]):
            結果[-1].append(self.國際音標對照表[音素])
            if 音節上尾一个:
                結果.append([])
        for 音節 in 結果:
            if len(音節) == 1 and 音節[0] in self.輔音音值:
                音節.append('ə')
        return 結果
