
class 台語多元書寫:
    @classmethod
    def 書寫章(cls, 章物件):
        結果 = []
        for 句物件 in 章物件.內底句:
            結果.append(cls.書寫章(句物件))
        return 結果

    @classmethod
    def 書寫句(cls, 句物件):
        pass
