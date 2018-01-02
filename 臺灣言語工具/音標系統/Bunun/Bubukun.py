import re
from 臺灣言語工具.音標系統.Pangcah.原住民族語言書寫系統秀姑巒阿美語 import 正規表示法

_元音 = {
    'a': 'a', 'i': 'i', 'o': 'o', 'e': 'e', 'u': 'u',

}
_輔音 = {
    'p': 'p', 'b': 'b', 't': 't', 'd': 'd',  'k': 'k',
    'c': 'ts',
    's': 's', 'z': 'ð', 'v': 'v', 'h': 'h',
    'm': 'm', 'n': 'n', 'ng': 'ŋ',
    'l': 'l',
}

_國際音標對照表 = {'-': 'ʔ'}
_國際音標對照表.update(_元音)
_國際音標對照表.update(_輔音)


class Bubukun:
    國際音標對照表 = _國際音標對照表
    元音 = _元音
    輔音 = _輔音
    寫法檢查 = re.compile(r'{}+\Z'.format(正規表示法(國際音標對照表)))
    拆音節檢查 = re.compile(正規表示法(國際音標對照表))

    def __init__(self, 音標):
        self.音標 = None
        try:
            小寫音標 = 音標.lower()
            if self.寫法檢查.match(小寫音標).group(0) == 小寫音標:
                self.音標 = 音標
        except AttributeError:
            pass

    def 預設音標(self):
        return self.音標

    def 音值(self):
        if self.音標 is None:
            return []
        音素陣列 = self.拆音節檢查.findall(
            self.音標
            .lower()
            .replace('iy', 'y')
            .replace('ow', 'w')
        )
        if 音素陣列[0] in self.元音:
            音素陣列 = ['-'] + 音素陣列
        是音節上尾一个 = []
        有元音矣 = False
        for 音素 in 音素陣列[::-1]:
            if 音素 == '-':  # 分音節符號
                是音節上尾一个.append(True)
                有元音矣 = False
            elif 音素 in self.輔音:  # 是輔音
                if 有元音矣:  # onset
                    是音節上尾一个.append(True)
                    有元音矣 = False
                else:  # coda
                    是音節上尾一个.append(False)
            else:  # 是元音
                是音節上尾一个.append(False)
                有元音矣 = True
        結果 = [[]]
        for 音素, 音節上尾一个 in zip(音素陣列, 是音節上尾一个[::-1]):
            if 音節上尾一个:
                結果.append([])
            結果[-1].append(self.國際音標對照表[音素])
        if 結果[0] == []:
            return 結果[1:]
        return 結果
