import phonenumbers as ph
from phonenumbers import timezone,geocoder,carrier

number=int(input("enter your number with +__ : "))
phone=ph.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(reg)