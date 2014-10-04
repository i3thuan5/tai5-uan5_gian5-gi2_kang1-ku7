# -*- coding: utf-8 -*-
"""
著作權所有 (C) 民國103年 意傳文化科技
開發者：薛丞宏
網址：http://意傳.台灣
語料來源：請看各資料庫內說明

本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以授權原文為主：
	１．得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
	２．任何以程式碼衍生的執行檔或網路服務，必須公開該程式碼；
	３．將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
"""
import os
from 摩西翻譯模型訓練 import 摩西翻譯模型訓練

if __name__ == '__main__':
	模型訓練 = 摩西翻譯模型訓練()
	模型訓練.訓練(
		['/home/Ihc/git/i3_thuan5/語料/華', ],
		['/home/Ihc/git/i3_thuan5/語料/閩', ],
		['/home/Ihc/git/i3_thuan5/語料/閩全'],
		3,
		os.path.join(os.path.dirname(__file__), '暫存資料夾'),
		SRILM執行檔路徑='/usr/local/srilm/bin/i686-m64/',
		GIZA執行檔路徑='/usr/local/mt/',
		MOSES腳本路徑='/usr/local/mosesdecoder/scripts/',
		)
# cat ../閩 ../閩全 | python3 ~/git/huan1-ik8_gian5-kiu3/資料處理/斷一對一字.py  > 字閩語言
# cat 翻.閩 | python3 ~/git/huan1-ik8_gian5-kiu3/資料處理/斷一對一字.py > 字.閩
# cat 翻.華 | python3 ~/git/huan1-ik8_gian5-kiu3/資料處理/斷一對一字.py > 字.華


# ngram-count -order 3 -interpolate -wbdiscount -unk -text 翻譯/字閩語言 -lm 翻譯/字閩.lm
# $SCRIPTS_ROOTDIR/training/train-model.perl -root-dir 翻譯/字模型 -corpus `pwd`/翻譯/字 -f 華 -e 閩 -alignment grow-diag-final-and -reordering msd-bidirectional-fe -lm 0:3:`pwd`/翻譯/字閩.lm -external-bin-dir=/usr/local/mt/
