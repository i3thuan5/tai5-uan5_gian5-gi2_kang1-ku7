# -*- coding: utf-8 -*-
import os
from os.path import isdir
from shutil import rmtree
from time import sleep
from unittest.case import TestCase
from unittest.mock import patch


from 臺灣言語工具.翻譯.摩西工具.摩西翻譯模型訓練 import 摩西翻譯模型訓練
from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器
from 臺灣言語工具.翻譯.摩西工具.斷詞轉斷字的編碼器 import 斷詞轉斷字編碼器
from 臺灣言語工具.翻譯.摩西工具.摩西服務端 import 摩西服務端
from 臺灣言語工具.翻譯.摩西工具.摩西用戶端 import 摩西用戶端
from 臺灣言語工具.翻譯.斷詞斷字翻譯 import 斷詞斷字翻譯
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.翻譯.摩西工具.安裝摩西翻譯佮相關程式 import 安裝摩西翻譯佮相關程式


class 摩西模型訓練佮翻譯整合試驗(TestCase):
    @classmethod
    def setUpClass(cls):
        安裝摩西翻譯佮相關程式.安裝gizapp()
        安裝摩西翻譯佮相關程式.安裝mgiza()  # 愛libboost
        安裝摩西翻譯佮相關程式.安裝moses(編譯CPU數=4)

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

        摩西用戶 = 摩西用戶端(埠=8500, 編碼器=翻譯編碼器)
        閩南語章物件, 翻譯結構華語章物件, 分數 = 摩西用戶.翻譯分析(華語章物件)

        譀鏡 = 物件譀鏡()
        self.assertIn('Pin5-tong', 譀鏡.看分詞(閩南語章物件))
        self.assertIn('套', 譀鏡.看分詞(閩南語章物件))
        self.assertIn('水-果', 譀鏡.看分詞(閩南語章物件))
        self.assertIn('套-在', 譀鏡.看分詞(翻譯結構華語章物件))
        self.assertLess(分數, 0)

        # 予「self.愛停的服務」佇tearDown處理
        # 服務.停()

    def test_訓練摩西斷詞佮斷字模型(self):
        翻譯編碼器 = 語句編碼器()  # 若用著Unicdoe擴充就需要

        模型訓練 = 摩西翻譯模型訓練()
        這馬資料夾 = os.path.dirname(os.path.abspath(__file__))
        斷詞暫存資料夾 = os.path.join(這馬資料夾, '暫存資料夾', '斷詞翻譯模型')
        模型訓練.訓練(
            self.平行華語, self.平行閩南語, self.閩南語語料,
            斷詞暫存資料夾,
            連紲詞長度=2,
            編碼器=翻譯編碼器,
            刣掉暫存檔=True,
        )

        斷詞編碼器 = 斷詞轉斷字編碼器()
        斷字暫存資料夾 = os.path.join(這馬資料夾, '暫存資料夾', '斷字翻譯模型')
        模型訓練.訓練(
            self.平行華語, self.平行閩南語, self.閩南語語料,
            斷字暫存資料夾,
            連紲詞長度=2,
            編碼器=斷詞編碼器(),
            刣掉暫存檔=True,
        )

        斷詞服務 = 摩西服務端(斷詞暫存資料夾, 埠=8501)
        斷字服務 = 摩西服務端(斷字暫存資料夾, 埠=8502)
        斷詞服務.走()
        斷字服務.走()
        self.愛停的服務 = [斷詞服務, 斷字服務]

        sleep(1)

        self.assertIsNone(斷詞服務.狀態())
        self.assertIsNone(斷字服務.狀態())

        分析器 = 拆文分析器()
        華語章物件 = 分析器.分詞句物件('屏東 潮州 有人 把麵包紙箱  套在 身上 。')

        翻譯工具 = 斷詞斷字翻譯(
            斷詞用戶端=摩西用戶端(埠=8501, 編碼器=翻譯編碼器),
            斷字用戶端=摩西用戶端(埠=8502, 編碼器=翻譯編碼器),
        )
        閩南語章物件, 翻譯結構華語章物件, 分數 = 翻譯工具.翻譯分析(華語章物件)

        譀鏡 = 物件譀鏡()
        self.assertIn('Pin5-tong', 譀鏡.看分詞(閩南語章物件))
        self.assertNotIn('套', 譀鏡.看分詞(閩南語章物件))
        self.assertIn('麵-包', 譀鏡.看分詞(閩南語章物件))
        self.assertIn('套 在', 譀鏡.看分詞(翻譯結構華語章物件))
        self.assertLess(分數, 0)

        # 予「self.愛停的服務」佇tearDown處理
        # 斷詞服務.停()
        # 斷字服務.停()

    def test_無完整的模型袂使用(self):
        模型訓練 = 摩西翻譯模型訓練()
        moses模型資料夾路徑 = os.path.join(self.這馬目錄, '暫存資料夾', '翻譯模型')
        模型訓練.訓練(
            self.平行華語, self.平行閩南語, self.閩南語語料,
            moses模型資料夾路徑,
            連紲詞長度=2,
            編碼器=語句編碼器(),
            刣掉暫存檔=True,
        )

        # 刣掉訓練部份模型
        os.remove(
            os.path.join(
                self.這馬目錄, '暫存資料夾', '翻譯模型', 'model', 'phrase-table.gz'
            )
        )

        服務 = 摩西服務端(moses模型資料夾路徑, 埠=8503)
        服務.走()

        sleep(1)

        self.assertIsNotNone(服務.狀態())

    def test_服務端會使等(self,):
        模型訓練 = 摩西翻譯模型訓練()
        moses模型資料夾路徑 = os.path.join(self.這馬目錄, '暫存資料夾', '翻譯模型')
        模型訓練.訓練(
            self.平行華語, self.平行閩南語, self.閩南語語料,
            moses模型資料夾路徑,
            連紲詞長度=2,
            編碼器=語句編碼器(),
            刣掉暫存檔=True,
        )

        服務 = 摩西服務端(moses模型資料夾路徑, 埠=8504)
        服務.走()

        等待patch = patch('subprocess.Popen.wait')
        等待mock = 等待patch.start()
        服務.等()
        等待mock.assert_called_once_with()
        等待patch.stop()

        服務.停()
