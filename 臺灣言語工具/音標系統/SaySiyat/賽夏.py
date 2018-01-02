import re
from 臺灣言語工具.音標系統.Pangcah.原住民族語言書寫系統秀姑巒阿美語 import 正規表示法

_元音 = {
    'a': 'a', 'i': 'i', 'e': 'e', 'o': 'o', 'oe': 'œ', 'ae': 'æ',
}
_滑音 = {'w': 'w', 'y': 'j', }
_輔音 = {
    'p': 'p', 't': 't', 'k': 'k', "'": 'ʔ',
    'b': 'β', 's': 's', 'z': 'z', 'S': 'ʃ', 'h': 'h',
    'm': 'm', 'n': 'n', 'ng': 'ŋ',
    'r': 'r', 'l': 'l',
    ':': 'L',
}

_國際音標對照表 = {}
_國際音標對照表.update(_元音)
_國際音標對照表.update(_滑音)
_國際音標對照表.update(_輔音)


class 賽夏:
    國際音標對照表 = _國際音標對照表
    元音 = _元音
    滑音 = _滑音
    輔音 = _輔音
    寫法檢查 = re.compile(r'{}+\Z'.format(正規表示法(國際音標對照表)))
    拆音節檢查 = re.compile(正規表示法(國際音標對照表))

    def __init__(self, 音標):
        self.音標 = None
        try:
            if self.寫法檢查.match(音標).group(0) == 音標:
                self.音標 = 音標
        except AttributeError:
            pass

    def 預設音標(self):
        return self.音標

    def 音值(self):
        if self.音標 is None:
            return []
        音素陣列 = self.拆音節檢查.findall(
            self.音標.replace('iy', 'y')
            .replace('ow', 'w')
        )
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
            if 音素 in _輔音:
                結果[-1].append(_輔音[音素])
            elif 音素 in _滑音:
                結果[-1].append(_滑音[音素])
            else:
                結果[-1].append(_元音[音素])
            if 音節上尾一个:
                結果.append([])
        return 結果
