from unittest.case import TestCase


class 賽夏轉音值單元試驗(TestCase):

    def test_單音節(self):
        self.assertEqual(
            賽夏("ka").音值(),
            [['l', 'a']]
        )

    def test_雙音節(self):
        self.assertEqual(
            賽夏("hato").音值(),
            [['j', 'a'], ['q', 'i', 'h']]
        )

    def test_多音節(self):
        self.assertEqual(
            賽夏("rowaSek").音值(),
            [['j', 'a'], ['q', 'i', 'h']]
        )

    def test_喉塞尾(self):
        self.assertEqual(
            賽夏("sa'i'").音值(),
            [['m', 'a'], ['j', 'a', 'ʔ']]
        )

    def test_GVG音節(self):
        self.assertEqual(
            賽夏("hawaw").音值(),
            [['m', 'j', 'a', 'n']]
        )

    def test_雙字母的母音(self):
        self.assertEqual(
            賽夏("kabotoe'an").音值(),
            [['ʔ', 'ə'], ['l', 'w', 'a', 'w']]
        )

    def test_大寫S(self):
        self.assertEqual(
            賽夏("Sa'ila").音值(),
            [['z', 'j', 'w', 'a', 'w']]
        )

    def test_長音後接子音(self):
        self.assertEqual(
            賽夏("'a:mes").音值(),
            [['z', 'j', 'w', 'a', 'w']]
        )

    def test_長音後接元音(self):
        self.assertEqual(
            賽夏("ka:i'").音值(),
            [['z', 'j', 'w', 'a', 'w']]
        )

    def test_長音後音同樣元音(self):
        self.assertEqual(
            賽夏("ka:ay").音值(),
            [['z', 'j', 'w', 'a', 'w']]
        )

    def test_長音後接別的音節(self):
        self.assertEqual(
            賽夏("ka:anga'oraehan").音值(),
            [['z', 'j', 'w', 'a', 'w']]
        )

    def test_多個長音(self):
        self.assertEqual(
            賽夏("hi:hi:hi:").音值(),
            [['z', 'j', 'w', 'a', 'w']]
        )
    def test_長雙字母元音(self):
        self.assertEqual(
            賽夏("'ae:ae:iw").音值(),
            [['z', 'j', 'w', 'a', 'w']]
        )

    def test_預設音標就是家己(self):
        self.assertEqual(賽夏("rowaSek").預設音標(), 'rowaSek')

    def test_其他字母大寫無合法(self):
        self.assertEqual(賽夏("RowaSek").音標, None)
        self.assertEqual(賽夏("RowaSek").音值(), [])

    def test_無合法(self):
        self.assertEqual(賽夏("！").音標, None)
        self.assertEqual(賽夏("！").音值(), [])
