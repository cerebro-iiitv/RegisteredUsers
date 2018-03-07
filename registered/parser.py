from registered import fetch


def parse_json(event_id=None):
    raw_data = fetch.fetch_json(event_id=event_id)
    obj = {}
    count = 0
    if event_id is None:
        for event in raw_data:
            if event is not None:
                obj.update({
                    str(count): {
                        'name': str(event['name']),
                        'count': str(len(event['participants'])),
                    }
                })
                # print(event['name'], len(event['participants']))
                count += 1
    else:
        # print(raw_data['name'])
        participant_list = []
        participant_obj = raw_data['participants']
        for participant in participant_obj:
            # print(participant_obj[participant]['name'])
            participant_list.append({
                'id': count,
                'name': participant_obj[participant]['name']
            })
        obj.update({
            str(event_id): {
                'name': str(raw_data['name']),
                'participants': participant_list
            }
        })
    print(obj)
    return obj
