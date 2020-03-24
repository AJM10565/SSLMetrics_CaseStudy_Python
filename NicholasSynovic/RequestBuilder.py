import urllib.request

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