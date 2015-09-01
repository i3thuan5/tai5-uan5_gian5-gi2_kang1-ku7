# -*- coding: utf-8 -*-
import unittest

from 臺灣言語工具.基本元素.集 import 集
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


class 字物件篩仔單元試驗(unittest.TestCase):
    def setUp(self):
        self.分析器 = 拆文分析器()
        self.粗胚 = 文章粗胚()
        self.篩仔 = 字物件篩仔()

    def tearDown(self):
        pass

    def test_篩字(self):
        型 = '媠'
        字物件 = self.分析器.建立字物件(型)
        self.assertEqual(self.篩仔.篩出字物件(字物件), [字物件])

    def test_篩詞孤字(self):
        型 = '媠'
        字物件 = self.分析器.建立字物件(型)
        詞物件 = self.分析器.建立詞物件(型)
        self.assertEqual(self.篩仔.篩出字物件(詞物件), [字物件])

    def test_篩詞無字(self):
        型 = ''
        詞物件 = self.分析器.建立詞物件(型)
        self.assertEqual(self.篩仔.篩出字物件(詞物件), [])

    def test_篩詞濟字漢字(self):
        語句 = '椅仔！'
        self.assertEqual(
            self.篩仔.篩出字物件(self.分析器.建立詞物件(語句)),
            [self.分析器.建立字物件('椅'), self.分析器.建立字物件('仔'), self.分析器.建立字物件('！')])

    def test_篩詞濟字音標(self):
        語句 = 'tsit8-tiunn1 !'
        self.assertEqual(
            self.篩仔.篩出字物件(self.分析器.建立詞物件(語句)),
            [self.分析器.建立字物件('tsit8'), self.分析器.建立字物件('tiunn1'), self.分析器.建立字物件('!')])

    def test_篩詞濟字漢羅(self):
        語句 = 'tsit8-張!'
        self.assertEqual(
            self.篩仔.篩出字物件(self.分析器.建立詞物件(語句)),
            [self.分析器.建立字物件('tsit8'), self.分析器.建立字物件('張'), self.分析器.建立字物件('!')])

    def test_篩組孤字(self):
        型 = '媠'
        字物件 = self.分析器.建立字物件(型)
        組物件 = self.分析器.建立組物件(型)
        self.assertEqual(self.篩仔.篩出字物件(組物件), [字物件])

    def test_篩組無字(self):
        型 = ''
        組物件 = self.分析器.建立組物件(型)
        self.assertEqual(self.篩仔.篩出字物件(組物件), [])

    def 建立組檢查(self, 原來語句, 切好語句):
        字陣列 = []
        [字陣列.extend(self.篩仔.篩出字物件(self.分析器.建立詞物件(詞)))
         for 詞 in 切好語句]
        return (self.分析器.建立組物件(原來語句), 字陣列)

    def test_篩組濟字(self):
        原來語句 = '我有一張椅仔！'
        切好語句 = ['我', '有', '一', '張', '椅', '仔', '！']
        組物件, 詞陣列 = self.建立組檢查(原來語句, 切好語句)
        self.assertEqual(self.篩仔.篩出字物件(組物件), 詞陣列)

    # 為著通用佮一致性，這愛家己建立詞來鬥。大部份攏是無細字揤著，親像平行語料庫才另外閣包一層
    def test_篩組濟字配空白(self):
        原來語句 = '我 有 一張 椅仔！'
        切好語句 = ['我', '有', '一', '張', '椅', '仔', '！']
        組物件, 詞陣列 = self.建立組檢查(原來語句, 切好語句)
        self.assertEqual(self.篩仔.篩出字物件(組物件), 詞陣列)

    def test_篩組濟音標(self):
        原來語句 = 'gua2 u7 tsit8-tiunn1 i2-a2'
        處理好語句 = 'gua2 u7 tsit8-tiunn1 i2-a2'
        加空白後語句 = 'gua2 u7 tsit8-tiunn1 i2-a2'
        self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
        self.assertEqual(self.粗胚.符號邊仔加空白(處理好語句), 加空白後語句)
        切好語句 = ['gua2', 'u7', 'tsit8-tiunn1', 'i2-a2']
        組物件, 詞陣列 = self.建立組檢查(處理好語句, 切好語句)
        self.assertEqual(self.篩仔.篩出字物件(組物件), 詞陣列)

    def test_篩組濟字輕聲(self):
        原來語句 = 'mi2-kiann7 boo5-0ki3 ah!'
        處理好語句 = 'mi2-kiann7 boo5-0ki3 ah!'
        加空白後語句 = 'mi2-kiann7 boo5-0ki3 ah ! '
        self.assertEqual(self.粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原來語句), 處理好語句)
        self.assertEqual(self.粗胚.符號邊仔加空白(處理好語句), 加空白後語句)
        切好語句 = ['mi2-kiann7', 'boo5-0ki3', 'ah', '!']
        組物件, 詞陣列 = self.建立組檢查(處理好語句, 切好語句)
        self.assertEqual(self.篩仔.篩出字物件(組物件), 詞陣列)

    def test_篩句濟字佮符號(self):
        原來語句 = '枋寮漁港「大條巷」上闊兩公尺。'
        切好語句 = ['枋', '寮', '漁', '港', '「', '大', '條',
                '巷', '」', '上', '闊', '兩', '公', '尺', '。']
        組物件, 詞陣列 = self.建立組檢查(原來語句, 切好語句)
        self.assertEqual(self.篩仔.篩出字物件(
            self.分析器.建立句物件(原來語句)), 詞陣列)
        組物件 = 組物件

    def test_篩章濟連字佮符號(self):
        原來語句 = '枋-寮漁-港「大-條-巷」。上-闊兩-公-尺'
        切好語句 = ['枋寮', '漁港', '「', '大條巷', '」', '。', '上闊', '兩公尺']
        組物件, 詞陣列 = self.建立組檢查(原來語句, 切好語句)
        self.assertEqual(self.篩仔.篩出字物件(
            self.分析器.建立章物件(原來語句)), 詞陣列)
        組物件 = 組物件

    def test_篩集濟組(self):
        原來語句 = '我有一張椅仔！'
        組陣列 = [self.分析器.建立組物件(原來語句),
               self.分析器.建立組物件(原來語句), ]
        self.assertRaises(解析錯誤, self.篩仔.篩出字物件, 集(組陣列))

    def test_篩集無字(self):
        型 = ''
        集物件 = self.分析器.建立集物件(型)
        self.assertEqual(self.篩仔.篩出字物件(集物件), [])

    def test_篩句無字(self):
        型 = ''
        句物件 = self.分析器.建立句物件(型)
        self.assertEqual(self.篩仔.篩出字物件(句物件), [])

    def test_篩章無字(self):
        型 = ''
        章物件 = self.分析器.建立章物件(型)
        self.assertEqual(self.篩仔.篩出字物件(章物件), [])

    def test_烏白擲物件(self):
        self.assertRaises(型態錯誤, self.篩仔.篩出字物件, 2123)
        self.assertRaises(型態錯誤, self.篩仔.篩出字物件, self.篩仔)
        self.assertRaises(型態錯誤, self.篩仔.篩出字物件, None)
