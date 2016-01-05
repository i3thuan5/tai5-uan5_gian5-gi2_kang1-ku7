import io
import itertools
import struct
import wave


class 聲音檔:

    @classmethod
    def 從檔案讀(cls, 音檔所在):
        with wave.open(音檔所在, 'rb') as wave音檔:
            return cls(wave音檔)

    @classmethod
    def 從資料轉(cls, 音檔資料):
        return cls.從檔案讀(io.BytesIO(音檔資料))

    @classmethod
    def 從參數轉(cls, 一點幾位元組, 一秒幾點, 幾个聲道, 原始資料):
        with io.BytesIO() as 音檔:
            with wave.open(音檔, mode='wb') as 音物件:
                音物件.setsampwidth(一點幾位元組)
                音物件.setframerate(一秒幾點)
                音物件.setnchannels(幾个聲道)
                音物件.writeframesraw(原始資料)
            return cls.從資料轉(音檔.getvalue())

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

    def 全部音框(self, 音框秒數=0.02):
        頂一个音框所在 = 0
        停 = False
        for 第幾个音框 in itertools.count(1):
            後一個音个所在 = int(self.一秒幾點 * 音框秒數 * 第幾个音框)
            資料 = []
            try:
                for 第幾个音值 in range(頂一个音框所在, 後一個音个所在):
                    資料.append(self._提著音值(第幾个音值))
            except struct.error:
                停 = True
            yield 資料
            頂一个音框所在 = 後一個音个所在
            if 停 or 頂一个音框所在 > len(self._資料):
                break

    def _提著音值(self, 第幾个音值, 頻道=0):
        開始所在 = self.一點幾位元組 * (第幾个音值 * self.幾个聲道 + 頻道)
        return struct.unpack('h', self._資料[開始所在:開始所在 + self.一點幾位元組])[0]
