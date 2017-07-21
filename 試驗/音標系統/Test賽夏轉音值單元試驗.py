from unittest.case import TestCase, skip
from 臺灣言語工具.音標系統.SaySiyat.賽夏 import 賽夏


class 賽夏轉音值單元試驗(TestCase):

    def test_單音節(self):
        self.assertEqual(
            賽夏("ka").音值(),
            [['k', 'a']]
        )

    def test_雙音節(self):
        self.assertEqual(
            賽夏("hato").音值(),
            [['h', 'a'], ['t', 'o']]
        )

    def test_多音節(self):
        self.assertEqual(
            賽夏("lomaliw").音值(),
            [['l', 'o'], ['m', 'a'], ['l', 'i', 'w']]
        )

    def test_書寫CowV實際上是CwV(self):
        self.assertEqual(
            賽夏("rowaSek").音值(),
            [['r', 'w', 'a'], ['ʃ', 'e', 'k']]
        )

    def test_書寫CiyV實際上是CyV(self):
        self.assertEqual(
            賽夏("ngiyaw").音值(),
            [['ŋ', 'j', 'a', 'w']]
        )

    def test_喉塞尾(self):
        self.assertEqual(
            賽夏("sa'i'").音值(),
            [['s', 'a'], ['ʔ', 'i', 'ʔ']]
        )

    def test_GVG音節(self):
        self.assertEqual(
            賽夏("hawaw").音值(),
            [['h', 'a'], ['w', 'a', 'w']]
        )

    @skip('猶未揣著完整的規範')
    def test_wow音節(self):
        self.assertEqual(
            賽夏("bawow").音值(),
            [['β', 'a'], ['w', 'o', 'w']]
        )

    def test_雙字母的母音(self):
        self.assertEqual(
            賽夏("kabotoe'an").音值(),
            [['k', 'a'], ['β', 'o'], ['t', 'œ'], ['ʔ', 'a', 'n']]
        )

    def test_大寫S開頭(self):
        self.assertEqual(
            賽夏("Sa'ila").音值(),
            [['ʃ', 'a', ], ['ʔ', 'i'], ['l', 'a']]
        )

    def test_其他字母大寫無合法(self):
        拼音 = 賽夏("RowaSek")
        self.assertIsNone(拼音.音標)
        self.assertEqual(拼音.音值(), [])

    @skip('長元音猶未揣著完整的規範')
    def test_冒號後同元音代表同一音節_接子音(self):
        self.assertEqual(
            賽夏("ra:am").音值(),
            [['r', 'a:', 'm']]
        )

    @skip('長元音猶未揣著完整的規範')
    def test_冒號後同元音代表同一音節_接滑音(self):
        self.assertEqual(
            賽夏("ka:ay").音值(),
            [['k', 'a:', 'j']]
        )

    @skip('長元音猶未揣著完整的規範')
    def test_冒號後同元音代表同一音節_接下一個音節的子音(self):
        self.assertEqual(
            賽夏("ka:anga'oraehan").音值(),
            [
                ['k', 'a:'], ['ŋ', 'a'],
                ['ʔ', 'o'], ['r', 'æ'], ['h', 'a', 'n']
            ]
        )

    @skip('長元音猶未揣著完整的規範')
    def test_冒號後不同元音代表同一音節的滑音(self):
        self.assertEqual(
            賽夏("ka:i'").音值(),
            [['k', 'a:', 'j', 'ʔ']]
        )

    @skip('長元音猶未揣著完整的規範')
    def test_冒號後接子音代表和下一個音節中有停頓(self):
        self.assertEqual(
            賽夏("ra:ma'").音值(),
            [['r', 'a', 'L'], ['m', 'a', 'ʔ']]
        )

    @skip('長元音猶未揣著完整的規範')
    def test_多個長音(self):
        self.assertEqual(
            賽夏("hi:hi:hi:").音值(),
            [['h', 'i', 'L'], ['h', 'i', 'L'], ['h', 'i:']]
        )

    @skip('長元音猶未揣著完整的規範')
    def test_雙字母長元音(self):
        self.assertEqual(
            賽夏("'ae:ae:iw").音值(),
            [['ʔ', 'æ:'], ['æ:'], ['i', 'w']]
        )

    @skip('長元音猶未揣著完整的規範')
    def test_長音後的iy尾(self):
        '其他狀況下不會出現iy尾'
        self.assertEqual(
            賽夏("ra:iy").音值(),
            [['r', 'a:', 'j']]
        )

    @skip('長元音猶未揣著完整的規範')
    def test_長音後的元音是下一個音節的滑音(self):
        'iy在長音後，也是代表一個滑音y'
        self.assertEqual(
            賽夏("rina:iyan").音值(),
            [['r', 'i'], ['n', 'a:'], ['j', 'a', 'n']]
        )

    @skip('長元音猶未揣著完整的規範')
    def test_加拉灣(self):
        self.assertEqual(
            賽夏("lala:ai'").音值(),
            [['l', 'a'], ['l', 'a:'], ['i', 'ʔ']]
        )

    def test_預設音標就是家己(self):
        self.assertEqual(賽夏("rowaSek").預設音標(), 'rowaSek')

    def test_無合法(self):
        拼音 = 賽夏("a！")
        self.assertIsNone(拼音.音標)
        self.assertEqual(拼音.音值(), [])
