#臺灣言語工具
---------------------

臺灣語言資訊系統製作，教材編排、語音辨識、合成、翻譯、…

程式佇eclipse面頂開發，裝pydev佮git，閣有函式庫就會使用矣

文件會沓沓仔寫新的，多謝～～


##準備
----------------------------
###作業系統
推薦[Mint Linux](http://www.linuxmint.com/download.php)佮[Ubuntu Linux](http://www.ubuntu-tw.org/modules/tinyd0/)
若是別的Linux抑是iOS攏會使
只是指令愛家己變化

###請先安裝python3、[pip](https://pip.pypa.io/en/latest/installing.html)佮[virtualenv](https://virtualenv.readthedocs.org/en/latest/)
```bash
sudo apt-get install python3 python3-pip
sudo pip3 install virtualenv
```
會當參考：[virtualenv](http://www.openfoundry.org/tw/tech-column/8516-pythons-virtual-environment-and-multi-version-programming-tools-virtualenv-and-pythonbrew)使用說明

##安裝
----------------------------
<!---
###PYPI發行版本
```bash
pip install tai5_uan5_gian5_gi2_kang1_ku7
```
--->
###上新的開發版本
```bash
pip install https://github.com/sih4sing5hong5/tai5_uan5_gian5_gi2_kang1_ku7/archive/master.zip
```
###徙掉
```bash
pip uninstall tai5_uan5_gian5_gi2_kang1_ku7
```

##相關套件
###bleualign
```bash
pip install https://github.com/rsennrich/Bleualign/archive/master.zip
```
###kenlm
```bash
sudo apt-get install -y g++ libboost-all-dev # for Ubuntu 14.04+ /Mint 17+
pip install https://github.com/kpu/kenlm/archive/master.zip
```
###htsengine
```bash
pip install https://github.com/sih4sing5hong5/hts_engine_python/archive/master.zip
```
