from 毓哲語言辨識.第零步之處理標籤格式 import 語料路徑

if __name__ == '__main__':
	import os
	佗一類 = 'high_score/'
	佗一類 = 'mid_score/'
	來源 = 語料路徑 + "wav/wav/" + 佗一類
	目標 = 語料路徑 + "wav/raw/" + 佗一類
	os.chdir(來源)
	for 檔名 in os.listdir(".")[:]:
		if 檔名.endswith(".wav"):
			輸出 = open(目標 + 檔名.replace('.wav', '.raw'), 'wb')
			with open(檔名, 'rb') as 輸入:
				位元組 = 輸入.read(44)
				位元組 = 輸入.read(1)
				while 位元組:
					輸出.write(位元組)
					位元組 = 輸入.read(1)
			輸出.close()
# 			print(檔名)
