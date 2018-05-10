# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 拆文分析器輕聲單元試驗(TestCase):
    def test_句頭輕聲(self):
        型 = '--啊'
        音 = '--ah'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertTrue(組物件.篩出字物件()[0].敢有輕聲標記())

    def test_句中輕聲(self):
        型 = '後--日'
        音 = 'āu--ji̍t'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertFalse(組物件.篩出字物件()[0].敢有輕聲標記())
        self.assertTrue(組物件.篩出字物件()[1].敢有輕聲標記())

    def test_句中分開輕聲(self):
        型 = '食飽矣'
        音 = 'tsia̍h-pá --ah'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertFalse(組物件.篩出字物件()[0].敢有輕聲標記())
        self.assertFalse(組物件.篩出字物件()[1].敢有輕聲標記())
        self.assertTrue(組物件.篩出字物件()[-1].敢有輕聲標記())

    def test_有先用文章粗坯處理減號的輕聲(self):
        型 = '後日'
        音 = 'āu-0ji̍t'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertTrue(組物件.篩出字物件()[-1].敢有輕聲標記())

    def test_型音其中一个有輕聲_音有(self):
        型 = '後日'
        音 = 'āu--ji̍t'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertTrue(組物件.篩出字物件()[-1].敢有輕聲標記())

    def test_型音其中一个有輕聲_型有(self):
        型 = '後--日'
        音 = 'āu-ji̍t'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertTrue(組物件.篩出字物件()[-1].敢有輕聲標記())

    def test_兩字詞一半輕聲(self):
        漢 = '講會出--來'
        組物件 = 拆文分析器.建立組物件(漢)
        self.assertFalse(組物件.篩出字物件()[2].敢有輕聲標記())
        self.assertTrue(組物件.篩出字物件()[3].敢有輕聲標記())

    def test_兩字輕聲詞(self):
        漢 = '講--出-來'
        組物件 = 拆文分析器.建立組物件(漢)
        self.assertFalse(組物件.篩出字物件()[0].敢有輕聲標記())
        self.assertTrue(組物件.篩出字物件()[1].敢有輕聲標記())
        self.assertFalse(組物件.篩出字物件()[2].敢有輕聲標記())

    def test_連續輕聲詞(self):
        音 = '害--矣--啦'
        組物件 = 拆文分析器.建立組物件(音)
        self.assertFalse(組物件.篩出字物件()[0].敢有輕聲標記())
        self.assertTrue(組物件.篩出字物件()[1].敢有輕聲標記())
        self.assertTrue(組物件.篩出字物件()[2].敢有輕聲標記())

    def test_輕聲的音免加0(self):
        # 以前用 0ah 標示這是輕聲字
        # 這馬用 敢有輕聲標記()
        型 = '--啊'
        音 = '--ah'
        組物件 = 拆文分析器.對齊組物件(型, 音)
        self.assertEqual(組物件.篩出字物件()[0].音, 'ah')
