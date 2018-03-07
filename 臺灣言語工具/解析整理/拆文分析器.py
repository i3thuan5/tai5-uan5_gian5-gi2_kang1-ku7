# -*- coding: utf-8 -*-
from 臺灣言語工具.基本物件.公用變數 import 分字符號
from 臺灣言語工具.基本物件.公用變數 import 分詞符號
from 臺灣言語工具.基本物件.字 import 字
from 臺灣言語工具.基本物件.詞 import 詞
from 臺灣言語工具.基本物件.組 import 組
from 臺灣言語工具.基本物件.集 import 集
from 臺灣言語工具.基本物件.句 import 句
from 臺灣言語工具.基本物件.章 import 章
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.基本物件.公用變數 import 無音
from 臺灣言語工具.基本物件.公用變數 import 組字式符號
from 臺灣言語工具.基本物件.公用變數 import 斷句標點符號
from 臺灣言語工具.基本物件.公用變數 import 標點符號
from itertools import chain
import re
import unicodedata


from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.基本物件.公用變數 import 分型音符號
from 臺灣言語工具.解析整理.程式掠漏 import 程式掠漏
from 臺灣言語工具.基本物件.公用變數 import 統一碼羅馬字類
from 臺灣言語工具.基本物件.公用變數 import 統一碼聲調符號
from 臺灣言語工具.基本物件.公用變數 import 統一碼注音聲調符號
from 臺灣言語工具.基本物件.公用變數 import 敢是拼音字元
from 臺灣言語工具.基本物件.公用變數 import 敢是注音符號
from 臺灣言語工具.基本物件.公用變數 import 統一碼數字類


