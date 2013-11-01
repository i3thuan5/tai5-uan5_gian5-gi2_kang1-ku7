聲母對照表 = {
		'b','p','m','f','v','d','t','n','l','g',
		'k','ng','ngi','h','j','q','x','z','c','s',
		'zi','ci','si','zh','ch','sh','rh'
}
韻母對照表 = {
		'ii','i','e','a','o','u','ie','eu','ieu','ia',
		'ua','ai','uai','au','iau','io','oi','ioi','iu',
		'ui','iui','ue','iim','im','em','iem','am','iam',
		'iin','in','en','ien','uen','an','uan','on','ion',
		'un','iun','ang','iang','uang','ong','iong','ung',
		'iung','iib','ib','eb','ieb','ab','iab','iid','id',
		'ed','ied','ued','ad','uad','od','iod','ud','iud',
		'ag','iag','uag','og','iog','ug','iug','er'
}
調類對照表 = {
		'','ˊ','ˋ','ˇ','+'
}

#########################################
#  2013/11/1 
#  意傳的客家話辨識用拼音
#########################################
class 臺灣客家話拼音: 
	
	#-------成員函式--------#
	def __init__(self, 音標):
		#self.腔
		self.聲母對照表  #通用拼音佮臺灣羅馬聲母對照表
		self.韻母對照表  
		self.調類對照表  
		self.音標 = None
		if 音標[-1:] in self.調類對照表:
				for 所在 in range(len(音標) - 1):
					if 音標[:所在] in self.聲母對照表 and 音標[所在:-1] in self.韻母對照表:
						self.聲 = 音標[:所在]
						self.韻 = 音標[所在:-1]
						self.調 = 音標[-1:]
						#special case	
	
	
	#-------成員變數--------#
	音標上長長度
	聲 = None
	韻 = None
	聲韻 = None
	調 = None
	音標 = None
	
	
	
	