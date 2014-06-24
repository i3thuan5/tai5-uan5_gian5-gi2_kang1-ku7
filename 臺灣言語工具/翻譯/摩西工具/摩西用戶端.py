# -*- coding: utf-8 -*-

import xmlrpc.client
from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器

class 摩西用戶端():
	網址格式 = "http://{0}:{1}/{2}"
	未知詞記號 = '|UNK|UNK|UNK'
	def __init__(self, 位址, 埠, 路徑='RPC2'):
		網址 = self.網址格式.format(位址, 埠, 路徑)
		self.主機 = xmlrpc.client.ServerProxy(網址)
	def 翻譯(self, 語句, 編碼器=None, 另外參數={}):
		if 編碼器 == None:
			來源 = 語句
		else:
			來源 = 編碼器.編碼(語句)
		參數 = {"text":來源, "align":"true", "report-all-factors":"true",
			'nbest':0}
		參數.update(另外參數)
# 218     si = params.find("sg");
# 220     si = params.find("topt");
# 224     si = params.find("nbest");
# 226     si = params.find("nbest-distinct")
		weights = None
		model_name = None
		if weights:
			if not model_name:
				raise RuntimeError("Error: if you define weights, you need to specify the feature to which the weights are to be applied (e.g. PhraseDictionaryMultiModel0)\n")
			參數['model_name'] = model_name
			參數['lambda'] = weights
		結果 = self.主機.translate(參數)
		if 編碼器 != None:
			結果['text'] = 編碼器.解碼(結果['text'])
			if 'nbest' in 結果:
				for 候選 in 結果['nbest']:
					候選['hyp'] = 編碼器.解碼(候選['hyp'])
		return 結果
	def 更新(self, 來源, 目標, 對齊, 編碼器=None):
		if 編碼器 != None:
			來源 = 編碼器.編碼(來源)
			目標 = 編碼器.編碼(目標)
		
		參數 = {"source":來源, "target":目標, "alignment":對齊}
		print("Updating with %s ..." % 參數)
		
		result = self.主機.updater(參數)
		print(result)

	def 最佳化(self, phrase_pairs, model_name):
		'''
		optimize
			phrase_pairs=[(1,2),(1,2)]
		'''
		params = {}
		params['phrase_pairs'] = phrase_pairs
		params['model_name'] = model_name
		weights = self.主機.optimize(params)
		print('weight vector (set lambda in moses.ini to this value to set as default): ')
		print(','.join(map(str, weights)) + '\n')
		return weights
	def 是未知詞(self, 詞):
		return 詞.endswith(self.未知詞記號)
	def 提掉後壁未知詞記號(self, 詞):
		return 詞[:-len(self.未知詞記號)]

if __name__ == '__main__':
	編碼器 = 語句編碼器()
	用戶端 = 摩西用戶端('localhost', '8080')
	語句 = "他 和 我 要 去 吃 飯 我 欲 去 食 飯 ."
	結果 = 用戶端.翻譯(語句, 編碼器, 另外參數={'nbest':3})
	print(結果['nbest'][0]['hyp'].split())
	print(結果)
	if 'align' in 結果:
		print("Phrase alignments:")
		aligns = 結果['align']
		for align in aligns:
			print("%s,%s,%s" % (align['tgt-start'], align['src-start'], align['src-end']))
	print(用戶端.翻譯('我 想 吃 飯 。 我 想 吃 很 多 飯 > 。', 編碼器)['text'])
	print(用戶端.翻譯('我 想 )  :>', 編碼器)['text'])
	語句 = "他 們 和 我 要 去 吃 飯 我 欲 去 食 飯 ."
	try:
		print(用戶端.翻譯(語句, 編碼器)['text'])
	except Exception as 出問題:
		raise RuntimeError('無支援第二平面：{}'.format(出問題))
	語句 = "𪜶 他 們 和 我 要 去 吃 飯 我 欲 去 食 飯 ."
	print(用戶端.翻譯(語句, 編碼器)['text'])
# 	來源 = "我 要 吃 。"
# 	目標 = "我｜gua2 欲｜beh4 食｜tsiah8  飯｜png7 。｜."
# 	對齊 = "0-0 1-1 2-2 2-3 3-4"
# # 	對齊 = "1-1 2-2 3-3 3-4 5-4"
# 	用戶端.更新(來源, 目標, 對齊, 編碼器)
# 	用戶端.最佳化([('他 打 我','伊 共 我 拍')], 'PhraseDictionaryMultiModelCounts0')
	
