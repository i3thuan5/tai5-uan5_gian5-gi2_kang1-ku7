class 字:
	型 = None
	音 = None
	def __init__(self, 型, 音):
		self.型 = 型
		self.音 = 音
	def __repr__(self):
		return self.型 + " " + self.音
	def __str__(self):
		return self.型 + " " + self.音
	def __eq__(self, other):
		return other != None and self.型 == other.型 and self.音 == other.音
