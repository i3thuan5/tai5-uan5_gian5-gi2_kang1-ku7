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
import xmlrpc.client
from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器
from 臺灣言語工具.翻譯.摩西工具.無編碼器 import 無編碼器

class 摩西用戶端():
	網址格式 = "http://{0}:{1}/{2}"
	未知詞記號 = '|UNK|UNK|UNK'
	def __init__(self, 位址, 埠, 路徑 = 'RPC2', 編碼器 = 無編碼器()):
		網址 = self.網址格式.format(位址, 埠, 路徑)
		self.主機 = xmlrpc.client.ServerProxy(網址)
		self.編碼器 = 編碼器
	def 翻譯(self, 語句, 另外參數 = {}):
		來源 = self.編碼器.編碼(語句)
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
		結果['text'] = self.編碼器.解碼(結果['text'])
		if 'nbest' in 結果:
			for 候選 in 結果['nbest']:
				候選['hyp'] = self.編碼器.解碼(候選['hyp'])
		return 結果
	def 更新(self, 來源, 目標, 對齊):
		來源 = self.編碼器.編碼(來源)
		目標 = self.編碼器.編碼(目標)

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
	用戶端 = 摩西用戶端('localhost', '8080', 編碼器 = 編碼器)
	語句 = "他 和 我 要 去 吃 飯 我 欲 去 食 飯 ."
	結果 = 用戶端.翻譯(語句, 另外參數 = {'nbest':3})
	print(結果['nbest'][0]['hyp'].split())
	print(結果)
	if 'align' in 結果:
		print("Phrase alignments:")
		aligns = 結果['align']
		for align in aligns:
			print("%s,%s,%s" % (align['tgt-start'], align['src-start'], align['src-end']))
	print(用戶端.翻譯('我 想 吃 飯 。 我 想 吃 很 多 飯 > 。')['text'])
	print(用戶端.翻譯('我 想 )  :>')['text'])
	語句 = "他 們 和 我 要 去 吃 飯 我 欲 去 食 飯 ."
	try:
		print(用戶端.翻譯(語句)['text'])
	except Exception as 出問題:
		raise RuntimeError('無支援第二平面：{}'.format(出問題))
	語句 = "𪜶 他 們 和 我 要 去 吃 飯 我 欲 去 食 飯 ."
	print(用戶端.翻譯(語句)['text'])
# 	來源 = "我 要 吃 。"
# 	目標 = "我｜gua2 欲｜beh4 食｜tsiah8  飯｜png7 。｜."
# 	對齊 = "0-0 1-1 2-2 2-3 3-4"
# # 	對齊 = "1-1 2-2 3-3 3-4 5-4"
# 	用戶端.更新(來源, 目標, 對齊)
# 	用戶端.最佳化([('他 打 我','伊 共 我 拍')], 'PhraseDictionaryMultiModelCounts0')

