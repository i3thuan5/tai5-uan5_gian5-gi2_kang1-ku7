'''
Created on 2013/3/3

@author: Ihc
'''

from 教育部臺灣閩南語常用詞辭典.資料庫連線 import 資料庫連線
from 文章音標解析器 import 文章音標解析器
from 通用拼音音標 import 通用拼音音標
from 臺灣語言音標 import 臺灣語言音標

揣攏總資料 = 資料庫連線.prepare('SELECT "識別碼","CHINESE","TAIWANESE","ForPA","TLPA" ' +
	'FROM "整理中的台語詞典"."整理中的台語詞典07" ORDER BY "識別碼" ASC')

通用解析器 = 文章音標解析器(通用拼音音標)
通用解析器.標點符號 = {'-'}
TLPA解析器 = 文章音標解析器(臺灣語言音標)
TLPA解析器.標點符號 = {'-'}
for 識別碼, CHINESE, TAIWANESE, ForPA , TLPA in 揣攏總資料():
#	print(識別碼)
	通用解析結果, 通用合法無 = 通用解析器.解析語句佮顯示毋著字元(ForPA)
	TLPA解析結果, TLPA合法無 = TLPA解析器.解析語句佮顯示毋著字元(TLPA)
	if 通用合法無 == False or TLPA合法無 == False or 通用解析結果 != TLPA解析結果:
		print(ForPA + ' != ' + TLPA)
		print('通用解析結果= ' + 通用解析結果)
		print('TLPA解析結果= ' + TLPA解析結果)
