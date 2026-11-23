temperature = 70
while temperature <=90:
    if temperature >=90:
        print("System stopped")
        break
    elif temperature >= 80:
        print ("High temperature alarm")
    else:
        print("Temperature is normal")
    temperature = temperature + 5