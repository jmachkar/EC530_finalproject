import requests
# import json

# BASE = 'http://127.0.0.1:5000'

# dan = {
#     'firstName': 'Daniel',
#     'lastName': 'Cabrera',
#     'username': 'dcabrera',
#     'password': 'password',
#     'role': 'student'
# }
# john = {
#     'firstName': 'John',
#     'lastName': 'Mikulskis',
#     'username': 'jmikulskis',
#     'password': 'password',
#     'role': 'student'
# }
# marco = {
#     'firstName': 'Marco',
#     'lastName': 'Achkar',
#     'username': 'jachkar',
#     'password': 'password',
#     'role': 'student'
# }
# osama = {
#     'firstName': 'Osama',
#     'lastName': 'GOAT',
#     'username': 'osama',
#     'password': 'password',
#     'role': 'Teacher'
# }

# print('users are added')
# response = requests.post(BASE + '/users/', json = dan)
# print(response.json())
# response = requests.post(BASE + '/users/', json = john)
# print(response.json())
# response = requests.post(BASE + '/users/', json = marco)
# print(response.json())
# response = requests.post(BASE + '/users/', json = osama)
# print(response.json())

# print('osama gets added again')
# response = requests.post(BASE + '/users/', json = osama)
# print(response.json())

# # start a convo
# print('osama starts conversation')
# convo = {
#     'name': 'EC530',
#     'username': 'osama',
#     'password': 'password'
# }
# EC530 = requests.post(BASE + '/conversations/', json = convo)
# print(EC530.json())

# # add users to the convo
# print('osama adds daniel')
# participant = {
#     'admin': 'osama',
#     'password': 'password',
#     'participant': 'dcabrera',
#     'conversationID': EC530.json()['ID']
# }
# response = requests.post(BASE + '/participants/', json = participant)
# print(response.json())

# print('osama adds marco')
# participant['participant'] = 'jachkar'
# response = requests.post(BASE + '/participants/', json = participant)
# print(response.json())

# print('osama thinks he adds john but adds marco again')
# response = requests.post(BASE + '/participants/', json = participant)
# print(response.json())

# print('osama posts msg to convo')
# msg = {
#     'username': 'osama',
#     'password': 'password',
#     'conversationID': EC530.json()['ID'],
#     'content': 'oops john was not added'
# }
# response = requests.post(BASE + '/messages/', json = msg)
# print(response.json())

# print('osama adds john')
# participant['participant'] = 'jmikulskis'
# response = requests.post(BASE + '/participants/', json = participant)
# print(response)

# print('osama posts msg to convo')
# msg['content'] = 'Ok, welcome to EC530!'
# response = requests.post(BASE + '/messages/', json = msg)
# print(response.json())

# print('daniel opens EC530')
# query = {
#     'username':'dcabrera',
#     'password':'password',
#     'conversationID':EC530.json()['ID']
# }
# response = requests.get(BASE + '/messages/', json = query)
# print(response.json())

# print('john opens EC530')
# query['username'] = 'jmikulskis'
# response = requests.get(BASE + '/messages/', json = query)
# print(response.json())

# # new conversation
# print('daniel starts a convo')
# convo = {
#     'name': 'Procrastinators',
#     'username': 'dcabrera',
#     'password': 'password'
# }
# groupchat = requests.post(BASE + '/conversations/', json = convo)
# print(groupchat.json())

# print('daniel adds marco and john')
# participant = {
#     'admin': 'dcabrera',
#     'password': 'password',
#     'participant': 'jachkar',
#     'conversationID': groupchat.json()['ID']
# }
# response = requests.post(BASE + '/participants/', json = participant)
# print(response.json())

# participant['participant'] = 'jmikulskis'
# response = requests.post(BASE + '/participants/', json = participant)
# print(response.json())

# print('daniel posts msg to convo')
# msg = {
#     'username': 'dcabrera',
#     'password': 'password',
#     'conversationID': groupchat.json()['ID'],
#     'content': 'I might drop this class'
# }
# response = requests.post(BASE + '/messages/', json = msg)
# print(response.json())

# print('marco checks all his conversations')
# convQuery = {
#     'username': 'jachkar',
#     'password': 'password'
# }
# response = requests.get(BASE + '/conversations/', json = convQuery)
# print(response.json())
BASE = 'http://127.0.0.1:5000'
response = requests.get(BASE + '/users/dcabrera/password')
print(response.json())
