from unittest.case import TestCase


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
            賽夏("rowaSek").音值(),
            [['r', 'o'], ['w', 'a'], ['ʃ', 'e', 'k']]
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

    def test_雙字母的母音(self):
        self.assertEqual(
            賽夏("kabotoe'an").音值(),
            [['k', 'a'], ['b', 'o'], ['t', 'œ'], ['ʔ', 'a', 'n']]
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

    def test_長音後接子音(self):
        self.assertEqual(
            賽夏("ra:am").音值(),
            [['r', 'a:'], ['a', 'm']]
        )

    def test_長音後接別音節子音(self):
        self.assertEqual(
            賽夏("ra:ma'").音值(),
            [['r', 'a:'], ['m', 'a', 'ʔ']]
        )

    def test_長音後接元音(self):
        self.assertEqual(
            賽夏("ka:i'").音值(),
            [['k', 'a:'], ['i', 'ʔ']]
        )

    def test_長音後音同樣元音(self):
        self.assertEqual(
            賽夏("ka:ay").音值(),
            [['k', 'a:'], ['a', 'j']]
        )

    def test_長音後接別的音節(self):
        self.assertEqual(
            賽夏("ka:anga'oraehan").音值(),
            [
                ['k', 'a:'], ['a'], ['ŋ', 'a'],
                ['ʔ', 'o'], ['r', 'æ'], ['h', 'a', 'n']
            ]
        )

    def test_多個長音(self):
        self.assertEqual(
            賽夏("hi:hi:hi:").音值(),
            [['h', 'i:'], ['h', 'i:'], ['h', 'i:']]
        )

    def test_長雙字母元音(self):
        self.assertEqual(
            賽夏("'ae:ae:iw").音值(),
            [['ʔ', 'æ:'], ['æ:'], ['i', 'w']]
        )

    def test_預設音標就是家己(self):
        self.assertEqual(賽夏("rowaSek").預設音標(), 'rowaSek')

    def test_無合法(self):
        拼音 = 賽夏("！")
        self.assertIsNone(拼音.音標)
        self.assertEqual(拼音.音值(), [])
