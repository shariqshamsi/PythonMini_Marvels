import phonenumbers
from phonenumbers import timezone, geocoder, carrier
number = input("Enter your No. with complete country code like +__ : ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
network = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")
print(phone)
print(time)
print(network)
print(reg)