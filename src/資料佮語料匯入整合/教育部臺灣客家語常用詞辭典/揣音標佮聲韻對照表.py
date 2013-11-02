from 字詞組集句章.音標系統.客話.臺灣客家話拼音 import 臺灣客家話拼音聲母對照表
from 字詞組集句章.音標系統.客話.臺灣客家話拼音 import 臺灣客家話拼音韻母對照表
from 字詞組集句章.基本元素.公用變數 import 標點符號

class 音標佮聲韻對照表:
	檔案 = '/home/Ihc/音標對照'
	def __init__(self):
		輸出 = open(self.檔案, 'w')
		for 聲 in 臺灣客家話拼音聲母對照表:
			for 韻 in 臺灣客家話拼音韻母對照表:
				print(聲 + 韻, 聲, 韻, file = 輸出)
		print('si9', 's', 'i', file = 輸出)
		無聲標仔 = 'sil'
		print(無聲標仔, 無聲標仔, file = 輸出)
# 		for 符 in 標點符號:
# 			print(符, 無聲標仔, file = 輸出)


if __name__ == '__main__':
	音標佮聲韻對照表()
