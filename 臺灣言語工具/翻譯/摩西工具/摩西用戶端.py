
import xmlrpc.client

class 摩西用戶端():
	網址格式 = "http://{0}:{1}/RPC2"
	def __init__(self, 位址, 埠):
		網址 = self.網址格式.format(位址, 埠)
		self.主機 = xmlrpc.client.ServerProxy(網址)
	def 翻譯(self, 語句):
		參數 = {"text":語句, "align":"true", "report-all-factors":"true",
			'nbest':0}
# 218     si = params.find("sg");
# 220     si = params.find("topt");
# 224     si = params.find("nbest");
# 226     si = params.find("nbest-distinct")
		return self.主機.translate(參數)

if __name__ == '__main__':
	用戶端 = 摩西用戶端('localhost','8011')
	語句 = "他 和 我 要 去 吃 飯 我 欲 去 食 飯 ."
	結果=用戶端.翻譯(語句)
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
	except:
		print('無支援2-mp')