class 拆文分析器:
    _切組物件分詞 = re.compile('(([^ ｜]*.｜.[^ ｜]*) ?|[^ ]+)')
    _切章分詞 = re.compile('(\n｜.|.｜\n|\n)', re.DOTALL)
    _是空白 = re.compile('[ \t]+')
    _是分字符號 = re.compile('{}+'.format(分字符號))

    @classmethod
    def 建立字物件(cls, 語句, 別種書寫=無音):
        return 字(語句, 別種書寫)

    @classmethod
    def 建立詞物件(cls, 語句, 別種書寫=None):
        if 別種書寫 is None:
            return cls._物件的音攏提掉(cls.對齊詞物件(語句, 語句))
        return cls.對齊詞物件(語句, 別種書寫)

    @classmethod
    def 建立組物件(cls, 語句, 別種書寫=None):
        if 別種書寫 is None:
            return cls._物件的音攏提掉(cls.對齊組物件(語句, 語句))
        return cls.對齊組物件(語句, 別種書寫)

    @classmethod
    def 建立集物件(cls, 語句, 別種書寫=None):
        if 別種書寫 is None:
            return cls._物件的音攏提掉(cls.對齊集物件(語句, 語句))
        return cls.對齊集物件(語句, 別種書寫)

    @classmethod
    def 建立句物件(cls, 語句, 別種書寫=None):
        if 別種書寫 is None:
            return cls._物件的音攏提掉(cls.對齊句物件(語句, 語句))
        return cls.對齊句物件(語句, 別種書寫)

    @classmethod
    def 建立章物件(cls, 語句, 別種書寫=None):
        if 別種書寫 is None:
            return cls._物件的音攏提掉(cls.對齊章物件(語句, 語句))
        return cls.對齊章物件(語句, 別種書寫)

    @classmethod
    def 對齊字物件(cls, 型, 音):
        return 字(型, 音)

    @classmethod
    def 對齊詞物件(cls, 型, 音):
        組物件 = cls.對齊組物件(型, 音)
        if len(組物件.內底詞) == 0:
            return 詞()
        if len(組物件.內底詞) > 1:
            raise 解析錯誤('「{0}」、「{1}」超過一e5詞'.format(型, 音))
        return 組物件.內底詞[0]

    # 斷詞會照音來斷，型的連字符攏無算
    @classmethod
    def 對齊組物件(cls, 型, 音):
        if not isinstance(型, str):
            raise 型態錯誤('傳入來的型毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if not isinstance(音, str):
            raise 型態錯誤('傳入來的音毋是字串：型＝{0}，音＝{1}'.format(str(型), str(音)))
        if 型 == '' and 音 == 無音:
            return 組()

        全部型陣列 = cls._拆句做字(型.strip(分詞符號))
        全部音陣列, 巢狀輕聲陣列 = cls._拆句做巢狀詞(音)
        組物件 = 組()
        try:
            組物件.內底詞 = cls._對齊型音處理刪節號(全部型陣列, 全部音陣列, 巢狀輕聲陣列)
        except 解析錯誤 as 錯誤:
            raise 解析錯誤(錯誤.args[0].format(型, 音))
        return 組物件

    @classmethod
    def 對齊集物件(cls, 型, 音):
        if 型 == '' and 音 == 無音:
            return 集()
        集物件 = 集()
        集物件.內底組 = [cls.對齊組物件(型, 音)]
        return 集物件

    @classmethod
    def 對齊句物件(cls, 型, 音):
        if 型 == '' and 音 == 無音:
            return 句()
        句物件 = 句()
        句物件.內底集 = [cls.對齊集物件(型, 音)]
        return 句物件

    @classmethod
    def 對齊章物件(cls, 型, 音):
        if 型 == '' and 音 == 無音:
            return 章()

        斷句詞陣列 = cls._詞陣列分一句一句(cls.對齊句物件(型, 音).網出詞物件())
        return cls._斷句詞陣列轉章物件(斷句詞陣列)

    @classmethod
    def _拆句做字(cls, 語句):
        return cls._句分析(語句)[0]

    @classmethod
    def _拆句做巢狀詞(cls, 語句):
        字陣列, 輕聲陣列, 佮後一个字無仝一个詞 = cls._句分析(語句)
        巢狀詞陣列 = []
        巢狀輕聲陣列 = []
        位置 = 0
        while 位置 < len(字陣列):
            範圍 = 位置
            while 範圍 < len(佮後一个字無仝一个詞) and not 佮後一个字無仝一个詞[範圍]:
                範圍 += 1
            範圍 += 1
            巢狀詞陣列.append(字陣列[位置:範圍])
            巢狀輕聲陣列.append(輕聲陣列[位置:範圍])
            位置 = 範圍
        return 巢狀詞陣列, 巢狀輕聲陣列

    class _分析狀態:
        def __init__(self):
            self._字陣列 = []
            self._輕聲陣列 = []
            self._佮後一个字無仝一个詞 = []
            self.變一般模式()
            # 組字式抑是數羅會超過一个字元
            self._這馬字 = ''
            self._這馬是輕聲字 = False

        def 分析結果(self):
            return self._字陣列, self._輕聲陣列, self._佮後一个字無仝一个詞

        def 敢有分析資料矣(self):
            return len(self._字陣列) > 0 or self.這馬字敢閣有物件()

        def 這馬字敢閣有物件(self):
            return self._這馬字 != ''

        def 這馬字敢全部攏數字(self):
            return self._這馬字.isdigit()

        def 變一般模式(self):
            self._模式 = '一般'
            self._組字長度 = 0

        def 變組字模式(self):
            self._模式 = '組字'
            self._組字長度 = -1

        def 是一般模式(self):
            return self._模式 == '一般'

        def 是組字模式(self):
            return self._模式 == '組字'

        def 組字模型加一个字元(self, 字):
            if 字 in 組字式符號:
                self._組字長度 -= 1
            else:
                self._組字長度 += 1

        def 組字長度有夠矣未(self):
            return self._組字長度 == 1

        def 這馬字加一个字元(self, 字):
            self._這馬字 += 字

        def 這馬是輕聲字(self):
            self._這馬是輕聲字 = True

        def 字陣列直接加一字(self, 字):
            self._字陣列.append(字)
            self._輕聲陣列.append(False)
            self._佮後一个字無仝一个詞.append(None)

        def 這馬字好矣清掉囥入去字陣列(self):
            if self._這馬字 != '':
                self._字陣列.append(self._這馬字)
                self._輕聲陣列.append(self._這馬是輕聲字)
                self._佮後一个字無仝一个詞.append(None)
                self._這馬字 = ''
                self._這馬是輕聲字 = False

        def 頂一字佮這馬的字仝詞(self):
            try:
                self._佮後一个字無仝一个詞[-1] = False
            except IndexError:
                pass

        def 頂一字佮這馬的字無仝詞(self):
            try:
                if self._佮後一个字無仝一个詞[-1] is None:
                    self._佮後一个字無仝一个詞[-1] = True
            except IndexError:
                pass

        def 上尾敢是o結尾(self):
            return 文章粗胚._o結尾(self._這馬字)

    @classmethod
    def _句分析(cls, 語句):
        狀態 = cls._分析狀態()
        if 語句 == 分詞符號 or cls._是空白.fullmatch(語句):
            return 狀態.分析結果()
        頂一个字 = None
        頂一个字種類 = None
        頂一个是連字符 = False
        頂一个是空白 = False
        頂一个是輕聲符號 = False
        頂一个是注音符號 = False
        位置 = 0
        while 位置 < len(語句):
            字 = 語句[位置]
            字種類 = unicodedata.category(字)
            是連字符 = False
            是空白 = False
            是輕聲符號 = False
            是注音符號 = 敢是注音符號(字)
            if 狀態.是組字模式():
                狀態.這馬字加一个字元(字)
                狀態.組字模型加一个字元(字)
                if 狀態.組字長度有夠矣未():
                    狀態.這馬字好矣清掉囥入去字陣列()
                    狀態.變一般模式()
            elif 狀態.是一般模式():
                揣分字 = cls._是分字符號.match(語句[位置:])
                if 揣分字:
                    分字長度 = len(揣分字.group(0))
                    if 分字長度 == 1:
                        狀態.這馬字好矣清掉囥入去字陣列()
                        if (
                            (位置 == 0 or 頂一个是空白) and
                            (位置 + 1 == len(語句) or 語句[位置 + 1] == 分詞符號)
                        ):
                            狀態.字陣列直接加一字(分字符號)
                            狀態.頂一字佮這馬的字無仝詞()
                        else:
                            if not 狀態.敢有分析資料矣():
                                if len(語句) > 1:
                                    raise 解析錯誤(
                                        '連字符「-」佇句頭無接字！！語句：「{0}」'.format(語句)
                                    )
                                else:
                                    狀態.字陣列直接加一字(字)
                                    狀態.頂一字佮這馬的字無仝詞()
                            else:
                                if 頂一个是空白:
                                    raise 解析錯誤(
                                        '連字符「-」頭前閬一格無接字！！語句：「{0}」'.format(語句)
                                    )
                                狀態.頂一字佮這馬的字仝詞()
                            是連字符 = True
                    elif 分字長度 == 2:
                        狀態.這馬字好矣清掉囥入去字陣列()
                        是輕聲符號 = True
                        位置 += 1
                    else:
                        raise 解析錯誤(
                            '連字符「{1}」分析器毋知愛按怎處理。語句：「{0}」'.format(
                                語句, 揣分字.group(0)
                            )
                        )
                elif 字 == 分詞符號 or cls._是空白.fullmatch(字):
                    if 頂一个是連字符:
                        raise 解析錯誤('連字符「-」後壁閬一格無接字！！語句：「{0}」'.format(語句))
                    if 頂一个是輕聲符號:
                        raise 解析錯誤('輕聲符號「--」後壁閬一格無接字！！語句：「{0}」'.format(語句))
                    狀態.這馬字好矣清掉囥入去字陣列()
                    狀態.頂一字佮這馬的字無仝詞()
                    是空白 = True
                # 羅馬字接做伙
                elif 敢是拼音字元(字, 字種類):
                    # 頭前是羅馬字抑是輕聲、外來語的數字
                    # 「N1N1」、「g0v」濫做伙名詞，「sui2sui2」愛變做兩个字，予粗胚處理。
                    if not 敢是拼音字元(頂一个字, 頂一个字種類)\
                            and 頂一个字種類 not in 統一碼數字類:
                        # 頭前愛清掉
                        狀態.這馬字好矣清掉囥入去字陣列()
                    if 頂一个是輕聲符號:
                        狀態.這馬是輕聲字()
                    狀態.這馬字加一个字元(字)
                # 數字
                elif 字種類 in 統一碼數字類:
                    if (
                        頂一个字種類 not in 統一碼數字類 and
                        not 敢是拼音字元(頂一个字, 頂一个字種類) and
                        not 頂一个是注音符號
                    ):
                        狀態.這馬字好矣清掉囥入去字陣列()
                        狀態.頂一字佮這馬的字無仝詞()
                    狀態.這馬字加一个字元(字)
                # 音標後壁可能有聲調符號
                elif 字種類 in 統一碼聲調符號 and 頂一个字種類 in 統一碼羅馬字類:
                    狀態.這馬字加一个字元(字)
                # 處理注音，輕聲、注音、空三个後壁會當接注音
                elif 是注音符號:
                    if (
                        頂一个字種類 not in 統一碼注音聲調符號 and
                        not 頂一个是注音符號
                    ):
                        狀態.這馬字好矣清掉囥入去字陣列()
                    狀態.這馬字加一个字元(字)
                # 注音後壁會當接聲調
                elif 字種類 in 統一碼注音聲調符號 and 頂一个是注音符號:
                    狀態.這馬字加一个字元(字)

                elif 字 in 標點符號:
                    if 字 == '•' and 狀態.上尾敢是o結尾():
                        狀態.這馬字加一个字元(字)
                    else:
                        狀態.這馬字好矣清掉囥入去字陣列()
                        狀態.頂一字佮這馬的字無仝詞()
                        狀態.字陣列直接加一字(字)
                        狀態.頂一字佮這馬的字無仝詞()
                else:
                    if 狀態.這馬字敢全部攏數字():
                        狀態.這馬字好矣清掉囥入去字陣列()
                        狀態.頂一字佮這馬的字無仝詞()
                    else:
                        狀態.這馬字好矣清掉囥入去字陣列()
                    if 頂一个是輕聲符號:
                        狀態.這馬是輕聲字()
                    狀態.這馬字加一个字元(字)
                    if 字 in 組字式符號:
                        狀態.變組字模式()
                    else:
                        狀態.這馬字好矣清掉囥入去字陣列()
            位置 += 1
            頂一个字 = 字
            頂一个是連字符 = 是連字符
            頂一个是空白 = 是空白
            頂一个是輕聲符號 = 是輕聲符號
            頂一个字種類 = 字種類
            頂一个是注音符號 = 是注音符號
        if 狀態.這馬字敢閣有物件():
            if 狀態.是一般模式():
                狀態.這馬字好矣清掉囥入去字陣列()
            else:
                raise 解析錯誤('語句組字式無完整，語句＝{0}'.format(str(語句)))
        if 頂一个是連字符:
            raise 解析錯誤('連字符「-」佇句尾無接字！！')
        if 頂一个是輕聲符號:
            raise 解析錯誤('輕聲符號「--」佇句尾無接字！！')
        return 狀態.分析結果()

    @classmethod
    def 分詞字物件(cls, 分詞):
        程式掠漏.毋是字串都毋著(分詞)
        切開結果 = 分詞.split(分型音符號)
        if len(切開結果) == 2:
            return cls.對齊字物件(*切開結果)
        if len(切開結果) == 1:
            return cls.建立字物件(*切開結果)
        raise 解析錯誤('毋是拄仔好有一个抑是兩个部份：{0}'.format(分詞))

    @classmethod
    def 分詞詞物件(cls, 分詞):
        程式掠漏.毋是字串都毋著(分詞)
        if 分詞 == '':
            return cls.建立詞物件(分詞)
        切開結果 = 分詞.split(分型音符號)
        if len(切開結果) == 2:
            型, 音 = 切開結果
            if 型 == '':
                raise 解析錯誤('型是空的：{0}'.format(分詞))
            if len(型) == 1 and len(音) == 1:
                return 詞([cls.對齊字物件(型, 音)])
            型陣列 = 型.split(分字符號)
            音陣列 = 音.split(分字符號)
            if len(型陣列) > 1 and len(型陣列) == len(音陣列):
                return cls._拆好陣列對齊詞物件(型陣列, 音陣列, [False] * len(音陣列))
            return cls.對齊詞物件(型, 音)
        if len(切開結果) == 1:
            return cls.建立詞物件(分詞)
        if 切開結果 == [''] * 4:
            return cls.對齊詞物件(分型音符號, 分型音符號)
        if len(切開結果) == 3:
            if 切開結果[:2] == [''] * 2:
                return cls.對齊詞物件(分型音符號, 切開結果[2])
            if 切開結果[-2:] == [''] * 2:
                return cls.對齊詞物件(切開結果[0], 分型音符號)
        raise 解析錯誤('毋是拄仔好有一个抑是兩个部份：{0}'.format(分詞))

    @classmethod
    def 分詞組物件(cls, 分詞):
        程式掠漏.毋是字串都毋著(分詞)
        if 分詞 == '':
            return 組()
        組物件 = cls.建立組物件('')
        切開 = cls._切組物件分詞.split(分詞)
        for 分, 細 in zip(切開[1::3], 切開[2::3]):
            if 細 is not None:
                組物件.內底詞.append(cls.分詞詞物件(細))
            else:
                組物件.內底詞.append(cls.分詞詞物件(分))
        return 組物件

    @classmethod
    def 分詞集物件(cls, 分詞):
        if 分詞 == '':
            return 集()
        集物件 = cls.建立集物件('')
        集物件.內底組.append(cls.分詞組物件(分詞))
        return 集物件

    @classmethod
    def 分詞句物件(cls, 分詞):
        if 分詞 == '':
            return 句()
        句物件 = cls.建立句物件('')
        句物件.內底集.append(cls.分詞集物件(分詞))
        return 句物件

    @classmethod
    def 分詞章物件(cls, 分詞):
        if 分詞 == '':
            return 章()
        斷出來的詞陣列 = []
        try:
            for 第幾个, 句分詞 in enumerate(cls._切章分詞.split(分詞)):
                if 第幾个 % 2 == 0:
                    斷出來的詞陣列.append(
                        cls.分詞句物件(句分詞).網出詞物件()
                    )
                else:
                    斷出來的詞陣列.append(
                        cls.分詞詞物件(句分詞).網出詞物件()
                    )
        except TypeError:
            raise 型態錯誤('分詞型態有問題，分詞：{}'.format(分詞))
        斷句詞陣列 = cls._詞陣列分一句一句(list(chain(*斷出來的詞陣列)))
        return cls._斷句詞陣列轉章物件(斷句詞陣列)

    @classmethod
    def _詞陣列分一句一句(cls, 詞陣列):
        有一般字無 = False
        愛換的所在 = []
        for 詞物件 in 詞陣列[::-1]:
            是斷句, 是換逝 = cls._詞物件敢是斷句符號抑是換逝(詞物件)
            if (有一般字無 and 是斷句) or 是換逝:
                愛換的所在.append(True)
                有一般字無 = False
            else:
                愛換的所在.append(False)
                if not 是斷句:
                    有一般字無 = True
        愛換的所在 = 愛換的所在[::-1]
        斷句詞陣列 = []
        頭前 = 0
        for 第幾字 in range(len(詞陣列)):
            if 愛換的所在[第幾字]:
                斷句詞陣列.append(詞陣列[頭前:第幾字 + 1])
                頭前 = 第幾字 + 1
        if 頭前 < len(詞陣列):
            斷句詞陣列.append(詞陣列[頭前:])
        return 斷句詞陣列

    @classmethod
    def _斷句詞陣列轉章物件(cls, 斷句詞陣列):
        章物件 = 章()
        for 詞陣列 in 斷句詞陣列:
            組物件 = 組()
            組物件.內底詞 = 詞陣列
            集物件 = 集()
            集物件.內底組 = [組物件]
            句物件 = 句()
            句物件.內底集 = [集物件]
            章物件.內底句.append(句物件)
        return 章物件

    @classmethod
    def _詞物件敢是斷句符號抑是換逝(cls, 詞物件):
        if len(詞物件.內底字) == 1:
            字物件 = 詞物件.內底字[0]
            if 字物件.型 == '\n' or 字物件.音 == '\n':
                return False, True
            if 字物件.型 in 斷句標點符號 and\
                    (字物件.音 == 無音 or 字物件.音 in 斷句標點符號):
                return True, False
        return False, False

    @classmethod
    def _拆好陣列對齊詞物件(cls, 型陣列, 音陣列, 輕聲陣列):
        if len(型陣列) < len(音陣列):
            raise 解析錯誤('詞內底的型「{0}」比音「{1}」少！{2}：{3}'.format(
                str(型陣列), str(音陣列), len(型陣列), len(音陣列)))
        if len(型陣列) > len(音陣列):
            raise 解析錯誤('詞內底的型「{0}」比音「{1}」濟！{2}：{3}'.format(
                str(型陣列), str(音陣列), len(型陣列), len(音陣列)))
        if 型陣列 == [] and 音陣列 == []:
            return 詞()
        長度 = len(型陣列)
        詞物件 = 詞()
        字陣列 = 詞物件.內底字
        for 位置 in range(長度):
            字陣列.append(字(型陣列[位置], 音陣列[位置], 輕聲陣列[位置]))
        return 詞物件

    @classmethod
    def _對齊型音處理刪節號(cls, 全部型陣列, 全部音陣列, 巢狀輕聲陣列):
        詞陣列 = []
        第幾字 = 0
        第幾音 = 0
        while 第幾音 < len(全部音陣列):
            if (
                全部型陣列[第幾字:第幾字 + 2] == ['…', '…'] and
                全部音陣列[第幾音:第幾音 + 3] == [['.'], ['.'], ['.']]
            ):
                詞陣列.append(
                    cls._拆好陣列對齊詞物件(['……'], ['...'], [False])
                )
                第幾字 += 2
                第幾音 += 3
            elif (
                全部型陣列[第幾字:第幾字 + 2] == ['…', '…'] and
                全部音陣列[第幾音:第幾音 + 2] == [['…'], ['…']]
            ):
                詞陣列.append(
                    cls._拆好陣列對齊詞物件(['……'], ['……'], [False])
                )
                第幾字 += 2
                第幾音 += 2
            elif (
                全部型陣列[第幾字:第幾字 + 3] == ['.', '.', '.'] and
                全部音陣列[第幾音:第幾音 + 3] == [['.'], ['.'], ['.']]
            ):
                詞陣列.append(
                    cls._拆好陣列對齊詞物件(['...'], ['...'], [False])
                )
                第幾字 += 3
                第幾音 += 3
            else:
                音詞 = 全部音陣列[第幾音]
                輕聲 = 巢狀輕聲陣列[第幾音]
                if 第幾字 + len(音詞) > len(全部型陣列):
                    raise 解析錯誤(
                        '詞組內底的型「{{}}」比音「{{}}」少！配對結果：{}'.format(str(詞陣列))
                    )
                詞陣列.append(
                    cls._拆好陣列對齊詞物件(全部型陣列[第幾字:第幾字 + len(音詞)], 音詞, 輕聲)
                )
                第幾字 += len(音詞)
                第幾音 += 1
        if 第幾字 < len(全部型陣列):
            raise 解析錯誤('詞組內底的型「{{}}」比音「{{}}」濟！配對結果：{}'.format(str(詞陣列)))
        return 詞陣列

    @classmethod
    def _物件的音攏提掉(cls, 對齊物件):
        for 字物件 in 對齊物件.篩出字物件():
            字物件.音 = 無音
        return 對齊物件
