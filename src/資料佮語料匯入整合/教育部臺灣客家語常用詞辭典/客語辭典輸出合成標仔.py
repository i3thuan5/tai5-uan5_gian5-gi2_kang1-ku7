from 資料庫.資料庫連線 import 資料庫連線
from 資料佮語料匯入整合.教育部臺灣客家語常用詞辭典.客話辭典正規化 import 客話辭典正規化
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 字詞組集句章.解析整理工具.物件譀鏡 import 物件譀鏡
from 資料庫.欄位資訊 import 版本正常
from 資料庫.欄位資訊 import 字詞
from 資料庫.整合.整合入言語 import 加文字佮版本
from 資料佮語料匯入整合.教育部臺灣客家語常用詞辭典.調號處理 import 調號處理
from 資料庫.欄位資訊 import 客語
from 字詞組集句章.解析整理工具.轉物件音家私 import 轉物件音家私
from 資料庫.欄位資訊 import 四縣腔
from 資料庫.欄位資訊 import 海陸腔
from 資料庫.欄位資訊 import 大埔腔
from 資料庫.欄位資訊 import 饒平腔
from 資料庫.欄位資訊 import 詔安腔
from 字詞組集句章.基本元素.公用變數 import 標點符號
from 語音合成.合音檔.句物件轉合成標籤 import 句物件轉合成標籤
from 字詞組集句章.音標系統.客話.臺灣客家話拼音 import 臺灣客家話拼音
import os
import Pyro4


教育部客家語辭典名 = '教育部臺灣客家語常用詞辭典'
教育部客家語辭典地區 = '臺員'
教育部客家語辭典年代 = 100


揣全部資料 = 資料庫連線.prepare('SELECT "編號","詞目","詞性","四縣音","海陸音","大埔音","饒平音","詔安音","釋義","近義詞","反義詞","文白讀","又音","多音字","對應華語" FROM "教育部臺灣客家語常用詞辭典"."網頁資料"')


class 客語辭典輸出合成標仔():
	def __init__(self):
		# '無愛聲調' '愛聲調'　'全文'
		模式 = '全文'
		目標 = '/home/Ihc/research/labels' + 模式
		os.makedirs(目標, exist_ok = True)
		辭典正規化 = 客話辭典正規化()
		分析器 = 拆文分析器()
		全部資料 = 揣全部資料()
		譀鏡 = 物件譀鏡()
		轉音家私 = 轉物件音家私()
		調號 = 調號處理()
		Pyro4.config.SERIALIZER = 'pickle'
		標音工具 = Pyro4.Proxy("PYRONAME:內部自動標音")
		合成標籤工具 = 句物件轉合成標籤()
		def 初使音標(self, 音):
			self.音 = 音
		def 標準音標(self):
			return 調號.數字轉調號(self.音, self.腔)
		算 = 0
		for 編號, 詞目, 詞性, 四縣音, 海陸音, 大埔音, 饒平音, 詔安音, 釋義, 近義詞, 反義詞, \
				文白讀, 又音, 多音字, 對應華語 in 全部資料:
# 			if 編號!=1:
# 				continue
			for 音標, 腔, 頭 in [(四縣音, 四縣腔, 'si3'),
					 (海陸音, 海陸腔, 'hai2'), (大埔音, 大埔腔, 'tua7'),  # 粵臺片
					(饒平音, 饒平腔, 'phing5'), (詔安音, 詔安腔, 'an1')
					]:
				新音 = 辭典正規化.處理音標(音標)
				if 新音 != '':
					try:
						換音 = {'han113 fa53 rhid21 tai53 doi33 zhin53 gin33 mo113 rhid21 pied54':
						'han113 fa53 rhid21 tai53 doi33, zhin53 gin33 mo113 rhid21 pied54',
						'mang11 shid5 ng53 ngied5 zied2 zung53 o53 po55 m55 ho53 ngib5 vung53':
						'mang11 shid5 ng53 ngied5 zied2 zung53, o53 po55 m55 ho53 ngib5 vung53',
						'cai55 ga11 cien11 ngid24 hoo31 chid24 mun53 ban31 zhio11 nan53':
						'cai55 ga11 cien11 ngid24 hoo31, chid24 mun53 ban31 zhio11 nan53',
						'teu55 na55 cab2 vo55 chan53 liau55 diau11':
						'teu55 na55 cab2 vo55 chan53 －－ liau55 diau11',
						'uai33 zhoi53 choi33 lab54 ba31，rhid21 ton113 sia113 ki53':
						'uai33 zhoi53 choi33 lab54 ba31 －－ rhid21 ton113 sia113 ki53',
						'gung33 bud21 li113 po113 chin53 bud21 li113 to113':
						'gung33 bud21 li113 po113, chin53 bud21 li113 to113',
						'ho53 ma11 m55 shid5 shid5 fui55 teu55 co53':
						'ho53 ma11 m55 shid5 fui55 teu55 co53',
						'han113 fa53 rhid21 tai53 doi33 zhin53 gin33 mo113 rhid21 pied54':
						'han113 fa53 rhid21 tai53 doi33, zhin53 gin33 mo113 rhid21 pied54',
						}
						if 新音 in 換音:
