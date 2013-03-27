from 言語資料庫.公用資料 import 組字式符號

class 文章標點處理工具:
	斷字符號 = ['-']
	標點符號 = None

	def 切開語句(self, 語句):
		切開結果 = []
		目前字串 = ''
		處理位置 = 0
		語句長度 = len(語句)
#		print(語句)
#		print(語句長度)
		while 處理位置 < 語句長度:
			for 音標長度 in range(3, 0, -1):
				一段 = 語句[處理位置:處理位置 + 音標長度]
				if 一段 in self.斷字符號:
					目前字串 += 語句[處理位置]
					處理位置 += 音標長度
					break
				elif 一段 in self.標點符號:
					#字佮普通的標點符號中央愛有空白
					if len(切開結果)>0 and 切開結果[-1]!=' ' and (目前字串!='' or 一段!=' '):
						切開結果.append('')
						切開結果.append(' ')
#						print(切開結果)
					切開結果.append(目前字串)
					#普通的標點符號頭前愛有空白
					if 目前字串!='' and 一段!=' ':
						切開結果.append(' ')
						切開結果.append('')
					目前字串 = ''
					切開結果.append(一段)
					處理位置 += 音標長度
					break
			else:
				目前字串 += 語句[處理位置]
				處理位置 += 1
		if 目前字串 != '':
			切開結果.append(目前字串)
		return 切開結果
	
	def 分離漢字(self, 語句):
		漢字陣列=[]
		一个漢字=''
		長度=0
		for 字 in 語句:
			一个漢字+=字
			if 字 in 組字式符號:
				長度-=2
			else:
				長度+=1		
			if 長度==1:
				漢字陣列.append(一个漢字)
				一个漢字=''
				長度=0
		return 漢字陣列
	
	def 計算漢字語句漢字數量(self, 語句):
		長度=0
		for 字 in 語句:
			if 字 in 組字式符號:
				長度-=2
			else:
				長度+=1
		return len(語句)
	
	def 計算音標語句音標數量(self, 語句):
		return len(語句.replace('--','-').split(self.斷字符號[0]))

if __name__ == '__main__':
	標點處理工具 = 文章標點處理工具()
	標點處理工具.標點符號 = {' ', '-', ',', '。', '、', '，',
	'「', '」', '(', ')', '；', '？', '『', '』', '【', '】', '！', '：', '"'}
	print(標點處理工具.切開語句('bin5-si7-sin1-bun5-po3-to7'))
	print(標點處理工具.切開語句('tsit8-ui7 tan5-sio2-tsia2 kap4 han5-kok4-tsik8 e5 ang1-sai3 tshut4-kok4 ，'))
	print(標點處理工具.切開語句('bo5-siunn7-tioh8 thong1-kuan1 tsa1-giam7 ho1u7-tsio3 e5 si5-tsun7 ，'))
	print(標點處理工具.切開語句('pi7 ko1-hiong5 sio2-kang2-ki1-tiunn5 e5 tsa1-giam7-uan5 suan1-tshio3 。'))
	print(標點處理工具.切開語句('kong2 i1 ke3-ho1u7 tsit8-e5 bun5-hua3 「 thau1-khioh4-tsia2 」 ，'))
	print(標點處理工具.切開語句('khi3-kah8 tan5-sio2-tsia2 tong1-tiunn5 lau5-bak8-sai2 tshi1-tsham2-khau3 ，'))
	print(標點處理工具.切開語句('tshin1-iu2 hiong3 bin5-si7 sin1-bun5-tai5 tau5-ue7 。'))
	print(標點處理工具.切開語句('king1-kue3 hiong3 iu2-kuan1-tan1-ui7 tsa1-tsing3 ，'))
	print(標點處理工具.切開語句('i5-bin5-su2 than2-sing5 tsa1-giam7-uan5 sit4-gian5 ，'))
	print(標點處理工具.切開語句('i2-king1 tiau3-li7 hian7-tsit4 gian2-gi2 tshu2-hun1 。'))
	print(標點處理工具.切開語句('Pang-liau5 hi5-kang2 「 Toa7-tiau5-hang7 」 siang7-khoah nng7-kong-chhioh'))
	print(標點處理工具.計算音標語句音標數量('kau2-chap8-lak8-hoe3'))


