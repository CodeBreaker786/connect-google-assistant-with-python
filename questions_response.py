from utils import questionAnswer

def get_question_response(question):
    answer=questionAnswer.get(question)
    if answer!=None:
        return answer
    return None
     
    