# 							print('{0}\n{1}\n{2}\n音標改正：{3}'.
# 								format(編號, 詞目, 新音, 換音[新音]))
							新音 = 換音[新音]
							新詞目 = 詞目
						elif 詞目 == '時錶仔' and 新音 == 'shi55 biau24':
							新詞目 = '時錶'
						elif 詞目 == '磨刀仔' and 新音 == 'no55 do53':
							新詞目 = '磨刀'
						elif 詞目 == '紙炮仔' and 新音 == 'zhi24 pau11':
							新詞目 = '紙炮'
						elif 詞目 == '毆□死' and 新音 == 'eu55 bun11 gi55 si53':
							新詞目 = '毆分佢死'
						elif 詞目 == '竹馬仔' and 新音 == 'zhug5 ma53':
							新詞目 = '竹馬'
						elif 詞目 == '魚脯仔' and 新音 == 'ng55 pu24':
							新詞目 = '魚脯'
						elif 詞目 == '做粄仔' and 新音 == 'zo11 ban24':
							新詞目 = '做粄'
						elif 詞目 == '嫩葉仔' and 新音 == 'nun33 rhab2':
							新詞目 = '嫩葉'
						elif 詞目 == '茶壺仔' and 新音 == 'ca55 fu55':
							新詞目 = '茶壺'
						elif 詞目 == '嬰兒仔' and 新音 == 'o53 nga11':
							新詞目 = '嬰兒'
						elif 詞目 == '梅仔樹' and 新音 == 'moi55 shu33':
							新詞目 = '梅樹'
						elif 詞目 == '種痘仔' and 新音 == 'zhung11 teu33':
							新詞目 = '種痘'
						elif 詞目 == '送鬼仔' and 新音 == 'sung11 gui24':
							新詞目 = '送鬼'
						elif 詞目 == '頭臥臥仔' and 新音 == 'teu55 ngo11 ngo11':
							新詞目 = '頭臥臥'
						elif 詞目 == '時鐘仔' and 新音 == 'shi55 zhung53':
							新詞目 = '時鐘'
						else:
							新詞目 = 詞目
						新音 = 新音.replace('9', '31')
						for 符 in 標點符號:
							新音 = 新音.replace(符, ' sil ')
						句物件 = 分析器.產生對齊句(新詞目, 新音)
						腔型 = type('腔', (object,), {'__init__' : 初使音標, '腔':腔, '標準音標' :標準音標})
						新句物件 = 轉音家私.轉做標準音標(腔型, 句物件)
					except Exception as 錯誤:
						print('錯誤！！ {0}，{1}，{2}，{5}，原音標：{3}，{4}'.
							format(編號, 詞目, type(錯誤), 新音, 音標, 錯誤))
						算 += 1
# 					print(譀鏡.看型(句物件), 譀鏡.看音(句物件))
					else:
						輸出 = open(
							'{0}/{1}_{2:05}.lab'.format(目標, 頭, 編號), 'w')
						if 模式 == '無愛聲調':
							音 = 譀鏡.看音(句物件)
							音 = 音.replace('1', '')
							音 = 音.replace('2', '')
							音 = 音.replace('3', '')
							音 = 音.replace('4', '')
							音 = 音.replace('5', '')
							輸出.write('\n'.join(音.split()))
						elif 模式 == '愛聲調':
							音 = 譀鏡.看音(新句物件)
							輸出.write('\n'.join(音.split()))
						elif 模式 == '全文':
# 							print(腔)
							仝詞=新音.replace('  ',' ').replace('  ',' ').replace(' ','-')
							全文句物件=轉音家私.轉做標準音標(腔型,分析器.產生對齊句(新詞目, 仝詞))
# 							章物件 = 標音工具.斷詞標音物件(腔, 新句物件)
# 							標仔 = 合成標籤工具.句物件轉標籤(
# 								臺灣客家話拼音, 章物件)
							標仔 = 合成標籤工具.句物件轉標籤(
								臺灣客家話拼音, 全文句物件)
							輸出.write('\n'.join(標仔))
						else:
							raise RuntimeError('模式怪怪')
						輸出.write('\n')
# 						print(編號,譀鏡.看型(新句物件), 譀鏡.看音(句物件))
# 						print(教育部客家語辭典名, 字詞, 腔, 教育部客家語辭典地區,
# 									教育部客家語辭典年代, 譀鏡.看型(新句物件), 譀鏡.看音(新句物件), 版本正常)
# 						加文字佮版本(教育部客家語辭典名, 字詞, 腔, 教育部客家語辭典地區,
#  									教育部客家語辭典年代, 譀鏡.看型(新句物件), 譀鏡.看音(新句物件), 版本正常)
		print(算)
# [chhsueh@nol labels]$ sed -i 's/，/sil/g' *
# [chhsueh@nol labels]$ sed -i 's/；/sil/g' *
# [chhsueh@nol labels]$ sed -i 's/－/sil/g' *
# [chhsueh@nol labels]$ sed -i 's/。/sil/g' *
# [chhsueh@nol labels]$ sed -i -e 's/、/sil/g' -e 's/,/sil/g' *


if __name__ == '__main__':
	客語辭典輸出合成標仔()
