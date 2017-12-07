import urllib.request
import sys
class ImagensNet:
	return_ = None
	def __init__(self, link):
		try:
			url = urllib.request.urlretrieve(link, "Imagens/1.jpg")
			self.return_ = True
		except Exception as e:
			self.return_ = False
