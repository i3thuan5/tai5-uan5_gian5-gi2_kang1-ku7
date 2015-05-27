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
pip install tai5_uan5_gian5_gi2_kang1_ku7 https://github.com/rsennrich/Bleualign/archive/master.zip pip install https://github.com/kpu/kenlm/archive/master.zip
```

##開發
上面的pip不要裝`tai5_uan5_gian5_gi2_kang1_ku7`
```bash
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
sudo pip3 install virtualenv
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
```bash
pip install https://github.com/rsennrich/Bleualign/archive/master.zip
```
####[kenlm](https://github.com/kpu/kenlm)
```bash
sudo apt-get install -y g++ libboost-all-dev # for Ubuntu 14.04+ /Mint 17+
pip install https://github.com/kpu/kenlm/archive/master.zip
```
####[htsengine](https://github.com/sih4sing5hong5/hts_engine_python)
```bash
pip install https://github.com/sih4sing5hong5/hts_engine_python/archive/master.zip
```

