import datetime
import urllib.request
import sys
sys.path.append("/NicholasSynovic/")

from NicholasSynovic import DateTimeBuilder
class RequestBuilder:

	def __init__(self, token:str)	->	None:
		self.url = "https://api.github.com/graphql"
		self.token = token
		self.datetime = None

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

	# def makeISODatetimes(self, dt:datetime.datetime=None)	->	tuple:
	# 	dtb = DateTimeBuilder.DateTimeBuilder(year=dt.year, month=dt.month, day=dt.day, hour=dt.hour, minute=dt.minute)
	# 	foo = dtb.buildISODateTime()
	# 	bar 

	def build(self, isoDatetimeSTART:str, isoDatetimeEND)	->	urllib.request.Request:
		# Payload generated from PostMan code generator
		payload = "{\"query\":\"{\\n  search(query: \\\"language:Python created:%s..%s\\\", type: REPOSITORY, first: 100) {\\n    edges {\\n      cursor\\n      node {\\n        ... on Repository {\\n          createdAt\\n          hasIssuesEnabled\\n          nameWithOwner\\n          defaultBranchRef {\\n            target {\\n              ... on Commit {\\n                history(first: 0) {\\n                  totalCount\\n                }\\n              }\\n            }\\n          }\\n          issues {\\n            totalCount\\n          }\\n          pullRequests {\\n            totalCount\\n          }\\n        }\\n      }\\n    }\\n    pageInfo {\\n      endCursor\\n      hasNextPage\\n      hasPreviousPage\\n      startCursor\\n    }\\n  }\\n}\\n\",\"variables\":{}}" % (isoDatetimeSTART, isoDatetimeEND)

		headers = {
			'Authorization': 'bearer ' + self.token,
			'Content-Type': 'application/json'
		}

		payload = bytes(payload, "ascii")

		return urllib.request.Request(url=self.url, data=payload, headers=headers)
