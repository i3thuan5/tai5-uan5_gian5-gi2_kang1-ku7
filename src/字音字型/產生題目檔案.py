
from simpleodspy.sodsspreadsheet import SodsSpreadSheet
from simpleodspy.sodscsv import SodsCsv
from simpleodspy.sodsxml import SodsXml
from simpleodspy.sodshtml import SodsHtml
from simpleodspy.sodsxlsx import SodsXlsx

class 產生字音字形檔案:
	標 = ['號', '題目', '答案']
	def 產生無引號csv(self, 配對, 欄 = 2, 換頁逝 = 15):
		資料 = self.產生資料(配對, 欄, 換頁逝)
		這頁 = []
		for 這逝 in 資料:
			這頁.append(','.join(這逝))
		return '\n'.join(這頁)
	def 產生csv(self, 配對, 欄 = 2, 換頁逝 = 15):
		表=self.產生sods(配對, 欄, 換頁逝)
		檔 = SodsCsv(表)
		return 檔.exportCsv()
	def 產生xml(self, 配對, 欄 = 2, 換頁逝 = 15):
		表=self.產生sods(配對, 欄, 換頁逝)
		檔 = SodsXml(表)
		return 檔.exportXml()
	def 產生html(self, 配對, 欄 = 2, 換頁逝 = 15):
		表=self.產生sods(配對, 欄, 換頁逝)
		檔 = SodsHtml(表)
		return 檔.exportHtml()
	def 產生sods(self, 配對, 欄 = 2, 換頁逝 = 15):
		資料 = self.產生資料(配對, 欄, 換頁逝)
		表 = SodsSpreadSheet(len(資料) + 1, len(self.標) * 欄 + 1)
		這馬逝 = 1
		for 一逝 in 資料:
			for 所在 in range(len(一逝)):
				座標 = 表.encodeColName(所在 + 1) + str(這馬逝)
				表.setValue(座標, 一逝[所在])
				表.setStyle(座標,
					border_top = "1pt solid #000000",
					border_bottom = "1pt solid #000000",
					border_left = "1pt solid #000000",
					border_right = "1pt solid #000000",)
			這馬逝 += 1
		return 表
	def 產生資料(self, 配對, 欄 = 2, 換頁逝 = 15):
		一頁幾个 = 欄 * 換頁逝
		這頁 = []
		for 所在 in range(0, len(配對), 一頁幾个):
			這頁.append(self.標 * 欄)
			for 第幾逝 in range(換頁逝):
				這逝 = []
				for 第幾欄 in range(欄):
					編號 = 所在 + 第幾欄 * 換頁逝 + 第幾逝
					if 編號 < len(配對):
						題目, 解答 = 配對[編號]
						這逝.append('_' + str(編號 + 1) + '_')
						這逝.append(題目)
						這逝.append(解答)
					else:
						這逝.append('')
						這逝.append('')
						這逝.append('')
				這頁.append(這逝)
		return 這頁


if __name__ == '__main__':
	字音字形檔案 = 產生字音字形檔案()
	配對 = []
	for 編號 in range(47):
		配對.append(('我' + str(編號), 'gua2 ' + str(編號)))
		
	open('/home/ihc/aa-bo5.csv', 'w').write(字音字形檔案.產生無引號csv(配對))
	open('/home/ihc/aa.csv', 'w').write(字音字形檔案.產生csv(配對))
	open('/home/ihc/aa.xml', 'w').write(字音字形檔案.產生xml(配對))
	open('/home/ihc/aa.html', 'w').write(字音字形檔案.產生html(配對))
#	表=字音字形檔案.產生sods(配對)
#	檔 = SodsXlsx(表)
#	檔.save('/home/ihc/aa.xlsx')
#	open('/home/ihc/aa.xlsx', 'w').write(字音字形檔案.產生xlsx(配對))

