def check_temperature(temp):
    if temp <20:
        return "it's cold"
    elif temp<=60:
        return "Normal"
    else:
        return"Too hot"
temp=float(input("Enter the temperature:"))
result=check_temperature(temp)
print (result)
