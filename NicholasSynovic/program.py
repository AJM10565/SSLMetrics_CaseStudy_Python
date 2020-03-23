import datetime
import sys
import urllib.request
import json

class DateTimeBuilder:

	def __init__(self, year:int=2020, month:int=1, day:int=1, hour:int=0, minute:int=0)	->	None:
		self.year = year
		self.month = month
		self.day = day
		self.hour = hour
		self.minute = minute

	def buildDateTime(self)	->	datetime.datetime:
		return datetime.datetime(year=self.year, month=self.month, day=self.day, hour=self.hour, minute=self.minute)

	def buildISODateTime(self)	->	str:
		return self.buildDateTime().isoformat()

	def getDay(self)	->	int:
		return self.day

	def getHour(self)	->	int:
		return self.hour

	def getMinute(self)	->	int:
		return self.minute

	def getMonth(self)	->	int:
		return self.month

	def getYear(self)	->	int:
		return self.year

	def incrementMinute(self, datetime:datetime.datetime)	->	datetime.datetime:
		try:
			return datetime.replace(minute=datetime.minute + 1)
		except ValueError:
			foo = self.incrementHour(datetime=datetime)
			return foo.replace(minute=0)
	
	def incrementHour(self, datetime:datetime.datetime)	->	datetime.datetime:
		try:
			return datetime.replace(hour=datetime.hour + 1)
		except ValueError:
			foo = self.incrementDay(datetime=datetime)
			return foo.replace(hour=0)

	def incrementDay(self, datetime:datetime.datetime)	->	datetime.datetime:
		try:
			return datetime.replace(day=datetime.day + 1)
		except ValueError:
			foo = self.incrementMonth(datetime=datetime)
			return foo.replace(day=1)

	def incrementMonth(self, datetime:datetime.datetime)	->	datetime.datetime:
		try:
			return datetime.replace(month=datetime.month + 1)
		except ValueError:
			foo = self.incrementYear(datetime=datetime)
			return foo.replace(month=1)

	def incrementYear(self, datetime:datetime.datetime)	->	datetime.datetime:
		return datetime.replace(year=datetime.year + 1)

	def setDay(self, day:int=1)	->	None:
		self.day = day
	
	def setHour(self, hour:int=0)	->	None:
		self.hour = hour

	def setMinute(self, minute:int=0)	->	None:
		self.minute = minute

	def setMonth(self, month:int=1)	->	None:
		self.month = month

	def setYear(self, year:int=2020)	->	None:
		self.year = year

class RequestBuilder:

	def __init__(self, token:str, isoDateTime:str)	->	None:
		self.url = "https://api.github.com/graphql"
		self.token = token
		self.isoDateTime = isoDateTime

	def build(self)	->	urllib.request.Request:
		# Payload generated from PostMan code generator
		payload = "{\"query\":\"{\\n    search(query: \\\"language:Python created:<=%s\\\", type: REPOSITORY, first: 100)    {\\n        edges   {\\n            cursor\\n            node    {\\n                ... on Repository   {\\n                    createdAt\\n                    hasIssuesEnabled\\n                    nameWithOwner\\n                    defaultBranchRef    {\\n                        target  {\\n                            ... on Commit   {\\n                                history(first: 0)   {\\n                                    totalCount\\n                                }\\n                            }\\n                        }\\n                    }\\n                    issues  {\\n                        totalCount\\n                    }\\n                    pullRequests    {\\n                        totalCount\\n                    }\\n                }\\n            }\\n        }\\n    }\\n}\",\"variables\":{}}" % (self.isoDateTime)
		
		h = {
			'Authorization': 'bearer ' + self.token,
			'Content-Type': 'application/json'
		}

		payload = bytes(payload, "ascii")

		return urllib.request.Request(url=self.url, data=payload, headers=h)

	def getISODateTime(self)	->	str:
		return self.datetime

	def getToken(self)	->	str:
		return self.token
	
	def getURL(self)	->	str:
		return self.url

	def setDatetime(self, isoDateTime:str)	->	None:
		self.datetime = datetime

	def setToken(self, token:str)	->	None:
		self.token = token

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
		json.loads(foo)
		return foo

	def send(self):
		self.response = urllib.request.urlopen(self.getRequest())

	def setRequest(self, request:urllib.request.Request)	->	None:
		self.request = request
	
	def setResponse(self, response)	->	None:
		self.response = response
	
def program(token:str="", iterateDays:bool=True, iterateHours:bool=True, iterateMinutes:bool=False, year:int=2020, month:int=1, day:int=1, hour:int=0, minute:int=0)	->	None:
	dtb = DateTimeBuilder(year, month, day, hour, minute)
	isoDT = dtb.buildISODateTime()
	rb = RequestBuilder(token=token, isoDateTime=isoDT)
	req = rb.build()
	rh = RequestHandler(request=req)
	rh.send()
	print(rh.loadResponse())
program(token=sys.argv[1])

# print(datetime.datetime.now().isoformat())
# foo = datetime.datetime(year=2019, month=12, day=31, hour=19)
# print(str(foo.isoformat()))
# bar = foo.replace(year=2020)
# print(bar)