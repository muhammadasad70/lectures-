daysb,monthb,yearb=eval(input("enter your date of birth"))
daysp,monthp,yearp=eval(input("enter the present date"))
year=yearp-yearb-1
months=(12-monthb)+monthp-1
days=(30-daysb)+daysp-1
print("your age",days,"days",months,"months",year,"year")
