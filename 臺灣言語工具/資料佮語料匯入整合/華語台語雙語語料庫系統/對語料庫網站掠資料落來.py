"""
著作權所有 (C) 民國103年 意傳文化科技
開發者：薛丞宏
網址：http://意傳.台灣
語料來源：請看各資料庫內說明

本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以授權原文為主：
    １．得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
    ２．任何以程式碼衍生的執行檔或網路服務，必須公開該程式碼；
    ３．將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
"""
import urllib.request
import json

class 對語料庫網站掠資料落來:
    #[{'閩南語':'...','國語':'...'},{'閩南語':'...','國語':'...'},]
    def 掠資料(self):
        #icorpus.iis.sinica.edu.tw/全部題號
        網頁=urllib.request.urlopen(
            'http://icorpus.iis.sinica.edu.tw/%E5%85%A8%E9%83%A8%E9%A1%8C%E8%99%9F'
            ).read()
        #icorpus.iis.sinica.edu.tw/{0}/揣翻譯對應/
        掠文章='http://icorpus.iis.sinica.edu.tw/{0}/%E6%8F%A3%E7%BF%BB%E8%AD%AF%E5%B0%8D%E6%87%89/'
        資料=[]
        for 文章號碼 in json.loads(網頁.decode('UTF-8'))[:]:
            文章內容=urllib.request.urlopen(掠文章.format(文章號碼)).read()
#             print(文章內容.decode('UTF-8'))
#             print(掠文章.format(文章號碼))
#             print(文章號碼)
            翻譯=json.loads(文章內容.decode('UTF-8'))
            資料.append(翻譯)
        return 資料 
        
if __name__=='__main__':
    掠資料落來=對語料庫網站掠資料落來()
    資料=掠資料落來.掠資料()
    print(資料)