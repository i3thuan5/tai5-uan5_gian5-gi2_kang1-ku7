from os.path import isdir, isfile, join, dirname, abspath
from posix import listdir
from shutil import rmtree
from tempfile import mkdtemp
from unittest.case import TestCase
from 臺灣言語工具.語音辨識.HTK工具.HTK語料處理 import HTK語料處理
from 臺灣言語工具.語音辨識.HTK工具.HTK辨識模型訓練 import HTK辨識模型訓練


class HTK辨識整合試驗(TestCase):

    @classmethod
    def setUpClass(cls):
        語料目錄 = join(dirname(abspath(__file__)), '語音語料')
        cls.音檔目錄 = join(語料目錄, 'wav')
        cls.標仔目錄 = join(語料目錄, 'labels')
        cls.音節聲韻對照檔 = join(語料目錄, '聲韻對照.dict')
        cls.試驗語料暫存目錄 = mkdtemp()

        cls.特徵檔, cls.音節檔, cls.聲韻檔 = HTK語料處理.產生特徵佮音節佮聲韻檔(
            cls.音檔目錄,
            cls.標仔目錄,
            cls.音節聲韻對照檔,
            cls.試驗語料暫存目錄,
        )

    @classmethod
    def tearDownClass(cls):
        rmtree(cls.試驗語料暫存目錄)

    def setUp(self):
        self.模型暫存目錄 = mkdtemp()
        self.結果暫存目錄 = mkdtemp()

    def tearDown(self):
        rmtree(self.模型暫存目錄)
        rmtree(self.結果暫存目錄)

    def test_原本標音模型訓練(self):
        原本標音辨識模型 = HTK辨識模型訓練.訓練原本標音辨識模型(
            self.音檔目錄, self.標仔目錄, self.音節聲韻對照檔, self.模型暫存目錄
        )
        self.檢查資料夾有辨識出來的檔案(原本標音辨識模型.對齊聲韻(self.聲韻檔, self.特徵檔, self.結果暫存目錄))
        self.檢查資料夾有辨識出來的檔案(原本標音辨識模型.對齊音節(self.音節檔, self.特徵檔, self.結果暫存目錄))
        self.檢查辨識結果(原本標音辨識模型.辨識聲韻(self.特徵檔, self.結果暫存目錄, 3))
        self.檢查辨識結果(原本標音辨識模型.辨識音節(self.特徵檔, self.結果暫存目錄, 3))

    def test_拄好短恬模型訓練(self):
        拄好短恬辨識模型 = HTK辨識模型訓練.訓練拄好短恬辨識模型(
            self.音檔目錄, self.標仔目錄, self.音節聲韻對照檔, self.模型暫存目錄
        )
        self.檢查資料夾有辨識出來的檔案(拄好短恬辨識模型.對齊聲韻(self.聲韻檔, self.特徵檔, self.結果暫存目錄))
        self.檢查資料夾有辨識出來的檔案(拄好短恬辨識模型.對齊音節(self.音節檔, self.特徵檔, self.結果暫存目錄))
        self.檢查辨識結果(拄好短恬辨識模型.辨識聲韻(self.特徵檔, self.結果暫存目錄, 3))
        self.檢查辨識結果(拄好短恬辨識模型.辨識音節(self.特徵檔, self.結果暫存目錄, 3))

    def test_新拄好短恬聲韻檔對齊(self):
        self.檢查資料夾有辨識出來的檔案(
            HTK辨識模型訓練.對齊聲韻閣加短恬(
                self.音檔目錄, self.標仔目錄, self.音節聲韻對照檔, self.模型暫存目錄
            )
        )

    def test_新拄好短恬音節檔對齊(self):
        self.檢查資料夾有辨識出來的檔案(
            HTK辨識模型訓練.對齊音節閣加短恬(
                self.音檔目錄, self.標仔目錄, self.音節聲韻對照檔, self.模型暫存目錄
            )
        )

    def test_三連音模型訓練(self):
        三連音辨識模型 = HTK辨識模型訓練.訓練三連音辨識模型(
            self.音檔目錄, self.標仔目錄, self.音節聲韻對照檔, self.模型暫存目錄
        )
        self.檢查資料夾有辨識出來的檔案(三連音辨識模型.對齊聲韻(self.聲韻檔, self.特徵檔, self.結果暫存目錄))
        self.檢查資料夾有辨識出來的檔案(三連音辨識模型.對齊音節(self.音節檔, self.特徵檔, self.結果暫存目錄))
        '若愛辨識聲韻，聲韻類檔會傷大，所以無支援'
    #     三連音辨識模型.辨識聲韻(特徵檔, self.結果暫存目錄, 3)
        self.檢查辨識結果(三連音辨識模型.辨識音節(self.特徵檔, self.結果暫存目錄, 3))

    def 檢查資料夾有辨識出來的檔案(self, 資料夾):
        self.assertTrue(isdir(資料夾))
        self.assertEqual(len(listdir(資料夾)), 93)

    def 檢查辨識結果(self, 辨識結果):
        音節檔, 網路資料夾 = 辨識結果
        self.assertTrue(isfile(音節檔))
        self.檢查資料夾有辨識出來的檔案(網路資料夾)
