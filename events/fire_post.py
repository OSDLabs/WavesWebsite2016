import json

from firebase import firebase
from firebase import jsonutil

# firebase = firebase.FirebaseApplication('https://waves-98c93.firebaseio.com/', None)
# data = {'name': 'Sebastin'}
# sent = json.dumps(data)
# result = firebase.post('/users', sent)

firebase = firebase.FirebaseApplication('https://waves-98c93.firebaseio.com/', None)
result = firebase.get('/users', None)

print(result)

