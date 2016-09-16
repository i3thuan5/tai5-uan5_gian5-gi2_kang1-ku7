# -*- coding: utf-8 -*-
from 臺灣言語工具.音標系統.客話.臺灣客家話拼音轉音值模組 import 臺灣客家話拼音轉音值模組
臺灣客家話拼音聲母對照表 = {
    'b', 'p', 'm', 'f', 'v', 'd', 't', 'n', 'l', 'g',
    'k', 'ng', 'h', 'j', 'q', 'x', 'z', 'c', 's',
    'zh', 'ch', 'sh', 'rh', '', 'bb', 'r'
                # 'ngi','zi', 'ci', 'si',
}
臺灣客家話拼音韻母對照表 = {
    'ii', 'i', 'e', 'a', 'o', 'u', 'ie', 'eu', 'ieu', 'ia',
    'ua', 'ai', 'iai', 'uai', 'au', 'iau', 'io', 'oi', 'ioi', 'iu',
                'ui', 'iui', 'ue', 'iim', 'im', 'em', 'iem', 'am', 'iam',
                'iin', 'in', 'en', 'ien', 'uen', 'an', 'ian', 'uan', 'on', 'ion',
                'un', 'iun', 'ang', 'iang', 'uang', 'ong', 'iong', 'ung',
                'iung', 'iib', 'ib', 'eb', 'ieb', 'ab', 'iab', 'iid', 'id',
                'ed', 'ied', 'ued', 'ad', 'iad', 'uad', 'od', 'iod', 'ud', 'iud',
                'ag', 'iag', 'uag', 'og', 'iog', 'ug', 'iug', 'er',
                'm', 'n', 'ng',
                'oo', 'ee', 'eeb', 'eed', 'eem', 'een', 'eeu',
                'ainn', 'ann', 'iann', 'inn', 'onn', 'uainn',
}
臺灣客家話拼音調類對照表 = {
    '', 'ˊ', 'ˋ', 'ˇ', '+', '^'
}

#########################################
#  2013/11/1
#  意傳的客家話辨識用拼音
#########################################


class 臺灣客家話拼音:
    # -------成員函式-------- #

    def __init__(self, 音標):
        # self.腔
        self.音標 = None
        音標 = 音標.lower()
        if 音標[-1:] in self.調類對照表:
            for 所在 in range(len(音標) - 1):
                if 音標[:所在] in self.聲母對照表 and 音標[所在:-1] in self.韻母對照表:
                    self.聲 = 音標[:所在]
                    self.韻 = 音標[所在:-1]
                    self.調 = 音標[-1:]
                    # 檢查入聲字的調是否正確（只允許1和4聲）
                    if (self.韻.endswith('g') and not self.韻.endswith('ng')) or\
                            self.韻.endswith('d') or\
                            self.韻.endswith('b'):
                        # if(wrong)continue;
                        if(self.調 == '^' or self.調 == '+'):
                            continue

                    self.聲韻 = 音標[:-1]
                    self.音標 = 音標
                    # special case
        else:  # :調是1聲
            for 所在 in range(len(音標)):
                if 音標[:所在] in self.聲母對照表 and 音標[所在:] in self.韻母對照表:
                    self.聲 = 音標[:所在]
                    self.韻 = 音標[所在:]
                    self.調 = ''
                    self.聲韻 = 音標
                    self.音標 = 音標
                    # special case

    def 預設音標(self):
        return self.音標

    def 音值(self):
        if self.音標 is None:
            return self.轉音值模組.轉(None, None, None)
        return self.轉音值模組.轉(self.聲, self.韻, self.調)

    def 通用音值(self):
        return (self.聲, self.韻, self.調)
    # -------成員變數-------- #
    # ng uainn ˊ
    音標上長長度 = 8
    聲 = None
    韻 = None
    聲韻 = None
    調 = None
    音標 = None
    聲母對照表 = 臺灣客家話拼音聲母對照表
    韻母對照表 = 臺灣客家話拼音韻母對照表
    調類對照表 = 臺灣客家話拼音調類對照表
    轉音值模組 = 臺灣客家話拼音轉音值模組()
