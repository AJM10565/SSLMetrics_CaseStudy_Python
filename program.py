import sys
sys.path.append("/NicholasSynovic/")

from NicholasSynovic import DateTimeBuilder
from NicholasSynovic import RequestBuilder
from NicholasSynovic import RequestHandler
	
def program(token:str="", iterateDays:bool=True, iterateHours:bool=True, iterateMinutes:bool=False, year:int=2020, month:int=1, day:int=1, hour:int=0, minute:int=0)	->	None:
	#	Initalizes DateTimeBuilder class
	dtb = DateTimeBuilder.DateTimeBuilder()
	
	#	Sets the values of the FIRST datetime to be searched for
	dtb.setYear(year=year)
	dtb.setMonth(month=month)
	dtb.setDay(day=day)
	dtb.setHour(hour=hour)
	dtb.setMinute(minute=minute)

	#	Makes an ISO compatible datetime string
	dtISO = dtb.buildISODateTime()

	#	Debugging print
	print(dtISO)

	#	Creates a request using the ISO compatible datetime string
	rb = RequestBuilder.RequestBuilder(token=token, isoDateTime=dtISO)

	#	Makes the request class
	req = rb.build()

	#	Creates an object that can send requests and recieve responses
	rh = RequestHandler.RequestHandler(request=req)

	#	Sends the request ands waits a response
	rh.send()

	#	Takes the response and opens it as a dict
	foo = rh.loadResponse()

	bar = foo["data"]["search"]["edges"][0]["node"]

	print(bar)
	# # Writes the response to a file for storage
	# with open("test.json", "w") as file:
	# 	file.write(str(foo))
	# 	file.close()

	# return None
	
program(token=sys.argv[1])