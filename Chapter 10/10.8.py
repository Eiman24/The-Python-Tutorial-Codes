from datetime import date

now = date.today()
print(now)

datestr = now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
print(datestr)

birthday = date(1992, 7, 30)
age = now - birthday
print(age.days)
print(age)