# -*- coding: utf-8 -*-
'''
Created on 2013/9/22

@author: Ihc
'''
from 臺灣言語工具.基本物件.字 import 字
from 臺灣言語工具.基本物件.詞 import 詞
from 臺灣言語工具.基本物件.組 import 組
from 臺灣言語工具.基本物件.集 import 集
from 臺灣言語工具.基本物件.句 import 句
from 臺灣言語工具.基本物件.章 import 章
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤


class 程式掠漏:
    @classmethod
    def 毋是字物件就毋著(cls, 字物件):
        if not isinstance(字物件, 字):
            raise 型態錯誤('傳入來的毋是字物件：{0},{1}'
                       .format(type(字物件), str(字物件)))

    @classmethod
    def 毋是詞物件就毋著(cls, 詞物件):
        if not isinstance(詞物件, 詞):
            raise 型態錯誤('傳入來的毋是詞物件：{0},{1}'
                       .format(type(詞物件), str(詞物件)))

    @classmethod
    def 毋是組物件就毋著(cls, 組物件):
        if not isinstance(組物件, 組):
            raise 型態錯誤('傳入來的毋是組物件：{0},{1}'
                       .format(type(組物件), str(組物件)))

    @classmethod
    def 毋是集物件就毋著(cls, 集物件):
        if not isinstance(集物件, 集):
            raise 型態錯誤('傳入來的毋是集物件：{0},{1}'
                       .format(type(集物件), str(集物件)))

    @classmethod
    def 毋是句物件就毋著(cls, 句物件):
        if not isinstance(句物件, 句):
            raise 型態錯誤('傳入來的毋是句物件：{0},{1}'
                       .format(type(句物件), str(句物件)))

    @classmethod
    def 毋是章物件就毋著(cls, 章物件):
        if not isinstance(章物件, 章):
            raise 型態錯誤('傳入來的毋是章物件：{0},{1}'
                       .format(type(章物件), str(章物件)))

    @classmethod
    def 毋是字詞組集句章的毋著(cls, 物件):
        raise 型態錯誤('傳入來的毋是字詞組集句章其中一種物件：{0}，{1}'
                   .format(type(物件), str(物件)))

    @classmethod
    def 毋是字串都毋著(cls, 語句):
        if not isinstance(語句, str):
            raise 型態錯誤('傳入來的語句毋是字串：{0}'.format(str(語句)))
