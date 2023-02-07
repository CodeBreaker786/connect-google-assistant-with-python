from datetime import datetime

def time_in_range(start, end, current):
    return start <= current <= end


def timeStrToTime(time):
    return datetime.strptime(time.strip(),'%H:%M').time()




questionAnswer={
    'principal':' Dr. Naser Alsab',
    'block': ' B Block',
    'term 3 exams be':' We are still not sure when will it be but we will keep you updated',
    'vacation start': '27/3/2023',
    'report cards' :' We are still not sure when will it be but we will keep you updated',
    'how many majors are' : 'There are ASP, Advance, General, ENI, CAI, AET, AEA',
    'what should I do' : 'You can visit the student counsellor at B block',    
    }