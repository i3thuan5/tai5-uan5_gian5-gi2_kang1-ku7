# -*- coding: utf-8 -*-
import itertools
from math import log10
import os
from unittest.case import TestCase


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.語言模型.KenLM語言模型 import KenLM語言模型
'''
甲乙丙
數量=C(丙), C(乙丙), C(甲乙丙)
機率=P(丙), P(乙丙), P(甲乙丙)
條件=P(丙), P(乙丙)/P(乙), P(甲乙丙)/P(甲乙)
'''


class KenLM語言模型單元試驗(TestCase):
    忍受 = 1e-7

    def setUp(self):
        self.分析器 = 拆文分析器()
        '''
		srilm的結果
		原本檔案sui2：
		sui2 sui2 khiau2 tsiang5
		走ngram-count -order 3 -text sui2 -lm sui.lm：
		結果sui.lm：
		\data\
		ngram 1=5
		ngram 2=5
		ngram 3=0
		
		\1-grams:
		-0.69897	</s>
		-99	<s>	-99
		-0.69897	khiau2	-99
		-0.39794	sui2	-7.083871
		-0.69897	tsiang5	-99
		
		\2-grams:
		0	<s> sui2
		0	khiau2 tsiang5
		-0.30103	sui2 khiau2
		-0.30103	sui2 sui2
		0	tsiang5 </s>
		
		\3-grams:
		
		\end\
		'''
        self.媠媠巧靚連詞 = KenLM語言模型(
                os.path.join(os.path.dirname(os.path.abspath(__file__)), '語料', 'sui2.lm'))
        self.媠媠巧靚組物件 = self.分析器.建立組物件('sui2 sui2 khiau2 tsiang5')

    def tearDown(self):
        pass

    def test_媠媠巧靚_評詞陣列分(self):
        self.assertEqual(self.媠媠巧靚連詞.上濟詞數(), 3)
        self.陣列比較(list(self.媠媠巧靚連詞.評詞陣列分(self.媠媠巧靚組物件.內底詞)),
                [log10(2 / 5), log10(1 / 2), log10(1 / 2), -0.0], self.忍受)
        self.陣列比較(list(self.媠媠巧靚連詞.評詞陣列分(self.媠媠巧靚組物件.內底詞, 開始的所在=1)),
                [log10(1 / 2), log10(1 / 2), -0.0], self.忍受)

    def test_媠媠巧靚_評分(self):
        self.assertEqual(self.媠媠巧靚連詞.上濟詞數(), 3)
        self.陣列比較(list(self.媠媠巧靚連詞.評分(self.媠媠巧靚組物件)),
                [-0.0, log10(1 / 2), log10(1 / 2), -0.0, -0.0], self.忍受)

    def 陣列比較(self, 結果陣列, 答案陣列, 範圍):
        for 結果, 答案 in itertools.zip_longest(結果陣列, 答案陣列):
            self.assertAlmostEqual(結果, 答案, delta=範圍)
