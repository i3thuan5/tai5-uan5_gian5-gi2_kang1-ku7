from 毓哲語言辨識.第一點一步之檢查通用臺音標對照表 import 對齊語料路徑

元音 = ['a', 'i', 'u', 'e', 'o']
韻尾 = ['m', 'n', 'ng', 'h', 'p', 't', 'k']
鼻化韻 = ['nn', 'nnh']
if __name__ == '__main__':
	音表 = [line.strip().split()
		for line in open(對齊語料路徑 + '臺羅聲韻查通用音素.dic')]

# 	for 音 in 音表[:-1]:
# 		問題 = 'QS "Si7_' + 音[0] + '" {*-' + 音[0] + '+*}'
# 		print(問題)
# 
# 	for 音 in 韻尾:
# 		問題 = ('QS "Si7_' + 音 + '_Bue2' +
# 			'" {*-*?' + 音 + '+*}')
# 		print(問題)
# 	for 音 in 鼻化韻:
# 		問題 = ('QS "Si7_' + 音 + '_Bue2' +
# 			'" {*-*?' + 音 + '+*}')
# 		print(問題)
	
	for 音 in 音表[:-1]:
		問題 = 'QS "Si7_Tau5_' + 音[0] + '" {*' + 音[0] + '-*}'
		print(問題)

	for 音 in 韻尾:
		問題 = ('QS "Si7_Tau5_' + 音 + '_Bue2' +
			'" {*?' + 音 + '-*}')
		print(問題)
	for 音 in 鼻化韻:
		問題 = ('QS "Si7_Tau5_' + 音 + '_Bue2' +
			'" {*?' + 音 + '-*}')
		print(問題)
	
	for 音 in 音表[:-1]:
		問題 = 'QS "Si7_Bue2_' + 音[0] + '" {*+' + 音[0] + '/*}'
		print(問題)

	for 音 in 韻尾:
		問題 = ('QS "Si7_Bue2_' + 音 + '_Bue2' +
			'" {*+*?' + 音 + '/*}')
		print(問題)
	for 音 in 鼻化韻:
		問題 = ('QS "Si7_Bue2_' + 音 + '_Bue2' +
			'" {*+*?' + 音 + '/*}')
		print(問題)
