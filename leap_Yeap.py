def isleapyear(year):
    if year%4==0:
        return True
    elif year%100==0 and year%400==0:
        return True
    else:
        return False
year= int(input("enter a year"))
print(isleapyear(year))