import datetime
import calendar
from dateutil.relativedelta import relativedelta

class DateTimeBuilder:
	'''
A class to handle the creation and manipulation of datetimes. 
	'''
	def __init__(self, year:int=2020, month:int=1, day:int=1, hour:int=0, minute:int=0)	->	None:
		'''
Starts an instance of the class.\nAll arguements can be changed using getter and setter methods.\n
:param year: An int that represents the year portion of a datetime object.\n
:param month: An int that represents the month portion of a datetime object.\nCan only be 1 - 12.\n
:param day: An int that represents the day portion of a datetime object.\nCan only be 1 - 31 assuming that the month has 31 days.\n
:param hour: An int that represents the hour portion of a datetime object.\nCan only be 0 - 23.\n
:param minute: An int that represents the minute poriton of a datetime object.\nCan only be 0 - 59.\n
Attempting to initalize this class with invalid arguements will not cause the class to not initialize.\nHowever executing any methods (aside from getters and setters) will result in potentially wrong or invalid outputs. 
		'''
		self.year = year
		self.month = month
		self.day = day
		self.hour = hour
		self.minute = minute

	def buildDateTime(self)	->	datetime.datetime:
		'''
Creates a datetime object utilizing the year, month, day, hour, and minute values provided in the initalization of the class or the updated values.
		'''
		try:
			return datetime.datetime(year=self.year, month=self.month, day=self.day, hour=self.hour, minute=self.minute)
		except ValueError as error:
			print(error)

	def buildISODateTime(self, dt:datetime.datetime=None)	->	str:
		'''
Creates an ISO compatible datetime string from the values provided in the initalization of the class, updated values, or from a already made datetime object.
:param dt: An optional datetime object.
		'''
		if dt is None:
			return self.buildDateTime().isoformat()[0:-3]
		else:
			return dt.isoformat()[0:-3]

	def getDay(self)	->	int:
		'''
Return the current value of the class variable day.
		'''
		return self.day

	def getHour(self)	->	int:
		'''
Return the current value of the class variable hour.
		'''
		return self.hour

	def getMinute(self)	->	int:
		'''
Return the current value of the class variable minute.
		'''
		return self.minute

	def getMonth(self)	->	int:
		'''
Return the current value of the class variable month.
		'''
		return self.month

	def getYear(self)	->	int:
		'''
Return the current value of the class variable year.
		'''
		return self.year

	def incrementDay(self, dt:datetime.datetime)	->	datetime.datetime:
		'''
Increments the day of a datetime object by one and returns a new object.
:param dt: A datetime object.
		'''
		return dt + datetime.timedelta(days=1)
	
	def incrementDayByAmount(self, dt:datetime.datetime, amount:int)	->	datetime.datetime:
		return dt + datetime.timedelta(days=amount)

	def incrementHour(self, dt:datetime.datetime)	->	datetime.datetime:
		'''
Increments the hour of a datetime object by one.
:param dt: A datetime object.
		'''
		return dt + datetime.timedelta(hours=1)

	def incrementHourByAmount(self, dt:datetime.datetime, amount:int)	->	datetime.datetime:
		return dt + datetime.timedelta(hours=amount)

	def incrementMinute(self, dt:datetime.datetime)	->	datetime.datetime:
		'''
Increments the minute of a datetime object by one.
:param dt: A datetime object.
		'''
		return dt + datetime.timedelta(minutes=1)

	def incrementMinuteByAmount(self, dt:datetime.datetime, amount:int)	->	datetime.datetime:
		return dt + datetime.timedelta(minutes=amount)

	def incrementMonth(self, dt:datetime.datetime)	->	datetime.datetime:	#	TODO: Convert this into standard python
		'''
Increments the month of a datetime object by one.
:param dt: A datetime object.
		'''
		return dt + relativedelta(months=1)
	
	def incrementMonthByAmount(self, dt:datetime.datetime, amount:int)	->	datetime.datetime:	#	TODO: Convert this into standard python
		return dt + relativedelta(months=amount)

	def incrementYear(self, dt:datetime.datetime)	->	datetime.datetime:
		'''
Increments the year of a datetime object by one.
:param dt: A datetime object.
		'''
		return dt.replace(year=dt.year + 1)

	def incrementYearByAmount(self, dt:datetime.datetime, amount:int)	->	datetime.datetime:
		return dt.replace(year=dt.year + amount)

	def setDay(self, day:int=1)	->	None:
		'''
Changes the current value of the class variable day to a different value.
:param day: An int that represents the day portion of a datetime object.\nCan only be 1 - 31 assuming that the month has 31 days.
		'''
		self.day = day
	
	def setHour(self, hour:int=0)	->	None:
		'''
Changes the current value of the class variable hour to a different value.
:param hour: An int that represents the hour portion of a datetime object.\nCan only be 0 - 23.\n
		'''
		self.hour = hour

	def setMinute(self, minute:int=0)	->	None:
		'''
Changes the current value of the class variable minute to a different value.
:param minute: An int that represents the minute poriton of a datetime object.\nCan only be 0 - 59.\n
		'''
		self.minute = minute

	def setMonth(self, month:int=1)	->	None:
		'''
Changes the current value of the class variable month to a different value.
:param month: An int that represents the month portion of a datetime object.\nCan only be 1 - 12.\n
		'''
		self.month = month

	def setYear(self, year:int=2020)	->	None:
		'''
Changes the current value of the class variable year to a different value.
:param year: An int that represents the year portion of a datetime object.\n
		'''
		self.year = year


	def createNewDatetimeFromOld(self, oldDatetime:datetime.datetime, **kwargs)	->	datetime.datetime:	#	TODO: Move this into DateTimeBuilder at some point
		'''
This utilizes the current datetime stored in self.datetime and returns a new datetime utilizing the current one as a base.
		'''
		if "year" in kwargs:
			oldDatetime.replace(year=int(kwargs["year"]))
		if "month" in kwargs:
			oldDatetime.replace(month=int(kwargs["month"]))
		if "day" in kwargs:
			oldDatetime.replace(day=int(kwargs["day"]))
		if "hour" in kwargs:
			oldDatetime.replace(hour=int(kwargs["hour"]))
		if "minute" in kwargs:
			oldDatetime.replace(minute=int(kwargs["minute"]))

		print(kwargs)
		return oldDatetime