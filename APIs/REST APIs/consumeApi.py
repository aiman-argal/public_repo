import requests
import json

response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')


#Easy try to see if we can access some of the data correctly
for questions in response.json()['items']:
    if questions['answer_count']==0:
        #Returning all the unanswered questions in stackOverflow
        print(questions['title'])
        any_unanswered = True

if not any_unanswered:
    print('All the questions have been answered here :)')
        
    
#Make a count and a ranking of the different users who ask questions
owners = {}
for questions in response.json()['items']:
    account_id = questions['owner']['account_id']
    if account_id in owners:
        owners[account_id]+=1
    else:
        owners[account_id] = 1
        
sorted_owners = dict(sorted(owners.items(), key=lambda item: item[1]))
    
print(sorted_owners)
    