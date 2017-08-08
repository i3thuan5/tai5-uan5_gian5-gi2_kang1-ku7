from unittest.case import TestCase
from 臺灣言語工具.音標系統.Bunun.Bubukun import Bubukun


class Bubukun轉音值單元試驗(TestCase):

    def test_單元音(self):
        self.assertEqual(
            Bubukun("baak").音值(),
            [['b', 'a:', 'k']]
        )

    def test_雙元音(self):
        self.assertEqual(
            Bubukun("mais").音值(),
            [['m', 'a', 'i', 's']]
        )

    def test_雙音節短元音(self):
        self.assertEqual(
            Bubukun("tuza").音值(),
            [['t', 'u'], ['z', 'a']]
        )

    def test_雙音節長元音(self):
        self.assertEqual(
            Bubukun("tuzaa").音值(),
            [['t', 'u'], ['z', 'a:']]
        )

    def test_多音節(self):
        self.assertEqual(
            Bubukun("adasun").音值(),
            [['a'], ['d', 'a'], ['s', 'u', 'n']]
        )

    def test_元音分開(self):
        self.assertEqual(
            Bubukun("a-apnum").音值(),
            [['a'], ['a', 'p'], ['n', 'u', 'm']]
        )

    def test_音節分開(self):
        self.assertEqual(
            Bubukun("cinus-uvaazan").音值(),
            [['c', 'i'], ['n', 'u', 's'], ['u'], ['v', 'a:'], ['z', 'a', 'n']]
        )

    def test_預設音標就是家己(self):
        self.assertEqual(Bubukun("iskaan").預設音標(), 'iskaan')

    def test_無合法(self):
        拼音 = Bubukun("iskaan！")
        self.assertIsNone(拼音.音標)
        self.assertEqual(拼音.音值(), [])
