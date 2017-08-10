from unittest.case import TestCase, skip
from 臺灣言語工具.音標系統.Atayal.賽考利克 import 賽考利克


class 賽考利克轉音值單元試驗(TestCase):

    def test_單音節(self):
        self.assertEqual(
            賽考利克("la").音值(),
            [['l', 'a']]
        )

    def test_雙音節(self):
        self.assertEqual(
            賽考利克("yaqih").音值(),
            [['j', 'a'], ['q', 'i', 'h']]
        )

    def test_喉塞尾(self):
        self.assertEqual(
            賽考利克("maya'").音值(),
            [['m', 'a'], ['j', 'a', 'ʔ']]
        )

    def test_大寫(self):
        self.assertEqual(
            賽考利克("Maya'").音值(),
            [['m', 'a'], ['j', 'a', 'ʔ']]
        )

    def test_CGVG音節(self):
        self.assertEqual(
            賽考利克("myan").音值(),
            [['m', 'j', 'a', 'n']]
        )

    def test_底線弱母音(self):
        self.assertEqual(
            賽考利克("m_yan").音值(),
            [['m', 'ə'], ['j', 'a', 'n']]
        )

    def test_n佮g(self):
        self.assertEqual(
            賽考利克("n_gaw").音值(),
            [['n', 'ə'], ['ɣ', 'a', 'w']]
        )

    def test_子音串和CGVG音節(self):
        self.assertEqual(
            賽考利克("'lwaw").音值(),
            [['ʔ', 'ə'], ['l', 'w', 'a', 'w']]
        )

    def test_CGGVG音節(self):
        self.assertEqual(
            賽考利克("zywaw").音值(),
            [['z', 'j', 'w', 'a', 'w']]
        )

    def test_hngawan加in中綴(self):
        self.assertEqual(
            賽考利克("hinngawan").音值(),
            [['h', 'i', 'n'], ['ŋ', 'a'], ['w', 'a', 'n']]
        )

    def test_三子音串(self):
        self.assertEqual(
            賽考利克("mnbu'").音值(),
            [['m', 'ə'], ['n', 'ə'], ['β', 'u', 'ʔ']]
        )

    def test_表示詞源的nnV(self):
        self.assertEqual(
            賽考利克("minnbu'").音值(),
            [['m', 'i', 'n'], ['n', 'ə'], ['β', 'u', 'ʔ']]
        )

    @skip('-u佮-uw差佇佗？')
    def test_詞底層的uw(self):
        self.assertEqual(
            賽考利克("lpuw").音值(),
            [['l', 'ə'], ['p', 'u']]
        )

    def test_收i尾(self):
        self.assertEqual(
            賽考利克("qani").音值(),
            [['q', 'a'], ['n', 'i']]
        )

    @skip('-iy佮-i差佇佗？')
    def test_詞底層的iy(self):
        self.assertEqual(
            賽考利克("bihiy").音值(),
            [['β', 'i'], ['h', 'i']]
        )

    def test_預設音標就是家己(self):
        self.assertEqual(賽考利克("O").預設音標(), 'O')

    def test_無合法(self):
        self.assertEqual(賽考利克("！").音標, None)
        self.assertEqual(賽考利克("！").音值(), [])
