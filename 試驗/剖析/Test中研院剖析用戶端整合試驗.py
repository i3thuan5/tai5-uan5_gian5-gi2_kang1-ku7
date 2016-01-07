# -*- coding: utf-8 -*-
import unittest


from 臺灣言語工具.剖析.中研院.剖析用戶端 import 剖析用戶端


class 中研院剖析用戶端整合試驗(unittest.TestCase):
    def setUp(self):
        self.用戶端 = 剖析用戶端()

    def tearDown(self):
        pass

    def test_語句剖一句(self):
        self.assertEqual(self.用戶端.語句剖析做語句('我想吃飯'), [[
            '#1:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:吃飯))#',
        ]])

    def test_語句剖一逝字(self):
        self.assertEqual(self.用戶端.語句剖析做語句('我想吃飯。我想吃很多飯。'), [[
            '#1:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:吃飯))#。(PERIODCATEGORY)',
            '#2:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vt:吃|NP(DET:很多|Head:N:飯)))#。(PERIODCATEGORY)'],
        ])

    def test_語句剖兩逝字(self):
        self.assertEqual(self.用戶端.語句剖析做語句('我想吃飯。我想吃很多飯。\n我吃飽了。'), [[
            '#1:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:吃飯))#。(PERIODCATEGORY)',
            '#2:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vt:吃|NP(DET:很多|Head:N:飯)))#。(PERIODCATEGORY)',
        ], [
            '#1:1.[0] S(NP(Head:N:我)|Head:Vi:吃飽|T:了)#。(PERIODCATEGORY)',
        ],
        ])

    def test_語句剖濟逝字(self):
        self.assertEqual(self.用戶端.語句剖析做語句('\n\n我想吃飯。我想吃很多飯。\n\n  \n\n  　 \n\n我吃飽了。\n\n'), [[
            '#1:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vi:吃飯))#。(PERIODCATEGORY)',
            '#2:1.[0] S(NP(Head:N:我)|Head:Vt:想|VP(Head:Vt:吃|NP(DET:很多|Head:N:飯)))#。(PERIODCATEGORY)',
        ], [
            '#1:1.[0] S(NP(Head:N:我)|Head:Vi:吃飽|T:了)#。(PERIODCATEGORY)',
        ],
        ])

    def test_語句剖著大於符號(self):
        self.assertEqual(self.用戶端.語句剖析做語句('我想) :>'), [[
            '#1:1.[0] %(NP(Head:N:我)|Vt:想|COLONCATEGORY::)#&gt;(PARENTHESISCATEGORY)',
        ]])

    def test_語句剖著小於符號是空的(self):
        self.assertEqual(self.用戶端.語句剖析做語句('我想) :<'), [[
        ]])
