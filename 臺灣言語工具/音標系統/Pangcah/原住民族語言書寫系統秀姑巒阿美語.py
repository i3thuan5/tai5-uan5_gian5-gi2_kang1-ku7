# -*- coding: utf-8 -*-
import re

_元音 = {
    'a': 'a', 'i': 'i', 'e': 'ə', 'u': 'u', 'o': 'o',
    'aa': 'aː', 'ii': 'iː', 'ee': 'əː', 'uu': 'uː', 'oo': 'oː',
}
_滑音 = {'w': 'w', 'y': 'j', }
_輔音 = {
    'p': 'p', 't': 't', 'k': 'k',
    "'": 'ʡ', '^': 'ʔ',
    'c': 'ts', 'f': 'f', 'd': 'ɬ',
    's': 's', 'z': 'z', 'x': 'x', 'h': 'ħ',
    'm': 'm', 'n': 'n', 'ng': 'ŋ',
    'r': 'r', 'l': 'ɾ',
}

書寫系統國際音標對應表 = {}
書寫系統國際音標對應表.update(_元音)
書寫系統國際音標對應表.update(_滑音)
書寫系統國際音標對應表.update(_輔音)


def 正規表示法(對應表):
    一个 = []
    兩个以上 = []
    for 書寫 in sorted(對應表.keys(), key=lambda 素: (-len(素), 素)):
        if len(書寫) == 1:
            一个.append(書寫)
        else:
            兩个以上.append(書寫)
    return r'({}|[{}])'.format(
        '|'.join(兩个以上),
        ''.join(一个),
    )


class 原住民族語言書寫系統秀姑巒阿美語:
    寫法檢查 = re.compile(r'{}+\Z'.format(正規表示法(書寫系統國際音標對應表)))
    拆音節檢查 = re.compile(正規表示法(書寫系統國際音標對應表))
    元音音值 = set(_元音.values())
    簡寫塞音 = 'ʔ'

    def __init__(self, 音標):
        super(原住民族語言書寫系統秀姑巒阿美語, self).__init__()
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
        有輔音矣 = False
        for 音素 in 音素陣列[::-1]:
            if 音素 in _輔音:  # 是輔音
                if 有輔音矣 and 有元音矣:
                    是音節上尾一个.append(True)
                    有元音矣 = False
                    有滑音矣 = False
                    有輔音矣 = False
                elif 有元音矣:  # onset
                    是音節上尾一个.append(False)
                    有輔音矣 = True
                else:  # coda
                    是音節上尾一个.append(False)
            elif 音素 in _滑音:  # 是滑音
                if 有滑音矣 and 有元音矣:
                    是音節上尾一个.append(True)
                    有元音矣 = False
                    有滑音矣 = False
                    有輔音矣 = False
                elif 有元音矣:  # onset
                    是音節上尾一个.append(False)
                    有滑音矣 = True
                else:  # coda
                    是音節上尾一个.append(False)
            else:  # 是元音
                if 有元音矣:
                    是音節上尾一个.append(True)
                    有元音矣 = True
                    有滑音矣 = False
                    有輔音矣 = False
                else:
                    是音節上尾一个.append(False)
                    有元音矣 = True
        結果 = [[]]
        for 音素, 音節上尾一个 in zip(音素陣列, 是音節上尾一个[::-1]):
            結果[-1].append(書寫系統國際音標對應表[音素])
            if 音節上尾一个:
                結果.append([])
        if 結果[0][0] in self.元音音值:
            結果[0].insert(0, self.簡寫塞音)
        if 結果[-1][-1] in self.元音音值:
            結果[-1].append(self.簡寫塞音)
        return 結果
