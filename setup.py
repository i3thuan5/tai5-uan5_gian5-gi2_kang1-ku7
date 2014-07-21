# -*- coding: utf-8 -*-
'''
tar無法度下傷長的檔案名，所以愛用zip
python3 setup.py sdist --format=zip upload
'''
import os
from distutils.core import setup
from 版本 import 版本

def 揣工具包(頭='.'):
	'setup的find_packages無支援windows中文檔案'
	工具包 = []
	for 目錄, 資料夾, 檔案 in os.walk(頭):
		if '__init__.py' in 檔案:
			工具包.append(目錄.replace('/', '.'))
	return 工具包

def 讀(檔名):
	return open(os.path.join(os.path.dirname(__file__), 檔名), encoding='utf-8').read()

setup(
	# 臺灣言語工具 tai5_uan5_gian5_gi2_kang1_ku7
	name='tai5_uan5_gian5_gi2_kang1_ku7',
	packages=揣工具包('臺灣言語工具'),
	version=版本,
	description='臺灣語言資訊系統（Toolkit for Languages in Taiwan）',
	long_description=讀('README'),
	author='薛丞宏',
	author_email='ihcaoe@gmail.com',
	url='http://意傳.台灣/',
	download_url='https://github.com/sih4sing5hong5/tai5_uan5_gian5_gi2_kang1_ku7',  # I'll explain this in a second
	keywords=[
		'臺灣', '語料庫', '語言合成', '機器翻譯', '斷詞',
		'Taiwan', 'Taiwanese', 'Natural Language', 'Corpus',
		'Text to Speech', 'TTS',
		'Machine Translateion',
		'Word Segmentation',
		],
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Operating System :: POSIX :: Other',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
		'Natural Language :: Chinese (Traditional)',
		'Topic :: Scientific/Engineering',
		'Topic :: Scientific/Engineering :: Information Analysis',
		'Topic :: Text Processing',
		'Topic :: Text Processing :: Linguistic',
	],
)
