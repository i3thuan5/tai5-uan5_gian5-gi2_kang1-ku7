import os
from os.path import join
from tempfile import mkdtemp
from unittest.case import TestCase
from 臺灣言語工具.語音辨識.模型訓練 import 模型訓練
from 臺灣言語工具.語音辨識.辨識模型 import 辨識模型


class HTK辨識整合試驗(TestCase):

    def setUp(self):
        語料目錄 = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '語音語料'
        )
        self.音檔目錄 = os.path.join(語料目錄, 'wav')
        self.標仔目錄 = os.path.join(語料目錄, 'labels')
        self.音節聲韻對照檔 = os.path.join(語料目錄, '聲韻對照.dict')

        試驗語料暫存目錄 = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '暫存目錄試驗語料暫存目錄'
        )
        模型 = 辨識模型()
        self.特徵檔, self.音節檔, self.聲韻檔 = 模型.處理試驗語料(
            self.音檔目錄,
            試驗語料暫存目錄,
            self.標仔目錄,
            self.音節聲韻對照檔
        )

        self.訓練 = 模型訓練()
        self.模型 = 辨識模型()

    def test_原本標音模型訓練(self):
        暫存目錄 = mkdtemp()
        原本模型檔, 原本聲韻類檔 = self.訓練.訓練原本標音模型(
            self.音檔目錄, self. 標仔目錄, self.音節聲韻對照檔, 暫存目錄
        )
        期待模型檔 = join(
            os.path.dirname(os.path.abspath(__file__)),
            '暫存目錄', '原本標音模型', '加混合了模型-重估.macro'
        )
        with open(原本模型檔) as 結果:
            with open(期待模型檔) as 答案:
                self.assertEqual(結果.read(), 答案.read())

        原本目錄 = os.path.join(暫存目錄, '原本')
        os.makedirs(原本目錄, exist_ok=True)
        對齊聲韻結果檔 = self.模型.對齊聲韻(原本聲韻類檔, 原本模型檔, self.聲韻檔, self.特徵檔, 原本目錄)
        對齊音節結果檔 = self.模型.對齊音節(
            self.音節聲韻對照檔, 原本聲韻類檔, 原本模型檔, self.音節檔, self.特徵檔, 原本目錄)
        self. 模型.辨識聲韻(原本聲韻類檔, 原本模型檔, self.特徵檔, 原本目錄, 3)
        self.模型.辨識音節(self.音節聲韻對照檔, 原本聲韻類檔, 原本模型檔, self.特徵檔, 原本目錄, 3)

    def test_拄好短恬模型訓練(self):
        暫存目錄 = mkdtemp()
        加短恬模型檔, 加短恬聲韻類檔 = self.訓練.訓練拄好短恬模型(
            self.音檔目錄, self. 標仔目錄, self.音節聲韻對照檔, 暫存目錄
        )
        期待模型檔 = join(
            os.path.dirname(os.path.abspath(__file__)),
            '暫存目錄', '短恬目錄', '加混合了模型-重估.macro'
        )
        with open(加短恬模型檔) as 結果:
            with open(期待模型檔) as 答案:
                self.assertEqual(結果.read(), 答案.read())

        加短恬目錄 = os.path.join(暫存目錄, '加短恬')
        os.makedirs(加短恬目錄, exist_ok=True)
        對齊聲韻結果檔 = self.模型.對齊聲韻(加短恬聲韻類檔, 加短恬模型檔, self.聲韻檔, self.特徵檔, 加短恬目錄)
        對齊音節結果檔 = self.模型.對齊音節(
            self.音節聲韻對照檔, 加短恬聲韻類檔, 加短恬模型檔, self.音節檔, self.特徵檔, 加短恬目錄)
        self.模型.辨識聲韻(加短恬聲韻類檔, 加短恬模型檔, self. 特徵檔, 加短恬目錄, 3)
        self.模型.辨識音節(self.音節聲韻對照檔, 加短恬聲韻類檔, 加短恬模型檔, self.特徵檔, 加短恬目錄, 3)

    def test_新拄好短恬聲韻檔對齊(self):
        暫存目錄 = mkdtemp()
        對齊聲韻結果檔 = self.訓練.加短恬閣對齊(
            self.音檔目錄, self. 標仔目錄, self.音節聲韻對照檔, 暫存目錄
        )
        期待結果檔 = join(
            os.path.dirname(os.path.abspath(__file__)),
            '暫存目錄', '加短恬配拄好', '三連音全部縛做伙模型.macro'
        )
        with open(對齊聲韻結果檔) as 結果:
            with open(期待結果檔) as 答案:
                self.assertEqual(結果.read(), 答案.read())

    def test_三連音模型訓練(self):
        暫存目錄 = mkdtemp()
        三連音聲韻類檔, 三連音模型檔 = self.訓練.訓練三連音模型(
            self.音檔目錄, self. 標仔目錄, self.音節聲韻對照檔, 暫存目錄
        )
        期待模型檔 = join(
            os.path.dirname(os.path.abspath(__file__)),
            '暫存目錄', '三連音目錄', '三連音全部縛做伙模型.macro'
        )
        with open(三連音模型檔) as 結果:
            with open(期待模型檔) as 答案:
                self.assertEqual(結果.read(), 答案.read())

        三連音目錄 = os.path.join(暫存目錄, '三連音')
        os.makedirs(三連音目錄, exist_ok=True)
        對齊聲韻結果檔 = self.模型.對齊聲韻(三連音聲韻類檔, 三連音模型檔, self.聲韻檔, self.特徵檔, 三連音目錄)
        對齊音節結果檔 = self.模型.對齊音節(
            self.音節聲韻對照檔, 三連音聲韻類檔, 三連音模型檔, self.音節檔, self. 特徵檔, 三連音目錄)
        '若愛辨識聲韻，聲韻類檔會傷大，所以無支援'
    #     模型.辨識聲韻(三連音聲韻類檔, 三連音模型檔, 特徵檔, 三連音目錄, 3)
        self.模型.辨識音節(self.音節聲韻對照檔, 三連音聲韻類檔, 三連音模型檔, self. 特徵檔, 三連音目錄, 3)

    def test_辨識(self):
        訓練 = 模型訓練()
        暫存目錄 = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '暫存目錄'
        )
        (原本聲韻類檔, 原本模型檔),\
            (加短恬聲韻類檔, 加短恬模型檔),\
            (三連音聲韻類檔, 三連音模型檔),\
            (全部特徵檔, 原來聲韻檔, 新拄好短恬聲韻檔) = 訓練.訓練(
            self.音檔目錄, self.標仔目錄, self.音節聲韻對照檔, 暫存目錄,
        )

        加短恬目錄 = os.path.join(暫存目錄, '加短恬-新拄好短恬聲韻檔')
        os.makedirs(加短恬目錄, exist_ok=True)
        對齊聲韻結果檔 = self.模型.對齊聲韻(加短恬聲韻類檔, 加短恬模型檔, 新拄好短恬聲韻檔, self.特徵檔, 加短恬目錄)

        暫存目錄答案 = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '暫存目錄答案'
        )
        期待模型檔 = join(
            暫存目錄答案, '原始標音目錄', '加混合了模型-重估.macro'
        )
        with open(原本模型檔) as 結果:
            with open(期待模型檔) as 答案:
                self.assertEqual(結果.read(), 答案.read())

        期待模型檔 = join(
            暫存目錄答案, '短恬目錄', '加混合了模型-重估.macro'
        )
        with open(加短恬模型檔) as 結果:
            with open(期待模型檔) as 答案:
                self.assertEqual(結果.read(), 答案.read())

        期待模型檔 = join(
            暫存目錄答案, '三連音目錄', '三連音全部縛做伙模型.macro'
        )
        with open(三連音模型檔) as 結果:
            with open(期待模型檔) as 答案:
                self.assertEqual(結果.read(), 答案.read())
