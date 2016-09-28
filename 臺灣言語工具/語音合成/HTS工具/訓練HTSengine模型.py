from os.path import isdir, join, isfile, exists
from posix import listdir, chmod
from shutil import copytree, copyfile, rmtree
from stat import S_IRUSR, S_IXUSR, S_IWUSR
from 臺灣言語工具.解析整理.參數錯誤 import 參數錯誤
from 臺灣言語工具.語音合成.HTS工具.安裝HTS語音辨識程式 import 安裝HTS語音辨識程式
from 臺灣言語工具.系統整合.程式腳本 import 程式腳本


class 訓練HTSEngine模型(程式腳本):

    @classmethod
    def 訓練(cls, 訓練資料夾, 頻率,
           SPTK執行檔路徑=安裝HTS語音辨識程式.sptk執行檔目錄(),
           HTS執行檔路徑=安裝HTS語音辨識程式.hts執行檔目錄(),
           htsDemo目錄=安裝HTS語音辨識程式.htsDemo目錄()):
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

        cls._扣demo的資料到訓練資料夾(htsDemo目錄, 訓練資料夾)

        '走HTS'
        with cls._換目錄(訓練資料夾):
            音框長度 = 頻率 // 40
            音框移動 = 音框長度 // 5
    #         if 頻率 < 20000:
    #             參數量 = 24
    #         else:
    #             參數量 = 40
            # 'GAMMA=3 LNGAIN=1 MGCORDER={參數量}'
            chmod('./configure', S_IRUSR | S_IWUSR | S_IXUSR)
            HTS設定指令 = [
                './configure',
                '--with-sptk-search-path={}'.format(SPTK執行檔路徑),
                '--with-hts-search-path={}'.format(HTS執行檔路徑),
                'LOWERF0=60',
                'UPPERF0=500',
                'USEGV=0',
                'SAMPFREQ={}'.format(頻率),
                'FRAMELEN={}' .format(音框長度),
                'FRAMESHIFT={}'.format(音框移動),
            ]
            cls._走指令(HTS設定指令, env={'LANG': 'C'}, 愛直接顯示輸出=True)
            HTS走指令 = ['make', 'all']
            cls._走指令(HTS走指令, env={'LANG': 'C'}, 愛直接顯示輸出=True)
        return join(訓練資料夾, 'voices', 'qst001', 'ver1', 'ver1.htsvoice')

    @classmethod
    def _扣demo的資料到訓練資料夾(cls, htsDemo目錄, 訓練資料夾):
        for 檔案 in listdir(htsDemo目錄):
            路徑 = join(htsDemo目錄, 檔案)
            if not 檔案.startswith('.') and 檔案 != 'data':
                目標所在 = join(訓練資料夾, 檔案)
                if isfile(路徑):
                    copyfile(路徑, 目標所在)
                else:
                    if exists(目標所在):
                        rmtree(目標所在)
                    copytree(路徑, 目標所在)

        data目錄 = join(htsDemo目錄, 'data')
        訓練data資料夾 = join(訓練資料夾, 'data')
        for 檔案 in listdir(data目錄):
            路徑 = join(data目錄, 檔案)
            目標所在 = join(訓練data資料夾, 檔案)
            if isfile(路徑):
                copyfile(路徑, 目標所在)
            else:
                if exists(目標所在):
                    rmtree(目標所在)
                copytree(路徑, 目標所在)
