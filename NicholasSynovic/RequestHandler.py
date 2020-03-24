import urllib.request
import json

class RequestHandler:

	def __init__(self, request:urllib.request.Request=None):
		self.request = request
		self.response = None

	def closeResponse(self)	->	None:
		self.response.close()

	def getRequest(self)	->	urllib.request.Request:
		return self.request

	def getResponse(self)	->	None:
		return self.response

	def loadResponse(self)	->	dict:
		foo = self.getResponse().read()
		self.closeResponse()
		return json.loads(foo)
		

	def send(self):
		self.response = urllib.request.urlopen(self.getRequest())

	def setRequest(self, request:urllib.request.Request)	->	None:
		self.request = request
	
	def setResponse(self, response)	->	None:
		self.response = response