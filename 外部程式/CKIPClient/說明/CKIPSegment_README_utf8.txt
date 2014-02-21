使用方法 Ver.20120101
============================================================
※本程式僅支援 big5 ,utf-8, utf-16le 的輸入輸出格式。

用戶端傳送資料之 XML 格式範例：

<?xml version="1.0" ?>
<wordsegmentation version="0.1" charsetcode="big5">
<option showcategory="1" />
<authentication username="iis" password="iis" />
<text>台新金控12月3日將召開股東臨時會進行董監改選。</text>
</wordsegmentation>

注意:如果沒有 charsetcode 屬性，系統預設為big5。
----------------------------------------
1.先設定properties，參數範例如ckipsocket.propeties:

host: mirror site的主機位置  ( ex: host=140.109.19.104 )
port: mirror site的連接埠
user: 你的account name
pass: 你的acount password
overwrite: true/false  
charsetcode: big5/utf-8/utf-16le

程式設定是輸出
系統會檢查輸出資料夾內是否有與輸入資料夾內相同名稱的檔案，如果有的話就不會再重覆送去斷詞。
但如果設定overwrite=true的話，就不會做這項檢查。
---------------------------------------
2. 執行CkipClient.exe [prop] [input dir] [output dir]

prop: 在步驟1設定的propeties
input dir: 你要送去斷詞的文檔所在目錄 (可有子目錄)
output dir: 斷詞結果的目錄。【註一】

斷詞結果會以同樣的子目錄、同樣的檔名儲存在output dir下。
如果跑大量詞彙，有時可能會出現逾時的情況，這時請【註二】。

===================================================================
【註一】切忌與input dir同樣位置。
【註二】砍掉最後一個檔案，設定prop的overwrite=false，然後重新執行。

================================================================
demo：
test.bat是執行範例，測試前請先修改ckipsocket.propeties的帳號資訊