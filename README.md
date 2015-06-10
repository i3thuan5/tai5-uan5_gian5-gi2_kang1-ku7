#臺灣言語工具

[![Supported Python versions](https://pypip.in/py_versions/tai5_uan5_gian5_gi2_kang1_ku7/badge.svg)](https://pypi.python.org/pypi/tai5_uan5_gian5_gi2_kang1_ku7/)
[![Development Status](https://pypip.in/status/tai5_uan5_gian5_gi2_kang1_ku7/badge.svg)](https://pypi.python.org/pypi/tai5_uan5_gian5_gi2_kang1_ku7/)
[![Latest Version](https://pypip.in/version/tai5_uan5_gian5_gi2_kang1_ku7/badge.svg)](https://pypi.python.org/pypi/tai5_uan5_gian5_gi2_kang1_ku7/)
[![Build Status](https://travis-ci.org/sih4sing5hong5/tai5_uan5_gian5_gi2_kang1_ku7.svg?branch=master)](https://travis-ci.org/sih4sing5hong5/tai5_uan5_gian5_gi2_kang1_ku7)
[![Coverage Status](https://coveralls.io/repos/sih4sing5hong5/tai5_uan5_gian5_gi2_kang1_ku7/badge.svg)](https://coveralls.io/r/sih4sing5hong5/tai5_uan5_gian5_gi2_kang1_ku7)

臺灣語言資訊函式庫，文本處理、語音辨識、合成、斷詞、翻譯、…等功能。

##快速安裝
```bash
sudo apt-get install -y g++ libboost-all-dev python3 python-virtualenv
virtualenv venv --python python3 # 設置環境檔
. venv/bin/activate # 載入環境
pip install https://github.com/rsennrich/Bleualign/archive/master.zip pip install https://github.com/kpu/kenlm/archive/master.zip
pip install tai5_uan5_gian5_gi2_kang1_ku7
```

##使用說明

###基本元素
* 字
* 詞
* 組
* 集
* 句
* 章

解析工具

會當參考`python 範例/基本元素.py`

###常見情境
會當參考`試驗/整合試驗`的檔案

### 翻譯模型訓練 
本函式庫使用[Moses](http://www.statmt.org/moses/?n=Development.GetStarted)統計式機器翻譯。

#### 翻譯工具需要套件
```bash
sudo apt-get install -y g++ git subversion automake libtool zlib1g-dev libboost-all-dev libbz2-dev liblzma-dev python3-dev libgoogle-perftools-dev libxmlrpc-c++.*-dev # moses, libxmlrpc for mosesserver
sudo apt-get install -y cmake # mgiza
```

#### 安裝
```python3
from 臺灣言語工具.翻譯.摩西工具.安裝摩西翻譯佮相關程式 import 安裝摩西翻譯佮相關程式
安裝程式 = 安裝摩西翻譯佮相關程式()
安裝程式.安裝moses(編譯CPU數=4)
安裝程式.安裝gizapp()
安裝程式.安裝mgiza()
```

##開發
上面的pip不要裝`tai5_uan5_gian5_gi2_kang1_ku7`
```bash
sudo apt-get install -y g++ libboost-all-dev python3 python-virtualenv
virtualenv venv --python python3 # 設置環境檔
. venv/bin/activate # 載入環境
pip install https://github.com/rsennrich/Bleualign/archive/master.zip pip install https://github.com/kpu/kenlm/archive/master.zip
```

##詳細安裝

###作業系統
推薦[Mint Linux](http://www.linuxmint.com/download.php)佮[Ubuntu Linux](http://www.ubuntu-tw.org/modules/tinyd0/)
若是別的Linux抑是iOS攏會使
只是指令愛家己變化

###虛擬環境設定
請先安裝python3、[pip](https://pip.pypa.io/en/latest/installing.html)佮[virtualenv](https://virtualenv.readthedocs.org/en/latest/)
```bash
sudo apt-get install -y python3 python-virtualenv
virtualenv venv --python python3 # 設置環境檔
. venv/bin/activate # 載入環境
```
會當參考：[virtualenv](http://www.openfoundry.org/tw/tech-column/8516-pythons-virtual-environment-and-multi-version-programming-tools-virtualenv-and-pythonbrew)使用說明

每次使用前開啟環境
```bash
virtualenv venv --python python3 # 設置環境檔
. venv/bin/activate # 載入環境
```

###安裝

####PYPI發行版本
```bash
pip install tai5_uan5_gian5_gi2_kang1_ku7
```

####徙掉
```bash
pip uninstall tai5_uan5_gian5_gi2_kang1_ku7
```

###相關套件
####[bleualign](https://github.com/rsennrich/Bleualign)
平行語句對齊函式庫
```bash
pip install https://github.com/rsennrich/Bleualign/archive/master.zip
```
####[Kenlm](https://github.com/kpu/kenlm)
語言模型函式庫
```bash
sudo apt-get install -y g++ libboost-all-dev # for Ubuntu 14.04+ /Mint 17+
pip install https://github.com/kpu/kenlm/archive/master.zip
```
####[htsengine](https://github.com/sih4sing5hong5/hts_engine_python)
語音合成工具
```bash
pip install https://github.com/sih4sing5hong5/hts_engine_python/archive/master.zip
```

##聲明
本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以`LICENSE`授權原文為主：
	１．得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
	２．任何以程式碼衍生的執行檔或網路服務，必須公開該程式碼；
	３．將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
