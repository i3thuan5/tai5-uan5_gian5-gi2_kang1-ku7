from 字詞組集句章.基本元素.公用變數 import 標點符號

class 第三步整理文本格式:
	def 整理(self, 分堆句):
		資料 = []
		for 分堆 in 分堆句:
			資料.append(self.整理一句(分堆))
		return 資料
	def 整理一句(self, 分堆):
		(標籤, 漢羅, 音標) = 分堆
		新音標 = 音標.strip('-').replace(',', ' ').strip()
		新音標 = 新音標.replace('- ', '-')
		新漢羅 = 漢羅
		for 符號 in 標點符號:
			新漢羅 = 新漢羅.replace(符號, ' ')
		新漢羅 = 新漢羅.replace('ｅ', ' e ')
		return (標籤.strip(), 新漢羅.strip(), 新音標.strip())
