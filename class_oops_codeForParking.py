# coding for the parking system
# for week days mon-fri
# 8am-2pm charge = 2rs/hr
# 2pm-10pm charge = 4rs/hr
# for weeekend
# sat-sun
# 8am-2pm charge = 4rs/hr
# 2pm-10pm charge = 10rs/hr
# after 10pm - 8am they will not allow to be park
# create a coupon code
# code will be 6 digit number
# sum of all 6 digit number is even then code is valid
# then discount of 2rs
# time validation
# date validation
# code vaidation

class Parking:
    when_you_parked = input("Have u parked your car on weekdays(Y/N):  ")
    initial_time = int(input("Enter parked In time(24hrs):  "))
    finial_time = int(input("Enter parked Out time(24hrs):  "))
    code_validation = input("Do You Have Coupne(Y/N):  ")
    coupon_code = int(input("Enter the coupne code:  "))

    def __init__(self):
        self.at_8am_to_2pm_weekdays = (self.finial_time - self.initial_time)*2
        self.at_2pm_to_10pm_weekdays = (self.finial_time - self.initial_time)*4
        self.at_8am_to_2pm_weekend = (self.finial_time - self.initial_time)*4
        self.at_2pm_to_10pm_weekend = (self.finial_time - self.initial_time)*10

    def weekday_parked(self):
        if self.coupon_code//2 == 0 and self.code_validation[0].lower() == "y":
            if self.when_you_parked[0].lower() == "y":
                if self.initial_time >= 8 and self.finial_time < 14:
                    print(f"Charge of weekdays 8am to 2pm:  \n with discount {self.at_8am_to_2pm_weekdays -2}")
                elif self.initial_time >= 15 and self.finial_time < 22:
                    print(f"Charge of weekdays 2pm to 10pm: \n with discount {self.at_2pm_to_10pm_weekdays -2}")
                else:
                    print("!!!!!!!Time is not valid!!!!!!!")
        else:
            if self.when_you_parked[0].lower() == "y":
                if self.initial_time >= 8 and self.finial_time < 14:
                    print(f"Charge of weekdays 8am to 2pm:  {self.at_8am_to_2pm_weekdays - 2}")
                elif self.initial_time >= 15 and self.finial_time < 22:
                    print(f"Charge of weekdays 2pm to 10pm: {self.at_2pm_to_10pm_weekdays - 2}")
                else:
                    print("!!!!!!!Time is not valid!!!!!!!")

    def weekend_parked(self):
        if self.coupon_code//2 == 0 and self.code_validation[0].lower() == "y":
            if self.when_you_parked[0].lower() == "n":
                if self.initial_time >= 8 and self.finial_time < 14:
                    print(f"Charge of weekend 8am to 2pm:  \n with discount {self.at_8am_to_2pm_weekend - 2}")
                elif self.initial_time >= 15 and self.finial_time < 22:
                    print(f"Charge of weekend 2pm to 10pm: \n with discount {self.at_2pm_to_10pm_weekend - 2}")
                else:
                    print("!!!!!!!Time is not Input!!!!!!!")
        else:
            if self.when_you_parked[0].lower() == "n":
                if self.initial_time >= 8 and self.finial_time < 14:
                    print(f"Charge of weekend 8am to 2pm:  {self.at_8am_to_2pm_weekend}")
                elif self.initial_time >= 15 and self.finial_time < 22:
                    print(f"Charge of weekend 2pm to 10pm: {self.at_2pm_to_10pm_weekend}")
                else:
                    print("!!!!!!!Time is not Input!!!!!!!")
p = Parking()
p.weekday_parked()
p.weekend_parked()

            



