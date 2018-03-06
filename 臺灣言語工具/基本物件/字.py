# -*- coding: utf-8 -*-
from 臺灣言語工具.基本物件.公用變數 import 無音
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.基本物件.公用變數 import 標點符號
from 臺灣言語工具.基本物件.公用變數 import 分字符號
from 臺灣言語工具.基本物件.公用變數 import 分詞符號
from 臺灣言語工具.基本物件.公用變數 import 分型音符號
from 臺灣言語工具.基本物件.功能 import 功能


class 字(功能):

    def __init__(self, 型, 音=無音, 輕聲標記=False):
        if 型 == '':
            raise 解析錯誤('傳入來的型是空的！')
        try:
            型是標點 = (型 in 標點符號)
        except TypeError:
            raise 型態錯誤('型音一定愛是string抑是tuple！「{}」佮「{}」'.format(型, 音))
        try:
            音.__iter__
        except AttributeError:
            raise 型態錯誤('音一定愛是iterative！「{}」佮「{}」'.format(型, 音))
        try:
            音是標點 = (音 in 標點符號)
        except TypeError:
            pass
        else:
            if (
                not isinstance(型, tuple) and
                音 not in [無音, (None,)] and
                (型是標點 ^ 音是標點)
            ):
                raise 解析錯誤('型佮音干焦一个是標點符號！「{}」佮「{}」'.format(型, 音))
        self.型 = 型
        self.音 = 音
        self.輕聲標記 = 輕聲標記

    def 有音(self):
        return self.音 != 無音 and self.音 not in 標點符號

    def __eq__(self, 別个):
        return isinstance(別个, 字) and self.型 == 別个.型 and self.音 == 別个.音

    def __hash__(self):
        return hash((self.型, self.音))

    def __str__(self):
        return '字：{0} {1}'.format(self.型, self.音)

    def __repr__(self):
        return self.__str__()

    def 看型(self, 物件分字符號='', 物件分詞符號='', 物件分句符號=''):
        return self.型

    def 看音(self, 物件分字符號=分字符號, 物件分詞符號=分詞符號, 物件分句符號=分詞符號):
        return self.音

    def 看分詞(self, 物件分型音符號=分型音符號,
            物件分字符號=分字符號, 物件分詞符號=分詞符號, 物件分句符號=分詞符號):
        if self.音 == 無音:
            return self.看型(物件分字符號, 物件分詞符號)
        return (
            self.看型(物件分字符號, 物件分詞符號) +
            物件分型音符號 +
            self.看音(物件分字符號, 物件分詞符號)
        )

    def 敢有輕聲標記(self):
        return self.輕聲標記 or self.音.startswith('0')

    def 綜合標音(self, 語言綜合標音):
        return 語言綜合標音(self).轉json格式()

    def 篩出字物件(self):
        return [self]

    def 網出詞物件(self):
        raise 解析錯誤('字物件無法度網出詞物件！！')

    def 轉音(self, 音標工具, 函式='預設音標'):
        # 逐个函式攏愛產生新的物件
        if self.音 != 無音:
            新音物件 = 音標工具(self.音)
            新音 = getattr(新音物件, 函式)()
            if 新音 is None:
                if self.型 in 標點符號 and self.音 in 標點符號:
                    新音 = self.音
                else:
                    新音 = self.音
        else:
            新音 = 無音
        新型物件 = 音標工具(self.型)
        新型預設音標 = getattr(新型物件, 函式)()
        if self.音.startswith(self.型) and isinstance(新音, str):
            新型 = 新音
        elif (
            新型物件 is not None and 新型預設音標 is not None and
            isinstance(新型預設音標, str)
        ):
            新型 = 新型預設音標
        else:
            新型 = self.型
        return 字(新型, 新音)

    def 音標敢著(self, 音標工具):
        if self.型 in 標點符號 and self.音 in 標點符號:
            return True
        if self.音 == 無音:
            return True
        新音物件 = 音標工具(self.音)
        if 新音物件.音標 is None:
            return False
        return True
