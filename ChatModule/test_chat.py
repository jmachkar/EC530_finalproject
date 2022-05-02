import requests

BASE = 'http://127.0.0.1:5000'

dan = {
    'firstName': 'Daniel',
    'lastName': 'Cabrera',
    'role': 'student'
}
john = {
    'firstName': 'John',
    'lastName': 'Mikulskis',
    'role': 'student'
}
marco = {
    'firstName': 'Marco',
    'lastName': 'Achkar',
    'role': 'student'
}
osama = {
    'firstName': 'Osama',
    'lastName': 'GOAT',
    'role': 'Teacher'
}

print('users are added')
response = requests.post(BASE + '/users/dcabrera/password', json = dan)
print(response.json())
response = requests.post(BASE + '/users/jmikulskis/password', json = john)
print(response.json())
response = requests.post(BASE + '/users/jachkar/password', json = marco)
print(response.json())
response = requests.post(BASE + '/users/osama/password', json = osama)
print(response.json())
response = requests.post(BASE + '/users/osama/password', json = osama)
print(response.json())

# start a convo
print('osama starts conversation')
convo = {'name': 'EC530'}
EC530 = requests.post(BASE + '/conversations/osama/password', json = convo)
print(EC530.json())

# add users to the convo
print('osama adds daniel')
participant = {'participant': 'dcabrera'}
response = requests.post(BASE + '/participants/osama/password/' + str(EC530.json()['ID']), json = participant)
print(response.json())

print('osama adds marco')
participant['participant'] = 'jachkar'
response = requests.post(BASE + '/participants/osama/password/' + str(EC530.json()['ID']), json = participant)
print(response.json())

print('osama thinks he adds john but adds marco again')
response = requests.post(BASE + '/participants/osama/password/' + str(EC530.json()['ID']), json = participant)
print(response.json())

print('osama posts msg to convo')
msg = {'content': 'oops john was not added'}
response = requests.post(BASE + '/messages/osama/password/' + str(EC530.json()['ID']), json = msg)
print(response.json())

print('osama adds john')
participant['participant'] = 'jmikulskis'
response = requests.post(BASE + '/participants/osama/password/' + str(EC530.json()['ID']), json = participant)
print(response.json())

print('osama posts msg to convo')
msg['content'] = 'Ok, welcome to EC530!'
response = requests.post(BASE + '/messages/osama/password/' + str(EC530.json()['ID']), json = participant)
print(response.json())

print('daniel opens EC530')
response = requests.get(BASE + '/messages/dcabrera/password/'+ str(EC530.json()['ID']))
print(response.json())

print('john opens EC530')
response = requests.get(BASE + '/messages/jmikulskis/password/'+ str(EC530.json()['ID']))
print(response.json())

# new conversation
print('daniel starts a convo')
convo = {'name': 'Procrastinators'}
groupchat = requests.post(BASE + '/conversations/dcabrera/password', json = convo)
print(groupchat.json())

print('daniel adds marco and john')
participant = {'participant': 'jachkar'}
response = requests.post(BASE + '/participants/dcabrera/password/' + str(groupchat.json()['ID']), json = participant)
print(response.json())

participant['participant'] = 'jmikulskis'
response = requests.post(BASE + '/participants/dcabrera/password/' + str(groupchat.json()['ID']), json = participant)
print(response.json())

print('daniel posts msg to convo')
msg = {'content': 'I might drop this class'}
response = requests.post(BASE + '/messages/dcabrera/password/' + str(groupchat.json()['ID']), json = msg)
print(response.json())

print('marco checks all his conversations')
response = requests.get(BASE + '/conversations/jachkar/password')
print(response.json())
