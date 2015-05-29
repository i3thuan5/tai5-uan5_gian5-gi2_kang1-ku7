# -*- coding: utf-8 -*-
import os
from 臺灣言語工具.翻譯.摩西工具.摩西翻譯模型訓練 import 摩西翻譯模型訓練
from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器
from 臺灣言語工具.翻譯.摩西工具.斷詞轉斷字的編碼器 import 斷詞轉斷字編碼器

if __name__ == '__main__':
	平行華語 = ['/home/Ihc/git/i3_thuan5/語料/華', ]
	平行閩南語 = ['/home/Ihc/git/i3_thuan5/語料/閩', ]
	閩南語語料 = ['/home/Ihc/git/i3_thuan5/語料/閩全', ]
	模型訓練 = 摩西翻譯模型訓練()
	這馬資料夾 = os.path.dirname(os.path.abspath(__file__))
	斷詞暫存資料夾 = os.path.join(這馬資料夾, '斷詞暫存資料夾')
	模型訓練.訓練(
		平行華語, 平行閩南語, 閩南語語料,
		斷詞暫存資料夾,
		連紲詞長度=3,
		編碼器=語句編碼器(),
		SRILM執行檔路徑='/usr/local/srilm/bin/i686-m64/',
		GIZA執行檔路徑='/usr/local/mt/',
		MOSES腳本路徑='/usr/local/mosesdecoder/scripts/',
		)

	斷詞編碼器 = 斷詞轉斷字編碼器()
	斷字暫存資料夾 = os.path.join(這馬資料夾, '斷字暫存資料夾')
	模型訓練.訓練(
		平行華語, 平行閩南語, 閩南語語料,
		斷字暫存資料夾,
		連紲詞長度=3,
		編碼器=斷詞編碼器(),
		SRILM執行檔路徑='/usr/local/srilm/bin/i686-m64/',
		GIZA執行檔路徑='/usr/local/mt/',
		MOSES腳本路徑='/usr/local/mosesdecoder/scripts/',
		)
