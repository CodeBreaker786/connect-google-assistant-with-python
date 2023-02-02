from datetime import datetime

def time_in_range(start, end, current):
    return start <= current <= end


def timeStrToTime(time):
    return datetime.strptime(time.strip(),'%H:%M').time()




questionAnswer={
    'Who is the principal of ATHS Ras Al Khaima?':' Dr. Naser Alsab',
    'In which block will is 11 CAI': ' B Block',
    'When will the end of term 3 exams be? ':' We are still not sure when will it be but we will keep you updated',
    'when does term 2 student vacation start?': '27/3/2023',
    'when will the report cards be announced?  ' :' We are still not sure when will it be but we will keep you updated',
    'How many majors are in ATHS RAK?' : 'There are ASP, Advance, General, ENI, CAI, AET, AEA',
    'someone is bullying me. What should I do?' : 'You can visit the student counsellor at B block',    
    }