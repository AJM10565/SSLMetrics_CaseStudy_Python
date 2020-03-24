import urllib.request

class RequestBuilder:

	def __init__(self, token:str, isoDateTimeSTART:str=None, isoDateTimeEND:str=None)	->	None:
		self.url = "https://api.github.com/graphql"
		self.token = token
		self.isoDateTimeSTART = isoDateTimeSTART
		self.ISODateTimeEND = isoDateTimeEND

	def build(self, singleDatetime:bool=True, betweenDatetimes:bool=False)	->	urllib.request.Request:
		# Payload generated from PostMan code generator
		if singleDatetime and betweenDatetimes:
			print("Incompatible queries.\nDefaulting to singleDatetime")

			foo = self.isoDateTimeSTART
			bar = foo.find("T")
			if foo[bar:] == "T00:00:00":
				datetime = foo[0:bar]

			payload = "{\"query\":\"{\\n  search(query: \\\"language:Python created:%s\\\", type: REPOSITORY, first: 100) {\\n    edges {\\n      cursor\\n      node {\\n        ... on Repository {\\n          createdAt\\n          hasIssuesEnabled\\n          nameWithOwner\\n          defaultBranchRef {\\n            target {\\n              ... on Commit {\\n                history(first: 0) {\\n                  totalCount\\n                }\\n              }\\n            }\\n          }\\n          issues {\\n            totalCount\\n          }\\n          pullRequests {\\n            totalCount\\n          }\\n        }\\n      }\\n    }\\n    pageInfo {\\n      endCursor\\n      hasNextPage\\n      hasPreviousPage\\n      startCursor\\n    }\\n  }\\n}\\n\",\"variables\":{}}" % (datetime)
			
		elif singleDatetime and not betweenDatetimes:
			payload = "{\"query\":\"{\\n  search(query: \\\"language:Python created:%s\\\", type: REPOSITORY, first: 100) {\\n    edges {\\n      cursor\\n      node {\\n        ... on Repository {\\n          createdAt\\n          hasIssuesEnabled\\n          nameWithOwner\\n          defaultBranchRef {\\n            target {\\n              ... on Commit {\\n                history(first: 0) {\\n                  totalCount\\n                }\\n              }\\n            }\\n          }\\n          issues {\\n            totalCount\\n          }\\n          pullRequests {\\n            totalCount\\n          }\\n        }\\n      }\\n    }\\n    pageInfo {\\n      endCursor\\n      hasNextPage\\n      hasPreviousPage\\n      startCursor\\n    }\\n  }\\n}\\n\",\"variables\":{}}" % (self.isoDateTimeSTART)
		
		elif not singleDatetime and betweenDatetimes:
			payload = "{\"query\":\"{\\n  search(query: \\\"language:Python created:%s..%s\\\", type: REPOSITORY, first: 100) {\\n    edges {\\n      cursor\\n      node {\\n        ... on Repository {\\n          createdAt\\n          hasIssuesEnabled\\n          nameWithOwner\\n          defaultBranchRef {\\n            target {\\n              ... on Commit {\\n                history(first: 0) {\\n                  totalCount\\n                }\\n              }\\n            }\\n          }\\n          issues {\\n            totalCount\\n          }\\n          pullRequests {\\n            totalCount\\n          }\\n        }\\n      }\\n    }\\n    pageInfo {\\n      endCursor\\n      hasNextPage\\n      hasPreviousPage\\n      startCursor\\n    }\\n  }\\n}\\n\",\"variables\":{}}" % (isoDateTimeSTART, isoDateTimeEND)

		else:
			print("Incompatible queries.\nExiting program")
			quit()

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