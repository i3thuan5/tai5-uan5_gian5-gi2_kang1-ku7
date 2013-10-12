from 言語資料庫.公用資料 import 資料庫連線
流水號查詢=資料庫連線.prepare('SELECT "流水號" FROM "言語"."文字" ORDER BY "流水號"')

刣流水號=資料庫連線.prepare('DELETE FROM "言語"."文字" WHERE "流水號"=$1')

for 流水號 in 流水號查詢():
	print(流水號[0])
	刣流水號(流水號[0])