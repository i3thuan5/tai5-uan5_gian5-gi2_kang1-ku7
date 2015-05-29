# -*- coding: utf-8 -*-
import os
from 臺灣言語工具.翻譯.摩西工具.摩西翻譯模型訓練 import 摩西翻譯模型訓練
from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器

if __name__ == '__main__':
	平行華語 = ['/home/tshau/華', ]
	平行閩南語 = ['/home/tshau/閩', ]
	閩南語語料 = ['/home/tshau/閩', ]
	模型訓練 = 摩西翻譯模型訓練()
	模型訓練.訓練(
		平行華語, 平行閩南語, 閩南語語料,
		os.path.join(os.path.dirname(os.path.abspath(__file__)), '暫存資料夾'),
		連紲詞長度=1,
		編碼器=語句編碼器(),
		SRILM執行檔路徑='/home/tshau/git/mosesdecoder-depth1',
		GIZA執行檔路徑='/home/tshau/git/mgiza/mgizapp/bin',
		MOSES腳本路徑='/home/tshau/git/mosesdecoder-depth1/scripts/',
		)
