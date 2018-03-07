from firebase import firebase


def get_json():
    firebase_obj = firebase.FirebaseApplication('https://cerebro-2018-f1052.firebaseio.com/')
    result = firebase_obj.get('/events', None)
    return result


if __name__ == '__main__':
    get_json()
