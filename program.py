import datetime
import sys
sys.path.append("/NicholasSynovic/")

from NicholasSynovic import DateTimeBuilder
from NicholasSynovic import RequestBuilder
from NicholasSynovic import RequestHandler

def askIntQuestion(question:str, lowerBound:int, upperBound:int)	->	int:
	while True:
		try:
			response = int(input(question))
			if response < lowerBound:
				raise ValueError
			if response > upperBound:
				raise ValueError
			return response
		except ValueError:
			print("Invalid input.\nInput a number between the constraints.\n")
	
def askBoolQuestion(question:str)	->	bool:
	while True:
		try:
			response = input(question).lower().strip().replace(" ", "")
			if response == "yes":
				return True
			if response == "no":
				return False
			else:
				raise ValueError
		except ValueError:
			print("Invalid input.\nInput a number between the constraints.\n")

def program(token:str="", iterateDays:bool=True, iterateHours:bool=True, iterateMinutes:bool=False, minuteSpacing:int=15)	->	None:
	# Stores the current datetime inf
	currentDate = datetime.datetime.now()

	datetimeQuestion = lambda datetimePosition, datetimeValue: "What %s do you want the program to search repositories from? (2000 - %s)? " % (datetimePosition, str(datetimeValue))
	checkQuestion = lambda datetimePosition: "Do you want the program to search for repositories starting at a specific %s (yes/no)? " % (datetimePosition)

	# User input for getting the datetime inforation
	year = askIntQuestion(question=datetimeQuestion("year", currentDate.year))
	month = askIntQuestion(question=datetimeQuestion("month", currentDate.month))
	day = askIntQuestion(question=datetimeQuestion("day", currentDate.day))

	# Checks if the user wants to collect repositories by the hour
	if askBoolQuestion(question=checkQuestion("hour")):
		hour = askIntQuestion(question=datetimeQuestion(datetimePosition="hour", datetimeValue=currentDate.hour))
	else:
		hour = None
	
	# Checks if the user wants to collect repositories by the minute
	if askBoolQuestion(question=checkQuestion(datetimePosition="minute")):
		minute = askIntQuestion(question=datetimeQuestion(datetimePosition="minute", datetimeValue=currentDate.minute))
	else:
		minute = None

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