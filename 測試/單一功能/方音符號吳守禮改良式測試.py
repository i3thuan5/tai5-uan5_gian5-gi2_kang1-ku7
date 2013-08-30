import unittest
from 方音符號吳守禮改良式 import 方音符號吳守禮改良式

class 方音符號吳守禮改良式測試(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	
	def test_零聲母聲韻調輕(self):
		方音=方音符號吳守禮改良式('ainn7')
		self.assertEqual(方音.音標, 'ㆮ˫')
		self.assertEqual(方音.聲, '')
		self.assertEqual(方音.韻, 'ㆮ')
		self.assertEqual(方音.調, '˫')
# 		self.assertEqual(方音.輕, '')
		
	def test_完整聲韻調輕(self):
		方音=方音符號吳守禮改良式('sih')
		self.assertEqual(方音.音標, 'ㄒㄧㆷ')
		self.assertEqual(方音.聲, 'ㄒ')
		self.assertEqual(方音.韻, 'ㄧㆷ')
		self.assertEqual(方音.調, '')
# 		self.assertEqual(方音.輕, '')
		
	def test_韻化輔音聲韻調輕(self):
		方音=方音符號吳守禮改良式('ng5')
		self.assertEqual(方音.音標, 'ㆭˊ')
		self.assertEqual(方音.聲, '')
		self.assertEqual(方音.韻, 'ㆭ')
		self.assertEqual(方音.調, 'ˊ')
# 		self.assertEqual(方音.輕, '')
		
	def test_語法輕聲聲韻調輕(self):
		方音=方音符號吳守禮改良式('0e5')
		self.assertEqual(方音.音標, '˙ㆤ')
		self.assertEqual(方音.聲, '')
		self.assertEqual(方音.韻, 'ㆤ')
		self.assertEqual(方音.調, '˙')
# 		self.assertEqual(方音.輕, '0')
		
	def test_定看音標(self):
		self.assertEqual(方音符號吳守禮改良式('e').音標, 'ㆤ')
		self.assertEqual(方音符號吳守禮改良式('e1').音標, 'ㆤ')
		self.assertEqual(方音符號吳守禮改良式('be2').音標, 'ㆠㆤˋ')
		self.assertEqual(方音符號吳守禮改良式('ang3').音標, 'ㄤ˪')
		self.assertEqual(方音符號吳守禮改良式('mng5').音標, 'ㄇㆭˊ')
		self.assertEqual(方音符號吳守禮改良式('ainn7').音標, 'ㆮ˫')
		self.assertEqual(方音符號吳守禮改良式('ang9').音標, 'ㄤ^')
		
	def test_入聲(self):
		self.assertEqual(方音符號吳守禮改良式('Pih4').音標, 'ㄅㄧㆷ')
		self.assertEqual(方音符號吳守禮改良式('Pih8').音標, 'ㄅㄧ㆐ㆷ')
		self.assertEqual(方音符號吳守禮改良式('Pih10').音標, 'ㄅㄧㆷ㆐')
		
	def test_舌尖顎化(self):
		self.assertEqual(方音符號吳守禮改良式('tsa').音標, 'ㄗㄚ')
		self.assertEqual(方音符號吳守禮改良式('tsia').音標, 'ㄐㄧㄚ')
		self.assertEqual(方音符號吳守禮改良式('tsha').音標, 'ㄘㄚ')
		self.assertEqual(方音符號吳守禮改良式('tshia').音標, 'ㄑㄧㄚ')
		self.assertEqual(方音符號吳守禮改良式('sa').音標, 'ㄙㄚ')
		self.assertEqual(方音符號吳守禮改良式('sia').音標, 'ㄒㄧㄚ')
		self.assertEqual(方音符號吳守禮改良式('ja').音標, 'ㆡㄚ')
		self.assertEqual(方音符號吳守禮改良式('jia').音標, 'ㆢㄧㄚ')

	def test_輕聲(self):
		self.assertEqual(方音符號吳守禮改良式('ta0').音標, '˙ㄉㄚ')
		self.assertEqual(方音符號吳守禮改良式('pih0').音標, '˙ㄅㄧㆷ')

	def test_語法輕聲(self):
		self.assertEqual(方音符號吳守禮改良式('0a').音標, '˙ㄚ')
		self.assertEqual(方音符號吳守禮改良式('0e5').音標, '˙ㆤ')
		self.assertEqual(方音符號吳守禮改良式('0hannh').音標, '˙ㄏㆩㆷ')
		self.assertEqual(方音符號吳守禮改良式('0tsi̍t').音標, '˙ㄐㄧㆵ')

	def test_罕用音標(self):
		self.assertEqual(方音符號吳守禮改良式('tor').音標, 'ㄉㄛ')
		self.assertEqual(方音符號吳守禮改良式('kee5').音標, 'ㄍㄝˊ')
		self.assertEqual(方音符號吳守禮改良式('ter5').音標, 'ㄉㄮˊ')
		self.assertEqual(方音符號吳守禮改良式('tere5').音標, 'ㄉㄮㆤˊ')
		self.assertEqual(方音符號吳守禮改良式('tir5').音標, 'ㄉㆨˊ')

	def test_違法音標(self):
		self.assertEqual(方音符號吳守禮改良式('@@').音標, None)
		self.assertEqual(方音符號吳守禮改良式('pe̍m').音標, None)
		self.assertEqual(方音符號吳守禮改良式('xxtsé--á').音標, None)
		self.assertEqual(方音符號吳守禮改良式('óonn').音標, None)

if __name__ == '__main__':
	unittest.main()
