
class 產生字音字形檔案:
	標 = ['號,題目,答案']
	def 產生(self, 配對, 欄 = 2, 換頁逝 = 15):
		一頁幾个 = 欄 * 換頁逝
		這頁 = []
		for 所在 in range(0, len(配對), 一頁幾个):
			這頁.append(','.join(self.標 * 欄))
			for 第幾逝 in range(換頁逝):
				這逝 = []
				for 第幾欄 in range(欄):
					編號 = 所在 + 第幾欄 * 換頁逝 + 第幾逝
					if 編號 < len(配對):
						題目, 解答 = 配對[編號]
						這逝.append(str(編號 + 1))
						這逝.append(題目)
						這逝.append(解答)
					else:
						這逝.append('')
						這逝.append('')
						這逝.append('')
				這頁.append(','.join(這逝))
		return '\n'.join(這頁)

if __name__ == '__main__':
	字音字形檔案 = 產生字音字形檔案()
	配對 = []
	for 編號 in range(47):
		配對.append(('我' + str(編號), 'gua2 ' + str(編號)))
	結果 = 字音字形檔案.產生(配對)
	檔案 = open('/home/ihc/aa.cvs', 'w')
	檔案.write(結果)
