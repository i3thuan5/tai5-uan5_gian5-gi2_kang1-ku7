from distutils.core import setup
import os

def 讀(檔名):
	return open(os.path.join(os.path.dirname(__file__), 檔名)).read()

setup(
	# 臺灣言語工具 tai5_uan5_gian5_gi2_kang1_ku7
	name='tai5_uan5_gian5_gi2_kang1_ku7',
	packages=['臺灣言語工具'],
	version='0.2.1',
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
