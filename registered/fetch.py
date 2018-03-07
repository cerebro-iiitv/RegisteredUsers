from firebase import firebase


def fetch_json(event_id=None):
    base_url = 'https://cerebro-2018-f1052.firebaseio.com/'
    if event_id is None:
        firebase_obj = firebase.FirebaseApplication(base_url)
        result = firebase_obj.get('events', None)
    else:
        base_url += 'events/'
        # print(base_url)
        firebase_obj = firebase.FirebaseApplication(base_url)
        result = firebase_obj.get(str(event_id), None)
    # print(result)
    return result
