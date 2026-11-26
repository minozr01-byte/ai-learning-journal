def check_temperature(temp,limit=80):
    if temp >= limit:
        print ("High temperature alarm")
    else:
        print ("Temperature is normal")
check_temperature(75)
check_temperature(85,90)