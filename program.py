import datetime
import calendar
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
	#	Initalizes DateTimeBuilder class
	dtb = DateTimeBuilder.DateTimeBuilder()
	rb = RequestBuilder.RequestBuilder(token=token)
	
	#	Stores the current datetime info
	currentDate = datetime.datetime.now()

	datetimeQuestion = lambda datetimePosition, lowerBound, upperBound: "What %s do you want the program to search repositories from? (%s - %s)? " % (datetimePosition, str(lowerBound), str(upperBound))
	checkQuestion = lambda datetimePosition: "Do you want the program to search for repositories starting at a specific %s (yes/no)? " % (datetimePosition)

	#	User input for getting the datetime inforation
	year = askIntQuestion(question=datetimeQuestion(datetimePosition="year", lowerBound=2000, upperBound=currentDate.year), lowerBound=2000, upperBound=currentDate.year)

	if year == currentDate.year:
		month = askIntQuestion(question=datetimeQuestion(datetimePosition="month", lowerBound=1, upperBound=currentDate.month), lowerBound=1, upperBound=currentDate.month)

		if month == currentDate.month:
			if currentDate.day == 1:
				day = 1
			else:
				day = askIntQuestion(question=datetimeQuestion(datetimePosition="day", lowerBound=1, upperBound=currentDate.day), lowerBound=1, upperBound=currentDate.day)
		
		else:
			day = askIntQuestion(question=datetimeQuestion(datetimePosition="day", lowerBound=1, upperBound=calendar.monthrange(year=year, month=month)[1]), lowerBound=1, upperBound=calendar.monthrange(year=year, month=month)[1])
	
	else:
		month = askIntQuestion(question=datetimeQuestion(datetimePosition="month", lowerBound=1, upperBound=12), lowerBound=1, upperBound=12)

		day = askIntQuestion(question=datetimeQuestion(datetimePosition="day", lowerBound=1, upperBound=calendar.monthrange(year=year, month=month)[1]), lowerBound=1, upperBound=calendar.monthrange(year=year, month=month)[1])

	#	Checks if the user wants to collect repositories by the hour
	if [year, month, day] == [currentDate.year, currentDate.month, currentDate.day]:
		if currentDate.hour == 0:
			hour = 0
		else:
			if askBoolQuestion(question=checkQuestion("hour")):
				if currentDate.hour == 0:
					hour = askIntQuestion(datetimeQuestion("hour", 0, 23), 0, 23)
				else:	
					hour = askIntQuestion(datetimeQuestion("hour", 0, currentDate.hour), 0, currentDate.hour)
			else:
				hour = 0
	else:
		hour = askIntQuestion(datetimeQuestion("hour", 0, 23), 0, 23)
	
	#	Checks if the user wants to collect repositories by the minute
	if hour == currentDate.hour:
		if currentDate.minute == 0:
			minute = 0
		else:
			if askBoolQuestion(checkQuestion("minute")):
				if currentDate.hour == 0:
					minute = askIntQuestion(datetimeQuestion("minute", 0, 59), 0, 59)
				else:	
					minute = askIntQuestion(datetimeQuestion("minute", 0, currentDate.minute), 0, currentDate.minute)
			else:
				minute = 0
	else:
		minute = askIntQuestion(datetimeQuestion("minute", 0, 59), 0, 59)

	#	Sets the values of the FIRST datetime to be searched for
	dtb.setYear(year=year)
	dtb.setMonth(month=month)
	dtb.setDay(day=day)

	if hour is not None:
		dtb.setHour(hour=hour)
	
	if minute is not None:
		dtb.setMinute(minute=minute)

	while True:
		# Makes a datetime object
		dt = dtb.buildDateTime()
		isoDT = dtb.buildISODateTime(dt=dt)
		
		#	Debugging print
		print(str(dt) + " is the datetime object")
		print(isoDT + " is the ISO datetime string")

		rb.setDatetime(datetime=dt)
		print("Set RequestBuilder datetime to " + str(dt))

		print(dtb.incrementDay(dt))

		break
	
program(token=sys.argv[1])