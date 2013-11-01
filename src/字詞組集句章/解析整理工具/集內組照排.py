
from 字詞組集句章.基本元素.集 import 集
from 字詞組集句章.基本元素.句 import 句
from 字詞組集句章.基本元素.章 import 章
from 字詞組集句章.解析整理工具.型態錯誤 import 型態錯誤

class 集內組照排:
    def 排好(self, 排法, 物件):
        if isinstance(物件, 集):
            return self.排好集物件(排法,物件)
        if isinstance(物件, 句):
            return self.排好句物件(排法,物件)
        if isinstance(物件, 章):
            return self.排好章物件(排法,物件)
        raise 型態錯誤('傳入來的毋是集句章其中一種物件：{0}，{1}'
            .format(type(物件), str(物件)))
        
    def 排好集物件(self, 排法, 集物件):
        if not isinstance(集物件, 集):
            raise 型態錯誤('傳入來的毋是集物件：{0},{1}'
                .format(type(集物件), str(集物件)))
        return 集(sorted(集物件.內底組, key=排法))
        
    def 排好句物件(self, 排法, 句物件):
        if not isinstance(句物件, 句):
            raise 型態錯誤('傳入來的毋是句物件：{0},{1}'
                .format(type(句物件), str(句物件)))
        集陣列 = []
        for 一集 in 句物件.內底集:
            集陣列.append(self.排好集物件(排法,一集))
        return 句(集陣列)
    
    def 排好章物件(self, 排法, 章物件):
        if not isinstance(章物件, 章):
            raise 型態錯誤('傳入來的毋是章物件：{0},{1}'
                .format(type(章物件), str(章物件)))
        句陣列 = []
        for 一句 in 章物件.內底句:
            句陣列.append(self.排好句物件(排法,一句))
        return 章(句陣列)
        pass
#        音標工具 = 臺灣閩南語羅馬字拼音
#        字 = self.分析器.拆句做字(台語字)
#        標音結果 = []
#        i = 0
#        while i < len(字):
#            for j in range(20, 0, -1):
#                if i + j <= len(字):
#                    腔口型體資料 = 揣腔口型體資料(self.腔口, ''.join(台語字[i:i + j]))
#                    流水號 = set()
#                    [流水號.add(字詞[0]) for 字詞 in 腔口型體資料]
#                    if len(流水號) > 0:
#                        字詞選擇 = []
#                        文讀音編號 = 流水號 & self.文讀字
#                        白話音編號 = 流水號 & self.白話字
#                        其他音編號 = 流水號 - 文讀音編號 - 白話音編號
# #                         字詞登記=set()
#                        文讀音字詞 = []
#                        白話音字詞 = []
#                        其他音字詞 = []
#                        for 流水號碼, 型體, 音標 in 腔口型體資料:
#                            處理過的音標 = self.初胚工具.建立物件語句前處理減號(音標工具, 音標)
#                            字詞資料 = self.分析器.產生對齊組(型體, 處理過的音標)
#                            if 字詞資料 not in 文讀音字詞 and 字詞資料 not in 白話音字詞:
#                                if 流水號碼 in 文讀音編號:
#                                    文讀音字詞.append(字詞資料)
# #                                     字詞登記.add(文讀音字詞[-1])
#                                elif 流水號碼 in 白話音編號:
#                                    白話音字詞.append(字詞資料)
# #                                     字詞登記.add(白話音字詞[-1])
#                        for 流水號碼, 型體, 音標 in 腔口型體資料:
#                            處理過的音標 = self.初胚工具.建立物件語句前處理減號(音標工具, 音標)
#                            字詞資料 = self.分析器.產生對齊組(型體, 處理過的音標)
#                            if 字詞資料 not in 文讀音字詞 and 字詞資料 not in 白話音字詞 and 字詞資料 not in 其他音字詞:
#                                if 流水號碼 in 其他音編號:
#                                    其他音字詞.append(字詞資料)
# #                                     字詞登記.add(其他音字詞[-1])
#                        字詞選擇 = []
#                        if 語言層 == '文讀層':
#                            字詞選擇.extend(文讀音字詞)
#                            字詞選擇.extend(其他音字詞)
#                        elif 語言層 == '白話層':
#                            字詞選擇.extend(白話音字詞)
#                            字詞選擇.extend(其他音字詞)
#                        elif 語言層 == '全部':
#                            字詞選擇.extend(白話音字詞)
#                            字詞選擇.extend(其他音字詞)
#                            字詞選擇.extend(文讀音字詞)
#                        else:
#                            字詞選擇.extend(白話音字詞)
#                            字詞選擇.extend(其他音字詞)
#                            字詞選擇.extend(文讀音字詞)
#                        標音結果.append(集(字詞選擇))
#                        i += j
#                        break
#            else:
#                處理過的音標 = self.初胚工具.建立物件語句前處理減號(音標工具, 音標)
#                標音結果.append(self.分析器.建立集物件(字[i]))
#                i += 1
#        return 句(標音結果)
