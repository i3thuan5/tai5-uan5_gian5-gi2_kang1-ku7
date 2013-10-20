
if __name__ == '__main__':
	輸出=open('/home/Ihc/tmpfs/fileOut','w')
	for 檔名 in open('/home/Ihc/tmpfs/fileAll'):
		if 檔名.strip()!='':
			檔名=檔名.strip()
			print('mv',檔名,檔名.replace('/','+'),file=輸出)