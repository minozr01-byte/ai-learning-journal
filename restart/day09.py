def check_temperature(temp,limit=80):
    if temp >= limit:
        return ("Alarm")
    else:
        return ("Normal")
def show_temperature_status(temp, limit=80):
    status = check_temperature(temp, limit)
    print(f"Temperature: {temp}, Status: {status}")
show_temperature_status(85)
show_temperature_status(75,70)