from os import  getcwd, chdir, mkdir
from os.path import isdir
import datetime
import calendar
import sys

sys.path.append("/libs/")

from libs import DateTimeBuilder
from libs import RequestBuilder
from libs import RequestHandler

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

def makeFolder(dir:str)	->	bool:
	try: 
		if not isdir(dir):
			mkdir(dir)
	except OSError:
		pass
	return True
		
def program(token:str="", iterateDays:bool=True, iterateHours:bool=True, iterateMinutes:bool=False, minuteSpacing:int=15)	->	None:
	#	Initalizes DateTimeBuilder class
	dtb = DateTimeBuilder.DateTimeBuilder()
	rb = RequestBuilder.RequestBuilder(token=token)
	rh = RequestHandler.RequestHandler()
	
	# Creates/Check for the output path
	makeFolder(dir="output")
	makeFolder(dir="output/unprocessed")
	makeFolder(dir="output/processed")

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
		if askBoolQuestion(question=checkQuestion("hour")):
			hour = askIntQuestion(datetimeQuestion("hour", 0, 23), 0, 23)
		else:
			hour = 0
	
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
		if askBoolQuestion(question=checkQuestion("minute")):
			minute = askIntQuestion(datetimeQuestion("minute", 0, 59), 0, 59)
		else:
			minute = 0

	#	Sets the values of the FIRST datetime to be searched for
	dtb.setYear(year=year)
	dtb.setMonth(month=month)
	dtb.setDay(day=day)

	if hour is not None:
		dtb.setHour(hour=hour)
	
	if minute is not None:
		dtb.setMinute(minute=minute)

	dt = dtb.buildDateTime()

	print("\n")

	folderLoop = 0	# This is meant to stop creating duplicate folders and reduce processing time
	rootDir = getcwd()
	currentSavingDir = ""
	while True:
		# 	Makes a datetime object that is incremented by 15 minutes
		newDT = dtb.incrementMinuteByAmount(dt, 15)
		
		#	Makes ISO compatible datetime strings
		isoDT = dtb.buildISODateTime(dt=dt)
		newISODT = dtb.buildISODateTime(dt=newDT)
		
		#	Makes a folder containing only files from a specific day in the unproccessed folder dir
		if folderLoop == 0:
			currentSavingDir = "output/unprocessed/" + str(dt.year) + "-" + str(dt.month) + "-" + str(dt.day)
			makeFolder(dir=currentSavingDir)
			chdir(currentSavingDir)
			folderLoop = 1
			print("Created folder " + currentSavingDir)
		else:
			if (newDT.year > dt.year) or (newDT.month > dt.month) or (newDT.day > dt.day):
				currentSavingDir = "output/unprocessed/" + str(newDT.year) + "-" + str(newDT.month) + "-" + str(newDT.day)
				chdir(rootDir)
				makeFolder(dir=currentSavingDir)
				chdir(currentSavingDir)
				folderLoop = 1
				print("Created folder " + currentSavingDir)

		#	Debugging prints
		print(str(dt) + " is the original datetime object")
		print(str(newDT) + " is the updated datetime object")
		print(isoDT + " is the ISO datetime string")
		print(newISODT + " is the updated ISO datetime string")
		
		#	Create the request
		req = rb.build(isoDatetimeSTART=isoDT, isoDatetimeEND=newISODT)

		print("Created GitHub GraphQL request object")
		print("Sending request...")
		
		rh.send(req)

		response = rh.loadResponse()

		fn = isoDT + "-" + newISODT + ".txt"

		with open(fn, "w") as file:

			root = response["data"]["search"]["pageInfo"]
			lineList = [isoDT, newISODT, str(root["hasNextPage"]), str(root["endCursor"])]
			line = ', '.join(lineList) + "\n"
			file.write(line)

			for x in response["data"]["search"]["edges"]:
				root = x["node"]
				# Created at, username, repository, commits, issues, pull
				lineList = [root["createdAt"], root["nameWithOwner"].split("/")[0], root["nameWithOwner"].split("/")[1], str(root["defaultBranchRef"]["target"]["history"]["totalCount"]), str(root["issues"]["totalCount"]), str(root["pullRequests"]["totalCount"])]
				line = ', '.join(lineList) + "\n"
				file.write(line)

			file.close()
		if newDT >= datetime.datetime.now():
			break
		else:
			dt = newDT
	
program(token=sys.argv[1])