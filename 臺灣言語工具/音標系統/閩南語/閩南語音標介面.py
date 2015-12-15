# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class 閩南語音標介面(metaclass=ABCMeta):
    # 消警告用
    _頂層 = ABCMeta

    def 預設音標(self):
        return self.轉換到臺灣閩南語羅馬字拼音()

    @abstractmethod
    def 轉換到臺灣閩南語羅馬字拼音(self):
        pass
