# -*- coding: utf-8 -*-
from distutils.core import setup
import os
import sys
from 版本 import 版本


def 揣工具包(頭='.'):
    'setup的find_packages無支援windows中文檔案'
    工具包 = []
    for 目錄, _, 檔案 in os.walk(頭):
        if '__init__.py' in 檔案:
            工具包.append(目錄.replace('/', '.'))
    return 工具包

# tar無法度下傷長的檔案名，所以愛用zip
# python setup.py sdist --format=zip upload
print('sys.argv', sys.argv)
try:
    sys.argv.insert(sys.argv.index('sdist') + 1, '--format=zip')
except ValueError:
    # 無upload
    pass

setup(
    # 臺灣言語工具 tai5_uan5_gian5_gi2_kang1_ku7
    name='tai5_uan5_gian5_gi2_kang1_ku7',
    packages=揣工具包('臺灣言語工具'),
    version=版本,
    description='臺灣語言資訊系統（Toolkit for Languages in Taiwan）',
    long_description='臺灣語言資訊系統函式庫，支援語音辨識、合成、翻譯、…等技術',
    author='薛丞宏',
    author_email='ihcaoe@gmail.com',
    url='http://意傳.台灣/',
    # I'll explain this in a second
    download_url='https://github.com/sih4sing5hong5/tai5_uan5_gian5_gi2_kang1_ku7',
    keywords=[
        '臺灣', '語料庫', '語言合成', '機器翻譯', '斷詞',
        'Taiwan', 'Taiwanese', 'Natural Language', 'Corpus',
                'Text to Speech', 'TTS',
                'Machine Translateion',
                'Word Segmentation',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',
    ],
)
