import sys
sys.path.append("/NicholasSynovic/")

from NicholasSynovic import DateTimeBuilder
from NicholasSynovic import RequestBuilder
from NicholasSynovic import RequestHandler
	
def program(token:str="", iterateDays:bool=True, iterateHours:bool=True, iterateMinutes:bool=False, minuteSpacing:int=15)	->	None:
	#	Initalizes DateTimeBuilder class
	dtb = DateTimeBuilder.DateTimeBuilder()
	
	# User input for getting the datetime inforation
	year = int(input("What year do you want the program to start collecting repositories from? (2000 - )? "))
	month = int(input("What month do you want the program to start collecting repositories form? (1 - 12)? "))
	day = int(input("What day do you want the program to start collecting repositories from (1 - 28/29/31)? "))

	# Checks if the user wants to collect repositories by the hour
	check = input("Do you want to collect repositories within a specific hour (yes/no)? ").lower()
	if check == "yes":
		hour = int(input("What hour do you want the program to start collecting repositories from (0 - 23)? "))
	
	# Checks if the user wants to collect repositories by the minute
	check = input("Do you want to collect repositories within a specific minute (yes/no)? ").lower()
	if check == "yes":
		minute = int(input("What minute do you want the program to start collecting repositories from (0 - 23)? "))


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
	rb = RequestBuilder.RequestBuilder(token=token, isoDateTimeSTART=dtISO)

	#	Makes the request class
	req = rb.build(True, True)

	#	Creates an object that can send requests and recieve responses
	rh = RequestHandler.RequestHandler(request=req)

	#	Sends the request ands waits a response
	rh.send()

	#	Takes the response and opens it as a dict
	foo = rh.loadResponse()

	bar = foo["data"]["search"]["pageInfo"]["hasNextPage"]

	print(bar)
	# Writes the response to a file for storage
	with open("test.json", "w") as file:
		file.write(str(foo))
		file.close()

	return None
	
program(token=sys.argv[1])