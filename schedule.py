from datetime import datetime as date
from utils import time_in_range,timeStrToTime
import datetime
import csv


# current_time=date.today().time().strftime("%H:%M")
current_time=datetime.time(11,15)
day=date.today().strftime("%A")







def get_lecture_info():
    with open('schedule.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if 'Sunday'==day:
                return "There is no lecture on sunday"
                

            if row['Days']==day:
                row.pop('Days')
                st = timeStrToTime(list(row.keys())[0].split('-')[0])
                et= timeStrToTime(list(row.keys())[-1].split('-')[1]) 
                if not time_in_range(start=st,end=et,current=current_time):
                   return "At that time No lecture is going on"

                for time,data in row.items():
                    start_time,end_time=time.split('-')
                    if time_in_range(start=timeStrToTime(start_time),end=timeStrToTime(end_time),current=current_time)==True:
                        if data.__contains__('Break'):
                            return f"Right now {data} is going on"
                        subject,teacher=data.split('-')
                        return  f"Lecture of subject {subject} with {teacher} is going on"

                    
                
                 




