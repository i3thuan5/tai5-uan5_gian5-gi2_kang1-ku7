class 辭典集:
    def __init__(self, *tsuanpoo_sutian):
        if len(tsuanpoo_sutian) == 0:
            raise ValueError('上無愛傳一个辭典入來')
        self.tsuanpoo_sutian = tsuanpoo_sutian
        self._上濟字數 = 1
        for sutian in tsuanpoo_sutian:
            if sutian.上濟字數() > self._上濟字數:
                self._上濟字數 = sutian.上濟字數()

    def 上濟字數(self):
        return self._上濟字數

    def 查詞(self, 詞物件):
        tsha = []
        for _ in range(self.上濟字數()):
            tsha.append(set())
        for sutian in self.tsuanpoo_sutian:
            for tsha_set, sutian_set in zip(tsha, sutian.查詞(詞物件)):
                tsha_set |= sutian_set
        return tsha
