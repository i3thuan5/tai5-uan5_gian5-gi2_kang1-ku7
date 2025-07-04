# 臺灣言語工具

[![PyPI version](https://badge.fury.io/py/tai5-uan5-gian5-gi2-kang1-ku7.svg)](https://badge.fury.io/py/tai5-uan5-gian5-gi2-kang1-ku7)
[![Build Status](https://app.travis-ci.com/i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7.svg?branch=main)](https://app.travis-ci.com/i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7)



臺灣語言資訊函式庫，文本處理、語音辨識、合成、斷詞、翻譯、…等功能。

目前支援臺語/閩南語、客話，南島語需要大家的幫忙！！

用法請看[說明文件](https://i3thuan5.github.io/tai5-uan5_gian5-gi2_kang1-ku7/)


## 快速安裝
```bash
pip install tai5-uan5_gian5-gi2_kang1-ku7 # 安裝臺灣言語工具
```
### 安裝其他套件
若需要HTS抑是KenLM，請另外安裝：
```bash
sudo apt-get install -y python3 python-virtualenv g++ python3-dev zlib1g-dev libbz2-dev liblzma-dev libboost-all-dev # Ubuntu/Mint 安裝指令
pip install htsengine
pip install pypi-kenlm
```

## 相關專案
* [KeSi](https://github.com/i3thuan5/KeSi)
  * 包含`台灣言語工具`台文分析功能
  * 簡化API，方便羅馬字轉換
* [臺灣言語服務](https://github.com/sih4sing5hong5/tai5-uan5_gian5-gi2_hok8-bu7)
  * `臺灣言語資料庫`的套件
  * 結果`臺灣言語工具`，做好翻譯、語音合成等自動化模型訓練功能
  * 提供Web-based的服務

## 授權聲明
本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以`LICENSE`授權原文為主：

1. 得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
2. 任何以本程式所衍生的函式庫，必須公開該程式碼；
3. 將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
