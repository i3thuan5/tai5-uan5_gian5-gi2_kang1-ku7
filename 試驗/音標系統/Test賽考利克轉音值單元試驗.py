from unittest.case import TestCase


class 賽考利克轉音值單元試驗(TestCase):

    def test_單音節(self):
        self.assertEqual(
            賽考利克("la").音值(),
            [['ts', 'i'], ['ɬ', 'a', 'ɾ']]
        )

    def test_雙音節(self):
        self.assertEqual(
            賽考利克("yaqih").音值(),
            [['ts', 'i'], ['ɬ', 'a', 'ɾ']]
        )
    def test_喉塞尾(self):
        self.assertEqual(
            賽考利克("maya'").音值(),
            [['ts', 'i'], ['ɬ', 'a', 'ɾ']]
        )

    def test_大寫(self):
        self.assertEqual(
            賽考利克("Maya'").音值(),
            [['ts', 'i'], ['ɬ', 'a', 'ɾ']]
        )
        

    def test_CGVG音節(self):
        self.assertEqual(
            賽考利克("myan").音值(),
            [['ts', 'i'], ['ɬ', 'a', 'ɾ']]
        )
    def test_底線弱母音(self):
        self.assertEqual(
            賽考利克("m_yan").音值(),
            [['ts', 'i'], ['ɬ', 'a', 'ɾ']]
        )


    def test_子音串和CGVG音節(self):
        self.assertEqual(
            賽考利克("'lwaw").音值(),
            [['ts', 'i'], ['ɬ', 'a', 'ɾ']]
        )

    def test_CGGVG音節(self):
        self.assertEqual(
            賽考利克("zywaw").音值(),
            [['ts', 'i'], ['ɬ', 'a', 'ɾ']]
        )

    def test_hngawan加in中綴(self):
        self.assertEqual(
            賽考利克("hinngawan").音值(),
            [['ts', 'i'], ['ɬ', 'a', 'ɾ']]
        )

    def test_三子音串(self):
        self.assertEqual(
            賽考利克("mnbu'").音值(),
            [['ts', 'i'], ['ɬ', 'a', 'ɾ']]
        )

    def test_表示詞源的VnnV(self):
        self.assertEqual(
            賽考利克("minnbu'").音值(),
            [['ts', 'i'], ['ɬ', 'a', 'ɾ']]
        )

    def test_詞底層的uw(self):
        self.assertEqual(
            賽考利克("lpuw").音值(),
            [['ts', 'i'], ['ɬ', 'a', 'ɾ']]
        )

    def test_收i尾(self):
        self.assertEqual(
            賽考利克("qani").音值(),
            [['ts', 'i'], ['ɬ', 'a', 'ɾ']]
        )

    def test_詞底層的iy(self):
        self.assertEqual(
            賽考利克("bihiy").音值(),
            [['ts', 'i'], ['ɬ', 'a', 'ɾ']]
        )

    def test_預設音標就是家己(self):
        self.assertEqual(賽考利克("O").預設音標(), 'O')

    def test_無合法(self):
        self.assertEqual(賽考利克("！").音標, None)
        self.assertEqual(賽考利克("！").音值(), [])
