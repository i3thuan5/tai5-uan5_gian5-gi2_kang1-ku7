'''
Created on 2013/3/3

@author: Ihc
'''

from 文章音標解析器 import 文章音標解析器
from 通用拼音音標 import 通用拼音音標
from 言語資料庫.公用資料 import 資料庫連線
from 教育部臺灣閩南語常用詞辭典.資料庫連線 import 加文字

揣攏總資料 = 資料庫連線.prepare('SELECT "識別碼","unz","imbiau" ' +
	'FROM "整理中的台語詞典"."整理中的台語詞典01" ORDER BY "識別碼" ASC')

通用解析器 = 文章音標解析器(通用拼音音標)
通用解析器.標點符號 = {'-'}
# 第二个以後攏是伊拍毋著我改過來
代換字串 = [('_', '-'), ('ming', 'bing'), ('min', 'bin'), ('diuh2', 'diuh7'), ('niunn', 'niu'), ('kuh3', 'kuh4'),
	('iah2', 'iah8'), ('puah2', 'puah7'), ('mih4', 'mih7'), ('miann', 'mia'), ('kuh4', 'kuh7')]
for 識別碼, 字, 音 in 揣攏總資料():
# 	print(識別碼)
	for 錯誤, 正確 in 代換字串:
		音 = 音.replace(錯誤, 正確)
	通用解析結果, 通用合法無 = 通用解析器.解析語句佮顯示毋著字元(音)
	加文字('整理中的台語詞典01', '字詞', '閩南語', '臺員', 90, 字, 通用解析結果)
	if 通用合法無 == False:
		print('通用解析結果=' + 通用解析結果)

print('完成')
