
class 詞組綜合標音():
	綜合標音 = None
	詞組 = None
	def __init__(self, 綜合標音, 詞組):
		self.綜合標音 = 綜合標音
		self.詞組 = 詞組
	def 轉json格式(self):
		return ('{"綜合標音":[' +
			','.join([標音.轉json格式() for 標音 in self.綜合標音]) +
			'],"詞組":"' + self.詞組 + '"}')
	def __repr__(self):
		return self.轉json格式()
	def __str__(self):
		return self.轉json格式()
