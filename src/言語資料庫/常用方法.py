def 展開(items):
	result = []
	for item in items:
		if isinstance(item, list):
			result.extend(展開(item))
		else:
			result.append(item)
	return result

def 提掉空白(切開的資料):
	return [ 詞 for 詞 in 切開的資料 if 詞 != '' and 詞 != ' ']

def 拆開獨元素組(獨元素組資料):
	return [ 獨元素組[0] for 獨元素組 in 獨元素組資料]