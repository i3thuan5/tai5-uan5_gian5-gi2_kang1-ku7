import htsengine
from 臺灣言語工具.語音辨識.聲音檔 import 聲音檔


class HTS合成模型:

    def __init__(self, 模型所在):
        self._模型所在 = 模型所在

    def 合成(self, 愛合成標仔):
        return 聲音檔.對參數轉(*htsengine.synthesize(self._模型所在, 愛合成標仔))
