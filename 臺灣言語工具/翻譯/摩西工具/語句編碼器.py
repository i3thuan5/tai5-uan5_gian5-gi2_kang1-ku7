# -*- coding: utf-8 -*-


class 語句編碼器:
    @classmethod
    def 編碼(cls, 語句):
        return 語句.encode('unicode_escape').decode('ascii')

    @classmethod
    def 解碼(cls, 語句):
        return 語句.encode('ascii').decode('unicode_escape')
