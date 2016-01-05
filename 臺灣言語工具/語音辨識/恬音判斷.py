from math import sqrt


# 參考http://practicalcryptography.com/miscellaneous/machine-learning/voice-activity-detection-vad-tutorial/
class 恬音判斷:

    @classmethod
    def 算特徵參數(cls, 音框):
        return {
            '平方平均': cls.平方平均(音框),
            '過零機率': cls.過零機率(音框),
            '相關係數': cls.相關係數(音框),
        }

    @classmethod
    def 平方平均(cls, 音框):
        數字 = 0
        for 音值 in 音框:
            數字 += 音值 * 音值
        return 數字 / len(音框)

    @classmethod
    def 過零機率(cls, 音框):
        數量 = 0
        頂一個 = 音框[0]
        for 音值 in 音框[1:]:
            if 頂一個 * 音值 <= 0:
                數量 += 1
            頂一個 = 音值
        return 數量 / (len(音框) - 1)

    @classmethod
    def 相關係數(cls, 音框):
        分子 = 0
        頂一個 = 音框[0]
        for 音值 in 音框[1:]:
            分子 += 頂一個 * 音值
            頂一個 = 音值
        平方合 = cls.平方平均(音框) * len(音框)
        分母前 = 平方合 - 音框[0] * 音框[0]
        分母後 = 平方合 - 音框[-1] * 音框[-1]
        分母 = sqrt(分母前 * 分母後)
        try:
            結果 = 分子 / 分母
        except ZeroDivisionError:
            結果 = None
        return 結果
