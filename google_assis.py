import requests
from bs4 import BeautifulSoup

def query():
    
    user_query = input('Enter your query: ')

    URL = "https://www.google.co.in/search?q=" + user_query

    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
    }

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find(class_='Z0LcW XcVN5d').get_text()
    print(result)

while True:
    try:
        query()
    except Exception:
        print('Sorry no result, please be clear')
    user_input = input('To continue press y: ')
    if user_input != 'y':
        break

# year of first fifa world cup
# age of ronaldo
# height of burj khalifa
# when was leonardo di vinci born
# prime minister of uk
# what is the weight of earth