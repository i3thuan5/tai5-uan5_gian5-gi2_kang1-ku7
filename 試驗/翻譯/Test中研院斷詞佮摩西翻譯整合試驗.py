# -*- coding: utf-8 -*-
import os
from shutil import rmtree
from time import sleep
from unittest.case import TestCase


from 臺灣言語工具.翻譯.摩西工具.摩西翻譯模型訓練 import 摩西翻譯模型訓練
from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器
from 臺灣言語工具.翻譯.摩西工具.摩西服務端 import 摩西服務端
from 臺灣言語工具.翻譯.摩西工具.摩西用戶端 import 摩西用戶端
from 臺灣言語工具.斷詞.中研院.斷詞用戶端 import 斷詞用戶端
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from os.path import isdir


class 中研院斷詞佮摩西翻譯整合試驗(TestCase):

    def setUp(self):
        self.這馬目錄 = os.path.dirname(os.path.abspath(__file__))
        資料目錄 = os.path.join(self.這馬目錄, '翻譯語料')
        self.平行華語 = [os.path.join(資料目錄, '華'), ]
        self.平行閩南語 = [os.path.join(資料目錄, '閩'), ]
        self.閩南語語料 = [os.path.join(資料目錄, '閩'), ]
        self.愛停的服務 = []

    def tearDown(self):
        # 刣掉訓練出來的模型
        暫存資料夾 = os.path.join(self.這馬目錄, '暫存資料夾')
        if isdir(暫存資料夾):
            rmtree(暫存資料夾)
        for 服務 in self.愛停的服務:
            服務.停()

    def test_單一模型訓練(self):
        翻譯編碼器 = 語句編碼器()  # 若用著Unicode擴充就需要

        moses模型資料夾路徑 = os.path.join(self.這馬目錄, '暫存資料夾', '翻譯模型')
        模型訓練 = 摩西翻譯模型訓練()
        模型訓練.訓練(
            self.平行華語, self.平行閩南語, self.閩南語語料,
            moses模型資料夾路徑,
            連紲詞長度=2,
            編碼器=翻譯編碼器,
            刣掉暫存檔=False,
        )

        服務 = 摩西服務端(moses模型資料夾路徑, 埠=8500)
        服務.走()
        self.愛停的服務 = [服務]

        sleep(1)

        self.assertIsNone(服務.狀態())

        分析器 = 拆文分析器()
        華語章物件 = 分析器.分詞句物件('屏東 潮州 有人 把水果紙箱  套在 身上 。')

        斷詞用戶 = 斷詞用戶端()
        華語斷詞章物件 = 斷詞用戶.斷詞(華語章物件)

        摩西用戶 = 摩西用戶端(埠=8500, 編碼器=翻譯編碼器)
        閩南語章物件, 翻譯結構華語章物件, 分數 = 摩西用戶.翻譯分析(華語斷詞章物件)

        譀鏡 = 物件譀鏡()
        self.assertIn('Pin5-tong', 譀鏡.看分詞(閩南語章物件))
        self.assertIn('套', 譀鏡.看分詞(閩南語章物件))
        self.assertIn('水-果', 譀鏡.看分詞(閩南語章物件))
        self.assertIn('套 在', 譀鏡.看分詞(翻譯結構華語章物件))
        self.assertLess(分數, 0)

        # 予「self.愛停的服務」佇tearDown處理
        # 服務.停()
