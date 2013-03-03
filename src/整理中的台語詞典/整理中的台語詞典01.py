'''
Created on 2013/3/3

@author: Ihc
'''

from 教育部臺灣閩南語常用詞辭典.資料庫連線 import 資料庫連線
from 文章音標解析器 import 文章音標解析器
from 通用拼音音標 import 通用拼音音標

揣攏總資料 = 資料庫連線.prepare('SELECT "識別碼","unz","imbiau" ' +
	'FROM "整理中的台語詞典"."整理中的台語詞典01" ORDER BY "識別碼" ASC')

通用解析器 = 文章音標解析器(通用拼音音標)
通用解析器.合法字元 = {'_'}
for 識別碼, 字, 音 in 揣攏總資料():
# 	print(識別碼)
	通用解析結果, 通用合法無 = 通用解析器.解析語句佮顯示毋著字元(音)
	if 通用合法無 == False:
		print(字 + ' ' + 音)
		print('通用解析結果=' + 通用解析結果)
