import os

class 切音結果佮標仔佮拼準備合成():
	def __init__(self):
		語料路徑='/home/Ihc/research/'
		切音結果路徑 = 語料路徑 + 'mono.final.result.mlf'
		標仔原本路徑=語料路徑+'labels全文/'
		切音標仔路徑=語料路徑+'labels/full/'
		單音標仔路徑=語料路徑+'labels/mono/'
		os.makedirs(切音標仔路徑, exist_ok = True)
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
						音檔碼=音檔名.split('.')[0][3:]+'.lab'
	# 					print(音檔碼)
						合成標籤=list(open(標仔原本路徑+音檔碼))
# 						if 模式=='愛聲調':
# 							合成標籤=['sil']+合成標籤+['sil']
	# 					print(len(切音標籤))
	# 					print(len(合成標籤))
# 						print((切音標籤))
# 						print((合成標籤))
						if len(切音標籤)!=len(合成標籤):
							print(音檔碼+'長度對袂齊')
						單音標仔=open(
							單音標仔路徑+音檔名.split('.')[0][3:]+
							'.lab','w')
						for i in range(len(切音標籤)):
	# 						print(切音標籤[i].split())
							切音=切音標籤[i].split()
							print(切音[0],切音[1],切音[2],file=單音標仔)
						單音標仔.close()
						合成聲韻標籤檔=open(
							切音標仔路徑+音檔名.split('.')[0][3:]+
							'.lab','w')
						for i in range(len(切音標籤)):
	# 						print(切音標籤[i].split())
							切音=切音標籤[i].split()
							print(切音[0],切音[1],合成標籤[i].strip(),file=合成聲韻標籤檔)
						合成聲韻標籤檔.close()
						狀態='一開始'
					else:
						切音標籤.append(每行)
		else:
			print('檔案揣毋著矣')
	
if __name__ == '__main__':
	切音結果佮標仔佮拼準備合成()