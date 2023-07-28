from os import makedirs
from os.path import join, dirname, isfile
from tempfile import TemporaryDirectory
from unittest.case import TestCase
from unittest.case import skip
from 臺灣言語工具.語音合成.HTS工具.訓練HTSengine模型 import 訓練HTSEngine模型
from 臺灣言語工具.解析整理.參數錯誤 import 參數錯誤
from 臺灣言語工具.語音合成.HTS工具.安裝HTS語音辨識程式 import 安裝HTS語音辨識程式


@skip('2023.7.28發覺害--去，未來用袂著，bua̋i修')
class 訓練HTSEngine模型整合試驗(TestCase):

    @classmethod
    def setUpClass(cls):
        super(訓練HTSEngine模型整合試驗, cls).setUpClass()
        安裝HTS語音辨識程式.安裝sptk()
        安裝HTS語音辨識程式.安裝hts()
        安裝HTS語音辨識程式.掠htsDemoScript()

    def test_無data資料夾(self):
        with self.assertRaises(參數錯誤):
            with TemporaryDirectory() as 資料夾:
                訓練HTSEngine模型.訓練(資料夾, 44100, 顯示訓練過程=False)

    def test_data有欠物件(self):
        with self.assertRaises(參數錯誤):
            with TemporaryDirectory() as 資料夾:
                makedirs(join(資料夾, 'raw'))
                makedirs(join(資料夾, 'label'))
                訓練HTSEngine模型.訓練(資料夾, 44100, 顯示訓練過程=False)

    def test_一般訓練(self):
        htsengine模型 = 訓練HTSEngine模型.訓練(
            join(dirname(__file__), 'HTS訓練語料'), 44100, 顯示訓練過程=False
        )
        self.assertTrue(isfile(htsengine模型))

    def test_閣裝一擺就是更新(self):
        安裝HTS語音辨識程式.安裝sptk()
        安裝HTS語音辨識程式.安裝hts()
        安裝HTS語音辨識程式.掠htsDemoScript()
