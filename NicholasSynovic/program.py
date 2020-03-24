import sys

from DateTimeBuilder import DateTimeBuilder
from RequestBuilder import RequestBuilder
from RequestHandler import RequestHandler
	
def program(token:str="", iterateDays:bool=True, iterateHours:bool=True, iterateMinutes:bool=False, year:int=2020, month:int=1, day:int=1, hour:int=0, minute:int=0)	->	None:
	dtb = DateTimeBuilder(year, month, day, hour, minute)
	isoDT = dtb.buildISODateTime()
	rb = RequestBuilder(token=token, isoDateTime=isoDT)
	req = rb.build()
	rh = RequestHandler(request=req)
	rh.send()
	print(rh.loadResponse())
program(token=sys.argv[1])