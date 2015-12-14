# -*- coding: utf-8 -*-
from 臺灣言語工具.系統整合.程式腳本 import 程式腳本
import os
import shutil


from 臺灣言語工具.翻譯.摩西工具.無編碼器 import 無編碼器
from 臺灣言語工具.語言模型.KenLM語言模型訓練 import KenLM語言模型訓練
from 臺灣言語工具.系統整合.外部程式 import 外部程式


class 摩西翻譯模型訓練(程式腳本):

    @classmethod
    def 訓練(cls, 來源語言平行語料, 目標語言平行語料, 目標語言語料,
           暫存資料夾,
           連紲詞長度=3,
           編碼器=無編碼器(),
           刣掉暫存檔=True,
           giza多執行緒=False,
           moses路徑=外部程式.moses預設目錄(),
           # 愛有 mkcls, GIZA++/mgiza, & snt2cooc.out/snt2cooc
           gizapp執行檔路徑=外部程式.gizapp預設目錄(),
           # 愛有 mkcls, GIZA++/mgiza, & snt2cooc.out/snt2cooc
           mgiza執行檔路徑=外部程式.mgiza預設目錄(),
           ):
        語言模型訓練 = KenLM語言模型訓練(moses路徑)
        os.makedirs(暫存資料夾, exist_ok=True)
        語言模型檔 = 語言模型訓練.訓練(目標語言語料, 暫存資料夾, 連紲詞長度, 編碼器, 使用記憶體量='20%',)

        平行檔名 = os.path.join(暫存資料夾, '翻')
        來源平行檔名 = os.path.join(暫存資料夾, '翻.源')
        cls._檔案合做一个(來源平行檔名, 來源語言平行語料, 編碼器)
        目標平行檔名 = os.path.join(暫存資料夾, '翻.目')
        cls._檔案合做一个(目標平行檔名, 目標語言平行語料, 編碼器)

# 		翻譯模型指令版 = \
# 			'SCRIPTS_ROOTDIR={1} {1}/training/train-model.perl -root-dir {2} -corpus {3} -f {4} -e {5} -alignment grow-diag-final-and -reordering msd-bidirectional-fe -lm 0:{7}:{6} --mgiza -external-bin-dir={0}'
# 		翻譯模型指令 = 翻譯模型指令版.format(
# 				cls._執行檔路徑加尾(os.path.join(mgiza執行檔路徑, 'bin')),
# 				cls._執行檔路徑加尾(os.path.join(moses路徑, 'scripts')),
# 				暫存資料夾,
# 				平行檔名,
# 				'源',
# 				'目',
# 				語言模型檔,
# 				連紲詞長度,
# 			)
        指令 = [
            os.path.join(moses路徑, 'scripts', 'training', 'train-model.perl'),
            '-root-dir', 暫存資料夾,
            '-corpus', 平行檔名,
            '-f', '源',
            '-e', '目',
            '-alignment', 'grow-diag-final-and',
            '-reordering', 'msd-bidirectional-fe',
            '-lm', '0:{0}:{1}:9'.format(連紲詞長度, 語言模型檔),
        ]
        if not giza多執行緒:
            指令.append(
                '-external-bin-dir={0}'.format(
                    cls._執行檔路徑加尾(os.path.join(gizapp執行檔路徑, 'bin')))
            )
        else:
            指令.append('--mgiza')
            指令.append(
                '-external-bin-dir={0}'.format(
                    cls._執行檔路徑加尾(os.path.join(mgiza執行檔路徑, 'bin')))
            )
        cls._走指令(指令)
        if 刣掉暫存檔:
            shutil.rmtree(os.path.join(暫存資料夾, 'corpus'))
            shutil.rmtree(os.path.join(暫存資料夾, 'giza.源-目'))
            shutil.rmtree(os.path.join(暫存資料夾, 'giza.目-源'))
            os.remove(os.path.join(暫存資料夾, '翻.源'))
            os.remove(os.path.join(暫存資料夾, '翻.目'))
            os.remove(os.path.join(暫存資料夾, '語言模型.txt'))
            model資料夾 = os.path.join(暫存資料夾, 'model')
            for 檔名 in ['aligned.grow-diag-final-and',
                       'extract.inv.sorted.gz',
                       'extract.o.sorted.gz',
                       'extract.sorted.gz',
                       'lex.e2f',
                       'lex.f2e',
                       ]:
                os.remove(os.path.join(model資料夾, 檔名))

    @classmethod
    def _執行檔路徑加尾(cls, 執行檔路徑):
        if 執行檔路徑 != '' and not 執行檔路徑.endswith('/'):
            return 執行檔路徑 + '/'
        return 執行檔路徑
