import urllib.request
import json

class RequestHandler:

	def __init__(self):
		self.response = None

	def closeResponse(self)	->	None:
		self.response.close()

	def getResponse(self)	->	None:
		return self.response

	def loadResponse(self)	->	dict:
		foo = self.getResponse().read()
		self.closeResponse()
		return json.loads(foo)
		
	def send(self, req:urllib.request.Request):
		self.response = urllib.request.urlopen(req)
	
	def setResponse(self, response)	->	None:
		self.response = response