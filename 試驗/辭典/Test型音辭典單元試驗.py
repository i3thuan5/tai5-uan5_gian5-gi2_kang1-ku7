# -*- coding: utf-8 -*-
from unittest.case import TestCase


from 試驗.辭典.辭典單元試驗 import 辭典單元試驗
from 臺灣言語工具.辭典.型音辭典 import 型音辭典


class 型音辭典單元試驗(辭典單元試驗, TestCase):
    辭典型態 = 型音辭典
