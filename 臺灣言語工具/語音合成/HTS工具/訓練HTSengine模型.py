from os.path import isdir, join
from 臺灣言語工具.解析整理.參數錯誤 import 參數錯誤


class 訓練HTSEngine模型:

    @classmethod
    def 訓練(cls, 訓練資料夾,頻率):
        if (
            not isdir(join(訓練資料夾, 'data', 'raw')) or
            not isdir(join(訓練資料夾, 'data', 'labels', 'mono')) or
            not isdir(join(訓練資料夾, 'data', 'labels', 'full')) or
            not isdir(join(訓練資料夾, 'data', 'questions'))
        ):
            raise 參數錯誤(
                '訓練資料夾的data內底有欠資料！！'
                '請看臺灣言語工具的文件'
            )
            
        '走HTS'
        音框長度 = 頻率 // 40
        音框移動 = 音框長度 // 5
        if 頻率 < 20000:
            參數量 = 24
        else:
            參數量 = 40
        HTS設定指令 = (
            '''LANG=C ./configure --with-sptk-search-path={0} \
--with-hts-search-path={1} \
--with-hts-engine-search-path={2} \
LOWERF0=60 UPPERF0=500 SAMPFREQ={3} FRAMELEN={4} FRAMESHIFT={5} \
USEGV=0\
GAMMA=3 LNGAIN=1 MGCORDER={6} 
'''
        ).format(
            SPTK執行檔路徑, HTS執行檔路徑, HTS_ENGINE執行檔路徑,
            頻率, 音框長度, 音框移動, 參數量
        )
        cls._走指令(HTS設定指令)
        HTS走指令 = 'LANG=C make all'
        cls._走指令(HTS走指令)

