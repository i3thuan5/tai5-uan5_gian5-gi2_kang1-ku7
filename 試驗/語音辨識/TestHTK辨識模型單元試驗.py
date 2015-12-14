from os.path import dirname, abspath, join
from tempfile import mkdtemp
from unittest.case import TestCase
from 臺灣言語工具.語音辨識.HTK工具.HTK辨識模型 import HTK辨識模型
from shutil import rmtree


class HTK辨識模型單元試驗(TestCase):

    def setUp(self):
        self.資料目錄 = join(dirname(abspath(__file__)), '模型資料')

    def test_用資料夾建立(self):
        模型 = HTK辨識模型(資料目錄=self.資料目錄)
        self.assertEqual(模型.音節聲韻對照檔所在(), join(self.資料目錄, '音節聲韻對照檔.dict'))
        self.assertEqual(模型.聲韻類檔所在(), join(self.資料目錄, '聲韻類檔.list'))
        self.assertEqual(模型.模型參數檔所在(), join(self.資料目錄, '模型參數檔.macro'))

    def test_用音節聲韻對照檔佮聲韻類檔佮模型參數檔建立(self):
        模型 = HTK辨識模型(
            音節聲韻對照檔=join(self.資料目錄, '音節聲韻對照檔.dict'),
            聲韻類檔=join(self.資料目錄, '聲韻類檔.list'),
            模型參數檔=join(self.資料目錄, '模型參數檔.macro'),
        )
        self.assertEqual(模型.音節聲韻對照檔所在(), join(self.資料目錄, '音節聲韻對照檔.dict'))
        self.assertEqual(模型.聲韻類檔所在(), join(self.資料目錄, '聲韻類檔.list'))
        self.assertEqual(模型.模型參數檔所在(), join(self.資料目錄, '模型參數檔.macro'))

    def test_檔案無存在(self):
        with self.assertRaises(OSError):
            HTK辨識模型(
                音節聲韻對照檔=join(self.資料目錄, '音節聲韻對照檔'),
                聲韻類檔=join(self.資料目錄, '聲韻類檔'),
                模型參數檔=join(self.資料目錄, '模型參數檔'),
            )

    def test_存模型(self):
        暫存目錄 = mkdtemp()
        模型 = HTK辨識模型(self.資料目錄)
        模型.存資料佇(暫存目錄)
        for 檔名 in ['音節聲韻對照檔.dict', '聲韻類檔.list', '模型參數檔.macro']:
            with open(join(self.資料目錄, 檔名)) as 結果:
                with open(join(暫存目錄, 檔名)) as 答案:
                    self.assertEqual(結果.read(), 答案.read())
        rmtree(暫存目錄)
