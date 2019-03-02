from registered import fetch
from RegisteredUsers.settings import PARTICIPANTS_LIST


def parse_json(event_id=None):
    raw_data = fetch.fetch_json(event_id=event_id)
    obj = []
    if event_id is None:
        for event in raw_data:
            if event is not None:
                obj.append([
                                str(event['id']),
                                str(event['name']),
                                str(len(event['participants'])),
                        ])
                # print(event['name'], len(event['participants']))
    else:
        participant_list = []
        participant_obj = raw_data['participants']
        for participant in participant_obj:
            # print(participant_obj[participant]['uid'] in PARTICIPANTS_LIST)
            if participant_obj[participant]['uid'] in PARTICIPANTS_LIST:
                temp = PARTICIPANTS_LIST[participant_obj[participant]['uid']].get('phone', None)
                # print(temp)
                participant_list.append([ str(participant_obj[participant]['name']), str(temp)])
            else:
                participant_list.append([ str(participant_obj[participant]['name']), 'Not Given'])
        obj.append([
                        str(raw_data['name']),
                        participant_list
        ])

    # print(obj)
    return obj


tmp = parse_json(0)
# print(tmp)
# print(tmp[0][0])
# print(tmp[0][1])
