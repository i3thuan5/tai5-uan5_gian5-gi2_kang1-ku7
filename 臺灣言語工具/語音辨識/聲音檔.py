import io
import itertools
import struct
import wave
from builtins import range
from math import floor


def 結果轉做陣列(函式, *無名參數, **有名參數):
    def 新函式(*無名參數, **有名參數):
        return list(函式(*無名參數, **有名參數))
    return 新函式


class 聲音檔:
    音框秒數 = 0.02

    @classmethod
    def 對檔案讀(cls, 音檔所在):
        with wave.open(音檔所在, 'rb') as wave音檔:
            return cls(wave音檔)

    @classmethod
    def 對資料轉(cls, 音檔資料):
        return cls.對檔案讀(io.BytesIO(音檔資料))

    @classmethod
    def 對參數轉(cls, 一點幾位元組, 一秒幾點, 幾个聲道, 原始資料):
        with io.BytesIO() as 音檔:
            with wave.open(音檔, mode='wb') as 音物件:
                音物件.setsampwidth(一點幾位元組)
                音物件.setframerate(一秒幾點)
                音物件.setnchannels(幾个聲道)
                音物件.writeframesraw(原始資料)
            return cls.對資料轉(音檔.getvalue())

    def __init__(self, wave音檔):
        self.一點幾位元組 = wave音檔.getsampwidth()
        self.一秒幾點 = wave音檔.getframerate()
        self.幾个聲道 = wave音檔.getnchannels()
        self._資料 = wave音檔.readframes(wave音檔.getnframes())

    def wav音值資料(self):
        return self._資料

    def wav格式資料(self):
        with io.BytesIO() as 結果音檔:
            音物件 = wave.open(結果音檔, mode='wb')
            音物件.setsampwidth(self.一點幾位元組)
            音物件.setframerate(self.一秒幾點)
            音物件.setnchannels(self.幾个聲道)
            音物件.writeframesraw(self.wav音值資料())
            音物件.close()
            return 結果音檔.getvalue()

    def 時間長度(self):
        return len(self._資料) / self.一秒位元組數()

    def 一秒位元組數(self):
        return self.一點幾位元組 * self.一秒幾點 * self.幾个聲道

    def 產生仝參數空聲音檔(self):
        return self.對參數轉(self.一點幾位元組, self.一秒幾點, self.幾个聲道, b'')

    def 接(self, 尾音檔):
        if (self.一點幾位元組 != 尾音檔.一點幾位元組 or
                self.一秒幾點 != 尾音檔.一秒幾點 or
                self.幾个聲道 != 尾音檔.幾个聲道):
            raise ValueError('頭尾聲音檔參數愛仝款！！({},{},{})!=({},{},{})'.format(
                self.一點幾位元組, self.一秒幾點, self.幾个聲道,
                尾音檔.一點幾位元組, 尾音檔.一秒幾點, 尾音檔.幾个聲道,
            ))
        return self.對參數轉(
            self.一點幾位元組, self.一秒幾點, self.幾个聲道,
            self.wav音值資料() + 尾音檔.wav音值資料()
        )

    @結果轉做陣列
    def 全部音框(self, 音框秒數=音框秒數):
        頂一个音框所在 = 0
        資料數量 = len(self._資料) / (self.一點幾位元組 * self.幾个聲道)
        for 第幾个音框 in itertools.count(1):
            後一個音个所在 = int(self.一秒幾點 * 音框秒數 * 第幾个音框)
            資料 = []
            try:
                for 第幾个音值 in range(頂一个音框所在, 後一個音个所在):
                    資料.append(self._提著音值(第幾个音值))
            except struct.error:
                pass
            yield 資料
            頂一个音框所在 = 後一個音个所在
            if 頂一个音框所在 >= 資料數量:
                break

    @結果轉做陣列
    def 照函式切音(self, 判斷函式, 音框秒數=音框秒數):
        開始點所在 = 0
        有資料矣 = False
        先停時間 = None
        for 第幾个音框, 音框 in enumerate(self.全部音框(音框秒數)):
            if 判斷函式(音框):
                有資料矣 = True
                if 先停時間 is not None:
                    後尾時間 = (先停時間 + 第幾个音框) / 2
                    結束秒數 = 後尾時間 * 音框秒數
                    結束點所在 = int(self.一秒幾點 * 結束秒數)
                    yield self._照點所在切出音檔(開始點所在, 結束點所在)
                    開始點所在 = 結束點所在
                    先停時間 = None
            else:
                if 有資料矣 and 先停時間 is None:
                    先停時間 = 第幾个音框
        後尾時間 = 第幾个音框 + 1
        結束秒數 = 後尾時間 * 音框秒數
        結束點所在 = int(self.一秒幾點 * 結束秒數)
        yield self._照點所在切出音檔(開始點所在, 結束點所在)

    def 照秒數切出音檔(self, 開始秒數, 結束秒數):
        開始點所在 = floor(self.一秒幾點 * 開始秒數)
        結束點所在 = floor(self.一秒幾點 * 結束秒數)
        return self._照點所在切出音檔(開始點所在, 結束點所在)

    def _提著音值(self, 第幾个音值, 頻道=0):
        開始所在 = self.一點幾位元組 * (第幾个音值 * self.幾个聲道 + 頻道)
        return struct.unpack('h', self._資料[開始所在:開始所在 + self.一點幾位元組])[0]

    def _照點所在切出音檔(self, 開始點所在, 結束點所在):
        一秒的點數 = self.一點幾位元組 * self.幾个聲道
        開始實際所在 = 開始點所在 * 一秒的點數
        結束實際所在 = 結束點所在 * 一秒的點數
        return 聲音檔.對參數轉(
            self.一點幾位元組, self.一秒幾點, self.幾个聲道,
            self._資料[開始實際所在:結束實際所在]
        )
