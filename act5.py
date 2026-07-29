import datetime  
import calendar   
# using now() to get current time  
current_time = datetime.datetime.now()  
    
# Printing value of now.  
print("Time now at : ", end = " ")   
print(current_time)

# print calendar of year 2021

print("\n", calendar.calendar(2025))