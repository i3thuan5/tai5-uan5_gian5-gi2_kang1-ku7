class 字:
	型 = None
	音 = None
	def __init__(self, 型, 音):
		self.型 = 型
		self.音 = 音
	def __repr__(self):
		if  self.型==None:
			return "@@"
		return self.型 + " " + self.音
	def __str__(self):
		return self.型 + " " + self.音
