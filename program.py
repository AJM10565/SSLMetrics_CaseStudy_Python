import sys
sys.path.append("/NicholasSynovic/")

from NicholasSynovic import DateTimeBuilder
from NicholasSynovic import RequestBuilder
from NicholasSynovic import RequestHandler
	
def program(token:str="", iterateDays:bool=True, iterateHours:bool=True, iterateMinutes:bool=False, year:int=2020, month:int=1, day:int=1, hour:int=0, minute:int=0)	->	None:
	dtb = DateTimeBuilder.DateTimeBuilder()
	
	dtb.setYear(year=year)
	dtb.setMonth(month=month)
	dtb.setDay(day=day)
	dtb.setHour(hour=hour)
	dtb.setMinute(minute=minute)

	dtISO = dtb.buildISODateTime()

	print(dtISO)

	rb = RequestBuilder.RequestBuilder(token=token, isoDateTime=dtISO)

	req = rb.build()

	rh = RequestHandler.RequestHandler(request=req)

	rh.send()

	foo = rh.loadResponse()

	with open("test.json", "w") as file:
		file.write(str(foo))
		file.close()

	return None
	
program(token=sys.argv[1])