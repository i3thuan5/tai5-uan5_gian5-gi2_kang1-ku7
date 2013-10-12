from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器

class 第四步建立句物件:
	分析器 = 拆文分析器()
	def 建立(self, 語句):
		資料 = []
		for 句 in 語句:
			資料.append(self.建立一句(句))
		return 資料
	def 建立一句(self, 句):
		(標籤, 漢羅, 音標) = 句
		try:
			句物件=self.分析器.產生對齊句(漢羅, 音標)
		except Exception as 錯誤:
			print("有問題！！{0}".format(錯誤))
			return (標籤, None)
		return (標籤, 句物件)
