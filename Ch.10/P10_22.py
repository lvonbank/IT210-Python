# Levi VonBank

## Creates a class Appointment to manage schedule
class Appointment:
    def __init__(self, description, year, month, day):
        self._description = str(description)
        self._year = str(year)
        self._month = str(month)
        self._day = str(day)
    
    # Abstract method for Appointment
    def occursOn(self, year, month, day):
        raise NotImplemented
    
    ## Returns appointments description
    def getDescription(self):
        return self._description
    
    ## Returns appointments year
    def getYear(self):
        return self._year
    
    ## Returns appointments month
    def getMonth(self):
        return self._month
    
    ## Returns appointments day
    def getDay(self):
        return self._day
    
    ## A string representation of the Appointment
    def __repr__(self):
        return self._description

## Onetime are Appointment that happen once
class Onetime(Appointment):
    # Returns a True Boolean if day, month and year match-up
    def occursOn(self, year, month, day):
        if self.getYear() == str(year) \
        and self.getMonth() == str(month) \
        and self.getDay() == str(day):
            return True
        return False

## Daily are Appointment that happen everyday
class Daily(Appointment):
    # Returns a Boolean no mater what day, month or year
    def occursOn(self, year, month, day):
        return True

## Monthly are Appointment that happen on a given day of a given month
class Monthly(Appointment):
    # Returns a Boolean if day and month match-up
    def occursOn(self, year, month, day):
        if self.getMonth() == str(month) \
        and self.getDay() == str(day):
            return True
        return False


if __name__ == "__main__":
    appList = []
    appList.append(Onetime('Family Meeting', 2015, 11, 18))
    appList.append(Daily('Feed Dog', 2013, 12, 28))
    appList.append(Monthly('Dentist', 2008, 11, 18))
    
    # Tests a set of examples dates
    for year,month,day in [(2015, 11, 18),(2005, 11, 18),(2010, 10, 10)]:
        print("%d/%d/%d" %(month, day, year))
        for app in appList:
            if app.occursOn(year, month, day):
                print(" ", app)
        print()
    
    # Asks the user for a date (loop)
    day = input("Enter the day (Enter to quit): ")
    while day != "":
        month = input("Enter the month: ")
        year = input("Enter the year: ")
        print()
        for app in appList:
            if app.occursOn(year, month, day):
                print(app)
        day = input("Enter the day (Enter to quit): ")