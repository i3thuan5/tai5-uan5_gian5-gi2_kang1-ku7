from 言語資料庫.公用資料 import 資料庫連線
from 文章音標解析器 import 文章音標解析器
from 通用拼音音標 import 通用拼音音標
from 言語資料庫.公用資料 import 標點符號

檔案 = open('/home/Ihc/意傳計劃/國閩翻譯/台語數位典藏文本—排序過.txt', 'r')

插入台語數位典藏文本資料庫 = 資料庫連線.prepare('INSERT INTO "高明達先生資料"."台語數位典藏文本" ' +
	'("字","音") VALUES ($1,$2)')

通用解析器 = 文章音標解析器(通用拼音音標)
通用解析器.標點符號 = 標點符號
字音集合=set()
for 行 in 檔案:
	if len(行.strip().split('\t')) == 2:
		字, 音 = 行.strip().split('\t')
		音解析結果, 音合法 = 通用解析器.解析語句佮顯示毋著字元(音)
		if 音合法:
			# print(音解析結果)
			字音集合.add((字, 音解析結果))
	# else:
		# print(len(行.split('\t')))
print(len(字音集合))

for 字, 音解析結果 in 字音集合:
	插入台語數位典藏文本資料庫(字, 音解析結果)
	
