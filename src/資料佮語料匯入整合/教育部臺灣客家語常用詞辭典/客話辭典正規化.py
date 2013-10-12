class 客話辭典正規化:
    def 處理音標(self, 音標):
        音標 = 音標.split('）')[-1]
        音標 = 音標.replace('文', '')
        音標 = 音標.replace('白', '')
        return 音標.strip()
