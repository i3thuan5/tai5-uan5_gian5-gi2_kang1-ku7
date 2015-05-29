# -*- coding: utf-8 -*-
from 臺灣言語工具.表單.現掀辭典 import 現掀辭典
from 試驗.表單.辭典單元試驗 import 辭典單元試驗
from unittest.case import TestCase


class 現掀辭典單元試驗(辭典單元試驗,TestCase):
	辭典型態=現掀辭典
