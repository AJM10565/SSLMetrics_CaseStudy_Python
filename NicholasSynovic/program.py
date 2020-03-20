import datetime
import urllib.request

class RequestBuilder:

	def __init__(self, token:str, datetime:datetime.datetime):
		self.url = "https://api.github.com/graphql"
		self.token = token
		self.datetime = datetime

	def getDatetime(self)	->	datetime.datetime:
		return self.datetime

	def getToken(self)	->	str:
		return self.token
	
	def getURL(self)	->	str:
		return self.url

	def setDatetime(self, datetime:datetime.datetime)	->	None:
		self.datetime = datetime

	def setToken(self, token:str)	->	None:
		self.token = token

	def build(self)	->	urllib.request.Request:
		# Payload generated from PostMan Code generator
		payload = "{\"query\":\"{\\n    search(query: \\\"language:Python created:<=%s\\\", type: REPOSITORY, first: 100)    {\\n        edges   {\\n            cursor\\n            node    {\\n                ... on Repository   {\\n                    createdAt\\n                    hasIssuesEnabled\\n                    nameWithOwner\\n                    defaultBranchRef    {\\n                        target  {\\n                            ... on Commit   {\\n                                history(first: 0)   {\\n                                    totalCount\\n                                }\\n                            }\\n                        }\\n                    }\\n                    issues  {\\n                        totalCount\\n                    }\\n                    pullRequests    {\\n                        totalCount\\n                    }\\n                }\\n            }\\n        }\\n    }\\n}\",\"variables\":{}}" % (self.datetime)
		
		headers = {
			'Authorization': 'token %s' % (self.token),
			'Content-Type': 'application/json'
		}

		return urllib.request.Request(url=self.url, data=payload, headers=headers)

with open("token.txt", "r") as foo:
	token = foo.read()
	foo.close()
	b = RequestBuilder(token=token)
	print(b.getToken())
	print(type(b.build()))

# print(datetime.datetime.now().isoformat())
# foo = datetime.datetime(year=2019, month=12, day=31, hour=19)
# print(str(foo.isoformat()))
# bar = foo.replace(year=2020)
# print(bar)