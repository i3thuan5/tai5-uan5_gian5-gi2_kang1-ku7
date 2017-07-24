# -*- coding: utf-8 -*-
from sys import exit
from unittest.loader import defaultTestLoader
from unittest.runner import TextTestRunner
from unittest.suite import TestSuite


if __name__ == '__main__':
    中研院服務試驗包 = TestSuite()
    中研院服務試驗包.addTest(
        defaultTestLoader.discover(
            '.', pattern='Test中研院*整合試驗.py'
        )
    )
    試驗結果 = TextTestRunner().run(中研院服務試驗包)
    if len(試驗結果.errors) > 0 or len(試驗結果.failures) > 0:
        exit(1)
