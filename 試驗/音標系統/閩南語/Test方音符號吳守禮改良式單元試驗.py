# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch


from 臺灣言語工具.音標系統.閩南語.方音符號吳守禮改良式 import 方音符號吳守禮改良式


class 方音符號吳守禮改良式單元試驗(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_零聲母聲韻調輕(self):
        方音 = 方音符號吳守禮改良式('ㆮ˫')
        self.assertEqual(方音.音標, 'ㆮ˫')
        self.assertEqual(方音.聲, '')
        self.assertEqual(方音.韻, 'ㆮ')
        self.assertEqual(方音.調, '˫')
        self.assertEqual(方音.輕, '')
        self.assertEqual(方音.轉換到臺灣閩南語羅馬字拼音(), 'ainn7')

    def test_完整聲韻調輕(self):
        方音 = 方音符號吳守禮改良式('ㄒㄧㆷ')
        self.assertEqual(方音.音標, 'ㄒㄧㆷ')
        self.assertEqual(方音.聲, 'ㄒ')
        self.assertEqual(方音.韻, 'ㄧㆷ')
        self.assertEqual(方音.調, '')
        self.assertEqual(方音.輕, '')
        self.assertEqual(方音.轉換到臺灣閩南語羅馬字拼音(), 'sih4')

    def test_陽入聲聲韻調輕(self):
        方音 = 方音符號吳守禮改良式('ㄒㄧ㆐ㆷ')
        self.assertEqual(方音.音標, 'ㄒㄧ㆐ㆷ')
        self.assertEqual(方音.聲, 'ㄒ')
        self.assertEqual(方音.韻, 'ㄧㆷ')
        self.assertEqual(方音.調, '㆐')
        self.assertEqual(方音.輕, '')
        self.assertEqual(方音.轉換到臺灣閩南語羅馬字拼音(), 'sih8')

    def test_韻化輔音聲韻調輕(self):
        方音 = 方音符號吳守禮改良式('ㆭˊ')
        self.assertEqual(方音.音標, 'ㆭˊ')
        self.assertEqual(方音.聲, '')
        self.assertEqual(方音.韻, 'ㆭ')
        self.assertEqual(方音.調, 'ˊ')
        self.assertEqual(方音.輕, '')
        self.assertEqual(方音.轉換到臺灣閩南語羅馬字拼音(), 'ng5')

    def test_一般輕聲聲韻調輕(self):
        方音 = 方音符號吳守禮改良式('˙ㆤ')
        self.assertEqual(方音.音標, '˙ㆤ')
        self.assertEqual(方音.聲, '')
        self.assertEqual(方音.韻, 'ㆤ')
        self.assertEqual(方音.調, '')
        self.assertEqual(方音.輕, '˙')
        self.assertEqual(方音.轉換到臺灣閩南語羅馬字拼音(), '0e1')

    def test_語法聲聲韻調輕(self):
        方音 = 方音符號吳守禮改良式('˙ㆤˊ')
        self.assertEqual(方音.音標, '˙ㆤˊ')
        self.assertEqual(方音.聲, '')
        self.assertEqual(方音.韻, 'ㆤ')
        self.assertEqual(方音.調, 'ˊ')
        self.assertEqual(方音.輕, '˙')
        self.assertEqual(方音.轉換到臺灣閩南語羅馬字拼音(), '0e5')

    def test_違法音標(self):
        方音 = 方音符號吳守禮改良式('˙ㆤㄨ')
        self.assertEqual(方音.音標, None)

    @patch('臺灣言語工具.音標系統.閩南語.方音符號吳守禮改良式.方音符號吳守禮改良式.轉換到臺灣閩南語羅馬字拼音')
    def test_預設音標(self, 轉臺羅mock):
        方音符號吳守禮改良式('ㆮ˫').預設音標()
        轉臺羅mock.assert_called_once_with()
