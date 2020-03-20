import datetime
import urllib.request

class DateTimeBuilder:

	def __init__(self, year:int=2020, month:int=1, day:int=1, hour:int=0, minute:int=0)	->	None:
		self.year = year
		self.month = month
		self.day = day
		self.hour = hour
		self.minute = minute

	def build(self)	->	datetime.datetime:
		return datetime.datetime(year=self.year, month=self.month, day=self.day, hour=self.hour, minute=self.minute)

	def buildISO(self)	->	str:
		return self.build().isoformat()

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
		
		headers = {
			'Authorization': 'token %s' % (self.token),
			'Content-Type': 'application/json'
		}

		return urllib.request.Request(url=self.url, data=payload, headers=headers)

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

with open("token.txt", "r") as foo:
	token = foo.read()
	foo.close()

d = DateTimeBuilder()

b = RequestBuilder(token=token, isoDateTime=d.buildISO())
print(b.getToken())
print(type(b.build()))

# print(datetime.datetime.now().isoformat())
# foo = datetime.datetime(year=2019, month=12, day=31, hour=19)
# print(str(foo.isoformat()))
# bar = foo.replace(year=2020)
# print(bar)