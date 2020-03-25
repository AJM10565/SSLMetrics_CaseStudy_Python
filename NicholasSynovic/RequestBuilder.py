import datetime
import urllib.request

class RequestBuilder:

	def __init__(self, token:str, datetime:datetime.datetime)	->	None:
		self.url = "https://api.github.com/graphql"
		self.token = token
		self.datetime = datetime

	def createNewDatetimeFromOld(self, **kwargs)	->	datetime.datetime:	#	TODO: Move this into DateTimeBuilder at some point
		'''
This utilizes the current datetime stored in self.datetime and returns a new datetime utilizing the current one as a base.
		'''
		foo = self.datetime
		if "year" in kwargs:
			foo.replace(year=int(kwargs["year"]))
		if "month" in kwargs:
			foo.replace(month=int(kwargs["month"]))
		if "day" in kwargs:
			foo.replace(day=int(kwargs["day"]))
		if "hour" in kwargs:
			foo.replace(hour=int(kwargs["hour"]))
		if "minute" in kwargs:
			foo.replace(minute=int(kwargs["minute"]))
		return foo

	def getDatetime(self)	->	datetime.datetime:
		return self.datetime

	def getToken(self)	->	str:
		return self.token

	def getURL(self)	->	str:
		return self.url

	def setDatetime(self, datetime:datetime.datetime)	->	None:
		self.datetime = datetime

	def setToken(self, token:str=None)	->	None:
		self.token = token

	def setURL(self, url:str=None)	->	None:
		self.url = url


	def build(self)	->	urllib.request.Request:
		# Payload generated from PostMan code generator
		payload = "{\"query\":\"{\\n  search(query: \\\"language:Python created:%s..%s\\\", type: REPOSITORY, first: 100) {\\n    edges {\\n      cursor\\n      node {\\n        ... on Repository {\\n          createdAt\\n          hasIssuesEnabled\\n          nameWithOwner\\n          defaultBranchRef {\\n            target {\\n              ... on Commit {\\n                history(first: 0) {\\n                  totalCount\\n                }\\n              }\\n            }\\n          }\\n          issues {\\n            totalCount\\n          }\\n          pullRequests {\\n            totalCount\\n          }\\n        }\\n      }\\n    }\\n    pageInfo {\\n      endCursor\\n      hasNextPage\\n      hasPreviousPage\\n      startCursor\\n    }\\n  }\\n}\\n\",\"variables\":{}}" % (isoDateTimeSTART, isoDateTimeEND)

		headers = {
			'Authorization': 'bearer ' + self.token,
			'Content-Type': 'application/json'
		}

		payload = bytes(payload, "ascii")

		return urllib.request.Request(url=self.url, data=payload, headers=headers)
