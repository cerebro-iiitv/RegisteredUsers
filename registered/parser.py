from registered import fetch


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
        # print(raw_data['name'])
        participant_list = []
        participant_obj = raw_data['participants']
        for participant in participant_obj:
            # print(participant_obj[participant]['name'])
            participant_list.append(str(participant_obj[participant]['name']))
        obj.append([
                        str(raw_data['name']),
                        participant_list
        ])

    print(obj)
    return obj


tmp = parse_json(0)
print(tmp[0][0])
print(tmp[0][1])
