import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('./serviceAccountKey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
test_ref = db.collection(u'test')
docs = test_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
