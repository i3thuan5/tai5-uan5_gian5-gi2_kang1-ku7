from 語音合成.第一步之臺羅轉合成標籤 import 臺羅轉合成標籤
from 毓哲語言辨識.第零步之處理標籤格式 import 語料路徑
from 毓哲切音結果產生合成標籤格式.第一步之揣出愛處理的臺詞 import 合成標籤路徑

if __name__ == '__main__':
	合成標籤工具 = 臺羅轉合成標籤()
	臺詞表={}
	臺詞路徑 = 合成標籤路徑 + "alltcp.tai5lo5"
	for 一逝 in open(臺詞路徑):
		臺詞碼,臺羅拼音=一逝.split()
		臺詞表[臺詞碼]=臺羅拼音
	切音結果路徑 = 語料路徑 + 'mono.final.result.mlf'
	合成聲韻標籤檔路徑=語料路徑+'label/high_score/mono/'
	合成完整標籤檔路徑=語料路徑+'label/high_score/full/'
	切音結果路徑 = 語料路徑 + 'mid_mono.final.result.mlf'
	合成聲韻標籤檔路徑=語料路徑+'label/mid_score/mono/'
	合成完整標籤檔路徑=語料路徑+'label/mid_score/full/'
# 	os.chdir(語料路徑+'labe')
	切音結果=open(切音結果路徑)
	if 切音結果.readline().strip()=='#!MLF!#':
		狀態='一開始'
		for 每行 in 切音結果.readlines():
			每行=每行.strip()
			if 狀態=='一開始':
				音檔名=每行
				切音標籤=[]
				狀態='切音資料'
			elif 狀態=='切音資料':
				if 每行=='.':
					音檔碼=音檔名.split('_')[0][3:]
# 					print(音檔碼)
					合成標籤,聲韻標籤=合成標籤工具.臺羅轉合成標籤佮聲韻資料(臺詞表[音檔碼])
# 					print(len(切音標籤))
# 					print(len(合成標籤))
# 					print((切音標籤))
# 					print((合成標籤))
# 					for i in range(min(len(切音標籤),len(合成標籤))):
# 						print(切音標籤[i].split(' ')[2],合成標籤[i].split('/')[0])
					if len(切音標籤)!=len(合成標籤) or len(切音標籤)!=len(聲韻標籤):
						print(音檔碼+'長度對袂齊')
					合成聲韻標籤檔=open(
						合成聲韻標籤檔路徑+音檔名.split('.')[0][3:]+
						'.lab','w')
					for i in range(len(切音標籤)):
# 						print(切音標籤[i].split())
						切音=切音標籤[i].split()
						print(切音[0],切音[1],切音[2],file=合成聲韻標籤檔)
					合成聲韻標籤檔.close()
					合成完整標籤檔=open(
						合成完整標籤檔路徑+音檔名.split('.')[0][3:]+
						'.lab','w')
					for i in range(len(切音標籤)):
						切音=切音標籤[i].split()
						print(切音[0],切音[1],合成標籤[i],file=合成完整標籤檔)
					合成聲韻標籤檔.close()
					狀態='一開始'
				else:
					切音標籤.append(每行)
	else:
		print('檔案揣毋著矣')
			
			