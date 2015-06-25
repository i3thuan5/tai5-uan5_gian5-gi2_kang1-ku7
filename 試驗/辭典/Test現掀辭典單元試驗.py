# -*- coding: utf-8 -*-
from unittest.case import TestCase


from 試驗.辭典.辭典單元試驗 import 辭典單元試驗
from 臺灣言語工具.辭典.現掀辭典 import 現掀辭典


class 現掀辭典單元試驗(辭典單元試驗, TestCase):
    辭典型態 = 現掀辭典
