import urllib.request
from urllib.request import Request, urlopen

class RequestBuilder:

	def __init__(self, token:str):
		self.url = "https://api.github.com/graphql"
		self.token = token

	def getURL(self)	->	str:
		return self.url

	def getToken(self)	->	str:
		return self.token

	def setToken(self, token:str)	->	None:
		self.token = token

	def build(self)	->	urllib.request.Request:
		# Payload generated from request
		payload = "{\"query\":\"{\\n    search(query: \\\"language:Python created:<=2018-10-29T00:00:00\\\", type: REPOSITORY, first: 100)    {\\n        edges   {\\n            cursor\\n            node    {\\n                ... on Repository   {\\n                    createdAt\\n                    hasIssuesEnabled\\n                    nameWithOwner\\n                    defaultBranchRef    {\\n                        target  {\\n                            ... on Commit   {\\n                                history(first: 0)   {\\n                                    totalCount\\n                                }\\n                            }\\n                        }\\n                    }\\n                    issues  {\\n                        totalCount\\n                    }\\n                    pullRequests    {\\n                        totalCount\\n                    }\\n                }\\n            }\\n        }\\n    }\\n}\",\"variables\":{}}"
		
		headers = {
			'Authorization': 'token %s' % (self.token),
			'Content-Type': 'application/json'
		}

		return Request(url=self.url, data=payload, headers=headers)

with open("token.txt", "r") as foo:
	token = foo.read()
	b = RequestBuilder(token=token)
	print(b.getToken())
	print(type(b.build()))
