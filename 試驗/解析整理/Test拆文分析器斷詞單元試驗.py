# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 拆文分析器斷詞單元試驗(TestCase):

    def tearDown(self):
        句物件 = 拆文分析器.建立句物件(self.語句)
        self.assertEqual(len(句物件.網出詞物件()), self.詞數, self.語句)

    def test_全羅看有黏做伙無決定斷詞(self):
        self.語句 = 'Guan2 tsit4-ma2'
        self.詞數 = 2

    def test_全羅輕聲看有黏做伙無決定斷詞(self):
        self.語句 = 'Mi̍h-kiānn phah-bô--khì --ah'
        self.詞數 = 3

    def test_漢羅寫做伙ài斷詞(self):
        self.語句 = '台文通訊Bóng報'
        self.詞數 = 3

    def test_漢羅輕聲(self):
        self.語句 = '阿菊姨--ā'
        self.詞數 = 1

    def test_漢羅分開2詞(self):
        self.語句 = '媠 koo-niû'
        self.詞數 = 2

    def test_漢字看有黏做伙無決定斷詞(self):
        self.語句 = '媠 姑娘'
        self.詞數 = 2

    def test_漢字輕聲就當作無仝詞(self):
        self.語句 = '好 --矣'
        self.詞數 = 2

    def test_輕聲詞中央可能有重音詞(self):
        self.語句 = '有--ê-無--ê'
        self.詞數 = 1

    def test_輕聲符無(self):
        self.語句 = '有--ê無--ê'
        self.詞數 = 2

    def test_漢字知影有輕聲猶原一個詞(self):
        self.語句 = '害--矣--啦'
        self.詞數 = 1

    def test_全漢連續輕聲(self):
        self.語句 = '緊--出-來--啦'
        self.詞數 = 1

    def test_漢字濟字輕聲混合201802p13(self):
        self.語句 = '想--起-來就'
        self.詞數 = len(['想--起-來', '就'])

    def test_漢字濟字輕聲混合201802p13接羅馬字(self):
        self.語句 = '想--起-來tō ē'
        self.詞數 = len(['想--起-來', 'tō', 'ē'])

    def test_漢字濟字輕聲混合201802p13句尾(self):
        self.語句 = '想--起-來tō'
        self.詞數 = len(['想--起-來', 'tō'])

    def test_句中輕聲無連做伙嘛會使(self):
        self.語句 = '講會出--來'
        self.詞數 = 1

    def test_句中輕聲kah4後壁無連做伙嘛會使(self):
        self.語句 = '講--出-來'
        self.詞數 = 1

    def test_組字當作漢字(self):
        self.語句 = '癩⿸疒哥人'
        self.詞數 = 1

    def test_標點愛分開(self):
        self.語句 = '我愛「白話字」！'
        self.詞數 = 5

    def test_有連字符就認連字符(self):
        self.語句 = '無-？-bo5-?'
        self.詞數 = 1

    def test_連寫的客話音標(self):
        self.語句 = 'ngaiˇ dong+ho^'
        self.詞數 = 3

    def test_有連字符的客話音標(self):
        self.語句 = 'ngaiˇ dong+-ho^'
        self.詞數 = 2

    def test_漢字佮算式(self):
        self.語句 = '所以是5 - 3 = 2!'
        self.詞數 = len(['所以是', '5', '-', '3', '=', '2',  '!'])

    def test_時間符號(self):
        self.語句 = '伊18:30會來'
        self.詞數 = len(['伊', '18', ':', '30', '會來'])

    def test_日文前臺羅(self):
        self.語句 = 'si7げ'
        self.詞數 = 1

    def test_日文後數字(self):
        self.語句 = '仕上げ714'
        self.詞數 = len(['仕上げ', '714'])

    def test_濟字連字號尾(self):
        self.語句 = ' tsio1-sian3 - '
        self.詞數 = len(['tsio1-sian3', '-'])

    def test_臺羅刪節號(self):
        self.語句 = 'Pang-liau5 hi5-kang2...'
        self.詞數 = len(['Pang-liau5', 'hi5-kang2', '...'])

    def test_漢字刪節號(self):
        self.語句 = '枋寮漁港……'
        self.詞數 = len(['枋寮漁港', '……'])

    def test_tab當做空白(self):
        self.語句 = '\t千金小姐\ttshian1-kim1-sio2-tsia2\t'
        self.詞數 = 2

    def test_純日文(self):
        self.語句 = "オートバイ"
        self.詞數 = 1

    def test_漢字日文(self):
        self.語句 = '逐工踏伊的#オートバイ#（oo-tóo-bái）去貓空山頂種菜，'
        self.詞數 = len([
            '逐工踏伊的',
            '#', 'オートバイ', '#', '（', 'oo-tóo-bái', '）',
            '去貓空山頂種菜', '，'
        ])

    def test_羅馬字日文(self):
        self.語句 = 'ta̍k kang ta̍h i ê #オートバイ# (oo-tóo-bái) khì Niau-khang suann-tíng tsìng tshài,'
        self.詞數 = 17

    def test_注音符號(self):
        self.語句 = 'ㄙㄨㄧˋ ㄍㆦ ㄋㄧㄨˊ'
        self.詞數 = 3

    def test_注音摻英文數字(self):
        self.語句 = 'three ㄙㄨㄧˋ 3 姑 ㄋㄧㄨˊ'
        self.詞數 = 5

    def test_組字式注音(self):
        self.語句 = '⿿⿿⿿ㄙㄨㄧˋ⿿ㄍㆦ⿿⿿⿿ㄋㄧㄨˊ'
        self.詞數 = 1

    def test_半形大括號(self):
        self.語句 = '你{共人}看'
        self.詞數 = 5

    def test_錯誤ê連字符(self):
        self.語句 = '----你'
        self.詞數 = 5
