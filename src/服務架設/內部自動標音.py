
import Pyro4
from 斷詞標音.自動標音 import 自動標音

class 內部自動標音():
	def __init__(self):
		標音工具 = 自動標音()
		Pyro4.Daemon.serveSimple(
		{
			標音工具: "內部自動標音"
		},ns = True)

		
if __name__ == '__main__':
	內部自動標音()