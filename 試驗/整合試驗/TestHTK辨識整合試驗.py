import os
from os.path import join, isdir, isfile
from posix import listdir
from shutil import rmtree
from tempfile import mkdtemp
from unittest.case import TestCase
from 臺灣言語工具.語音辨識.模型訓練 import 模型訓練
from 臺灣言語工具.語音辨識.語料處理 import 語料處理


class HTK辨識整合試驗(TestCase):

    @classmethod
    def setUpClass(cls):
        語料目錄 = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), '語音語料'
        )
        cls.音檔目錄 = os.path.join(語料目錄, 'wav')
        cls.標仔目錄 = os.path.join(語料目錄, 'labels')
        cls.音節聲韻對照檔=os.path.join(語料目錄, '聲韻對照.dict')
        cls.期待模型檔資料夾 = os.path.join(語料目錄, '期待模型檔')
        cls.試驗語料暫存目錄 = mkdtemp()

        cls.特徵檔, cls.音節檔, cls.聲韻檔 = 語料處理.處理試驗語料(
            cls.音檔目錄,
            cls.試驗語料暫存目錄,
            cls.標仔目錄,
            cls.音節聲韻對照檔
        )

    @classmethod
    def tearDownClass(cls):
        rmtree(cls.試驗語料暫存目錄)

    def setUp(self):
        self.暫存目錄 = mkdtemp()

        self.訓練 = 模型訓練()

    def tearDown(self):
        rmtree(self.暫存目錄)

    def test_原本標音模型訓練(self):
        原本標音辨識模型 = self.訓練.訓練原本標音辨識模型(
            self.音檔目錄, self.標仔目錄, self.音節聲韻對照檔, self.暫存目錄
        )
        期待模型檔 = join(self.期待模型檔資料夾, '原始標音模型.macro')
        with open(原本標音辨識模型.模型參數檔所在()) as 結果:
            with open(期待模型檔) as 答案:
                self.assertEqual(結果.read(), 答案.read(), self.暫存目錄)

        原本目錄 = os.path.join(self.暫存目錄, '原本')
        os.makedirs(原本目錄, exist_ok=True)

        self.檢查資料夾有辨識出來的檔案(原本標音辨識模型.對齊聲韻(self.聲韻檔, self.特徵檔, 原本目錄))
        self.檢查資料夾有辨識出來的檔案(原本標音辨識模型.對齊音節(self.音節檔, self.特徵檔, 原本目錄))
        self.檢查辨識結果(原本標音辨識模型.辨識聲韻(self.特徵檔, 原本目錄, 3))
        self.檢查辨識結果(原本標音辨識模型.辨識音節(self.特徵檔, 原本目錄, 3))

    def test_拄好短恬模型訓練(self):
        拄好短恬辨識模型 = self.訓練.訓練拄好短恬辨識模型(
            self.音檔目錄, self.標仔目錄, self.音節聲韻對照檔, self.暫存目錄
        )
        期待模型檔 = join(self.期待模型檔資料夾, '加短恬模型.macro')
        with open(拄好短恬辨識模型.模型參數檔所在()) as 結果:
            with open(期待模型檔) as 答案:
                self.assertEqual(結果.read(), 答案.read())

        加短恬目錄 = os.path.join(self.暫存目錄, '加短恬')
        os.makedirs(加短恬目錄, exist_ok=True)

        self.檢查資料夾有辨識出來的檔案(拄好短恬辨識模型.對齊聲韻(self.聲韻檔, self.特徵檔, 加短恬目錄))
        self.檢查資料夾有辨識出來的檔案(拄好短恬辨識模型.對齊音節(self.音節檔, self.特徵檔, 加短恬目錄))
        self.檢查辨識結果(拄好短恬辨識模型.辨識聲韻(self.特徵檔, 加短恬目錄, 3))
        self.檢查辨識結果(拄好短恬辨識模型.辨識音節(self.特徵檔, 加短恬目錄, 3))

    def test_新拄好短恬聲韻檔對齊(self):
        self.檢查資料夾有辨識出來的檔案(
            self.訓練.加短恬閣對齊(
                self.音檔目錄, self.標仔目錄, self.音節聲韻對照檔, self.暫存目錄
            )
        )

    def test_三連音模型訓練(self):
        三連音辨識模型 = self.訓練.訓練三連音辨識模型(
            self.音檔目錄, self.標仔目錄, self.音節聲韻對照檔, self.暫存目錄
        )
        期待模型檔 = join(self.期待模型檔資料夾, '三連音全部縛做伙模型.macro')
        with open(三連音辨識模型.模型參數檔所在()) as 結果:
            with open(期待模型檔) as 答案:
                self.assertEqual(結果.read(), 答案.read())

        三連音目錄 = os.path.join(self.暫存目錄, '三連音')
        os.makedirs(三連音目錄, exist_ok=True)

        self.檢查資料夾有辨識出來的檔案(三連音辨識模型.對齊聲韻(self.聲韻檔, self.特徵檔, 三連音目錄))
        self.檢查資料夾有辨識出來的檔案(三連音辨識模型.對齊音節(self.音節檔, self.特徵檔, 三連音目錄))
        '若愛辨識聲韻，聲韻類檔會傷大，所以無支援'
    #     三連音辨識模型.辨識聲韻(特徵檔, 三連音目錄, 3)
        self.檢查辨識結果(三連音辨識模型.辨識音節(self.特徵檔, 三連音目錄, 3))

    def 檢查資料夾有辨識出來的檔案(self, 資料夾):
        self.assertTrue(isdir(資料夾))
        self.assertEqual(len(listdir(資料夾)), 93)

    def 檢查辨識結果(self, 辨識結果):
        音節檔, 網路資料夾 = 辨識結果
        self.assertTrue(isfile(音節檔))
        self.檢查資料夾有辨識出來的檔案(網路資料夾)
