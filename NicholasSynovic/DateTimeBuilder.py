import datetime

class DateTimeBuilder:

	def __init__(self, year:int=2020, month:int=1, day:int=1, hour:int=0, minute:int=0)	->	None:
		self.year = year
		self.month = month
		self.day = day
		self.hour = hour
		self.minute = minute

	def buildDateTime(self)	->	datetime.datetime:
		return datetime.datetime(year=self.year, month=self.month, day=self.day, hour=self.hour, minute=self.minute)

	def buildISODateTime(self)	->	str:
		return self.buildDateTime().isoformat()

	def getDay(self)	->	int:
		return self.day

	def getHour(self)	->	int:
		return self.hour

	def getMinute(self)	->	int:
		return self.minute

	def getMonth(self)	->	int:
		return self.month

	def getYear(self)	->	int:
		return self.year

	def incrementMinute(self, datetime:datetime.datetime)	->	datetime.datetime:
		try:
			return datetime.replace(minute=datetime.minute + 1)
		except ValueError:
			foo = self.incrementHour(datetime=datetime)
			return foo.replace(minute=0)
	
	def incrementHour(self, datetime:datetime.datetime)	->	datetime.datetime:
		try:
			return datetime.replace(hour=datetime.hour + 1)
		except ValueError:
			foo = self.incrementDay(datetime=datetime)
			return foo.replace(hour=0)

	def incrementDay(self, datetime:datetime.datetime)	->	datetime.datetime:
		try:
			return datetime.replace(day=datetime.day + 1)
		except ValueError:
			foo = self.incrementMonth(datetime=datetime)
			return foo.replace(day=1)

	def incrementMonth(self, datetime:datetime.datetime)	->	datetime.datetime:
		try:
			return datetime.replace(month=datetime.month + 1)
		except ValueError:
			foo = self.incrementYear(datetime=datetime)
			return foo.replace(month=1)

	def incrementYear(self, datetime:datetime.datetime)	->	datetime.datetime:
		return datetime.replace(year=datetime.year + 1)

	def setDay(self, day:int=1)	->	None:
		self.day = day
	
	def setHour(self, hour:int=0)	->	None:
		self.hour = hour

	def setMinute(self, minute:int=0)	->	None:
		self.minute = minute

	def setMonth(self, month:int=1)	->	None:
		self.month = month

	def setYear(self, year:int=2020)	->	None:
		self.year = year